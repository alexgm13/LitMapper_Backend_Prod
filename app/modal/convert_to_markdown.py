import modal


image = (
    modal.Image.debian_slim()
    .apt_install("git", "libgl1", "libglib2.0-0", "poppler-utils", "tesseract-ocr")
    .pip_install("marker-pdf", "torch", "transformers", "surya-ocr")
)

app = modal.App("marker-pdf-parser")

@app.cls(image=image, gpu="T4", timeout=600, container_idle_timeout=300)
class MarkerRemote:
    
    @modal.enter()
    def load_models(self):
        from marker.models import create_model_dict
        from marker.converters.pdf import PdfConverter
        
        self.artifact_dict = create_model_dict()
        
        self.converter = PdfConverter(
            artifact_dict=self.artifact_dict
        )

    @modal.method()
    def parse(self, pdf_bytes: bytes):
        import tempfile
        import os
        from marker.output import text_from_rendered
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf_bytes)
            tmp_path = tmp.name

        try:
            rendered = self.converter(tmp_path)
            text, metadata, images = text_from_rendered(rendered)
            
            return text
            
        except Exception as e:
            print(f"❌ Error: {e}")
            raise e
            
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)