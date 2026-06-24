import os
from PIL import Image
import pytesseract

def read_text_file(file_path):
    """Read plain text or log files"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading text file: {e}")
        return None


def read_pdf(file_path):
    """Extract text from PDF"""
    try:
        import PyPDF2
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None


def read_image(file_path):
    """Extract text from image using OCR"""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error reading image: {e}")
        return None


def detect_file_type(file_path):
    """Detect file type based on extension"""
    _, ext = os.path.splitext(file_path)
    return ext.lower()


def process_file(file_path):
    """Main handler to process any file"""
    file_type = detect_file_type(file_path)

    if file_type in ['.txt', '.log']:
        return read_text_file(file_path)

    elif file_type == '.pdf':
        return read_pdf(file_path)

    elif file_type in ['.png', '.jpg', '.jpeg']:
        return read_image(file_path)

    else:
        print(f"Unsupported file type: {file_type}")
        return None


if __name__ == "__main__":
    sample_path = "data/processed/sample.txt"
    content = process_file(sample_path)
    print(content[:500] if content else "No content extracted")