from io import BytesIO
from typing import List

from fastapi import UploadFile
from pypdf import PdfReader


async def extract_text_from_uploadfile(upload_file: UploadFile) -> str:
	"""Read an UploadFile (PDF) and return combined text from all pages."""
	data = await upload_file.read()
	return extract_text_from_bytes(data)


def extract_text_from_bytes(data: bytes) -> str:
	"""Extract text from PDF bytes and combine pages into a single string."""
	reader = PdfReader(BytesIO(data))
	pages_text: List[str] = []
	for page in reader.pages:
		# pypdf's `extract_text` may return None for empty pages
		text = page.extract_text() or ""
		pages_text.append(text)
    
	# Join pages with double newlines to preserve basic separation
	cleaned_pages=[]
	for p in pages_text:
		cleaned = p.strip()
		if cleaned:
			cleaned_pages.append(cleaned)
	combined="\n\n".join(cleaned_pages)
	return combined

