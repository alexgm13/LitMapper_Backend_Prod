import re
from typing import Dict, List

def parse_markdown_to_sections(markdown_text: str) -> Dict[str, str]:


    header_pattern = re.compile(r'^(#{1,6})\s+(.*)', re.MULTILINE)
    
    sections = {}
    

    matches = list(header_pattern.finditer(markdown_text))
    
    if not matches:
        return {"General": markdown_text.strip()}

    if matches[0].start() > 0:
        preamble = markdown_text[:matches[0].start()].strip()
        if preamble:
            sections["_PREAMBLE_"] = preamble

    for i, match in enumerate(matches):
        raw_title = match.group(2).strip()
        clean_title = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', raw_title) 
        clean_title = clean_title.replace('*', '').strip() 
        
        start_index = match.end()
        
        if i < len(matches) - 1:
            end_index = matches[i + 1].start()
            content = markdown_text[start_index:end_index]
        else:
            content = markdown_text[start_index:]
            
        sections[clean_title] = content.strip()
        
    return sections

