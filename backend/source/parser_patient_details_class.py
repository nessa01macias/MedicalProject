from parser_generic_class import MedicalDocParser
import re


class PatientParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    @staticmethod
    def get_bool_status(status: str) -> bool:
        if status == "Yes":
            return True
        return False

    def get_general(self):
        dic = {
            "patient_name": "",
            "patient_number": "",
            "hepatitis_status": "",  # self.get_bool_status("")
            "medical_problems": ""
        }

    def parse(self):
        pass
