from pdf2image import convert_from_path
# used to convert the pdf to an image
import pytesseract
# exact text from images using pytesseract
from PIL import Image
# pillow makes the pic printable as an image and not only an array
import utils

from parser_perscription_class import PrescriptionParser
from parser_patient_details_class import PatientParser

POPPLER_PATH = r'C:\Users\nessa\poppler-22.04.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path: str, file_type: str):
    # step 1: extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    whole_text = ''

    if len(pages) > 0:
        page = pages[0]
        preprocessed_page = utils.preprocessing_images(page)
        text = pytesseract.image_to_string(preprocessed_page, lang="eng")
        whole_text += text
    # return whole_text
    # step 2: extract the fields form text
    if file_type == "prescription":
        extracted = PrescriptionParser(whole_text).parse()
    elif file_type == "patient_details":
        extracted = PatientParser(whole_text).parse()
    else:
        raise Exception(f"Invalid Document format: {file_type}")
    return extracted


if __name__ == "__main__":
    patient_details1 = extract(r"C:\Users\nessa\MedicalProject\backend\resources\patient_details\pd_1.pdf",
                               "patient_details")
    patient_details2 = extract(r"C:\Users\nessa\MedicalProject\backend\resources\patient_details\pd_2.pdf",
                               "patient_details")

    print(patient_details1, "\n", patient_details2)

    prescription1 = extract(r"C:\Users\nessa\MedicalProject\backend\resources\prescription\pre_1.pdf",
                            "prescription")

    prescription2 = extract(r"C:\Users\nessa\MedicalProject\backend\resources\prescription\pre_2.pdf",
                            "prescription")
    print(prescription1, "\n", prescription2)
