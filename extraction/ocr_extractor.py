from PIL import Image
import pytesseract
import os

# ⚠️ Set your Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path):
    """Extract text from image using OCR"""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"OCR error (image): {e}")
        return None


def extract_text_from_pdf(pdf_path):
    """Extract text from PDF (basic)"""
    try:
        import PyPDF2
        text = ""

        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""

        return text.strip()

    except Exception as e:
        print(f"OCR error (pdf): {e}")
        return None


def extract_text(file_path):
    """Auto-detect file type and extract text"""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    elif ext == ".pdf":
        return extract_text_from_pdf(file_path)

    else:
        print(f"Unsupported file for OCR: {ext}")
        return None


if __name__ == "__main__":
    sample = "data/sample/test.png"
    result = extract_text(sample)
    print("Extracted Text:\n", result)