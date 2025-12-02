import modal

MarkerRemote = modal.Cls.from_name("marker-pdf-parser", "MarkerRemote")

class ModalClient:
    def __init__(self):
        self.marker_remote = MarkerRemote()

    def parse_pdf(self, pdf_bytes: bytes) -> str:
        return self.marker_remote.parse.remote(pdf_bytes)