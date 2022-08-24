from pdf2image import convert_from_path
# used to convert the pdf to an image
import pytesseract
# exact text from images using pytesseract
from PIL import Image
# pillow makes the pic printable as a image and not only an array
import utils

POPPLER_PATH = r'C:\Users\nessa\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path: str, file_type: str):
    # extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    whole_text = ''
    for page in pages:
        preprocessed_page = utils.preprocessing_images(page)
        text = pytesseract.image_to_string(preprocessed_page, lang="eng")
        whole_text += text
    return whole_text
    # if file_type == "prescription":
    #     pass
    # elif file_type == "patient_details":
    #     pass


if __name__ == "__main__":
    data = extract(r"C:\Users\nessa\MedicalProject\backend\resources\prescription\pre_2.pdf", "prescription")
    print(data)