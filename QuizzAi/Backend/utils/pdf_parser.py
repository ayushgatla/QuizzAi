import PyPDF2
from fastapi import UploadFile, HTTPException
from io import BytesIO

async def extract_text_from_pdf(file: UploadFile) -> str:
    try:
        contents = await file.read()
        pdf_file = BytesIO(contents)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        num_pages = len(pdf_reader.pages)
        if num_pages == 0:
            raise HTTPException(status_code=400, detail="PDF file is empty or corrupted")
        
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            text += f"\n--- Page {page_num + 1} ---\n"
            text += page_text
        
        text = text.strip()
        
        if not text or len(text) < 10:
            raise HTTPException(
                status_code=400, 
                detail="Could not extract text from PDF. It might be scanned images."
            )
        
        print(f"✅ Extracted {len(text)} characters from {num_pages} pages")
        return text
        
    except PyPDF2.errors.PdfReadError as e:
        raise HTTPException(status_code=400, detail=f"Invalid PDF file: {str(e)}")
    
    except Exception as e:
        print(f"❌ Error extracting PDF: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")

def validate_pdf_file(file: UploadFile) -> bool:
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="File must be a PDF (.pdf extension)")
    
    if file.content_type and file.content_type != 'application/pdf':
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid content type: {file.content_type}. Expected application/pdf"
        )
    
    return True

def get_pdf_preview(text: str, length: int = 200) -> str:
    if len(text) <= length:
        return text
    return text[:length] + "..."