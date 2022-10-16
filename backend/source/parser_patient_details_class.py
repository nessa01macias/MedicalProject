from backend.source.parser_generic_class import MedicalDocParser
import re


class PatientParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    @staticmethod
    def remove_noise_from_name(name):
        name = name.replace("Birth Date", "").strip()
        pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ 0-9]+)'
        date_matches = re.findall(pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name

    def get_general(self, option_text: str) -> str:
        dictionary = {
            "patient_name": "Patient Information(.*?)\(\d{3}\)",
            "patient_number": "Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})",
            "hepatitis_status": "Have you had the Hepatitis B vaccination\?.*(Yes|No)",
            "medical_problems": "List any Medical Problems \(asthma, seizures, headaches[\}|\)]:(.*)"
        }
        if dictionary[option_text]:
            match = re.findall(dictionary[option_text], self.text, re.DOTALL)
            # print(match)
            if option_text == "patient_name":
                name = self.remove_noise_from_name(match[0])
                return name.strip()
            if option_text == "patient_number":
                return match[0][1].strip()
            else:
                return match[0].strip()

    def parse(self):
        return {
            "patient_name": self.get_general('patient_name'),
            "patient_number": self.get_general('patient_number'),
            "hepatitis_status": self.get_general('hepatitis_status'),
            "medical_problems": self.get_general('medical_problems'),
        }


if __name__ == "__main__":
    text = """Patient Medical Record

            Patient Information Birth Date

            Jerry Lucas May 2 1998

            (279) 920-8204 Weight:

            4218 Wheeler Ridge Dr 57

            Buffalo, New York, 14201 Height:

            United States gnt
            170

            In Case of Emergency

            - eee

            Joe Lucas . 4218 Wheeler Ridge Dr
            Buffalo, New York, 14201
            Home phone United States
            Work phone

            General Medical History

            Chicken Pox (Varicelia): Measles: ..

            IMMUNE NOT IMMUNE

            Have you had the Hepatitis B vaccination?

            ‘Yes

            | List any Medical Problems (asthma, seizures, headaches):
            N/A"""

    text2= """17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 '

United States Height:
190

In Case of Emergency
ee J
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
nn ee
Chicken Pox (Varicella): Measies:
IMMUNE

IMMUNE
Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches}:

Migraine"""
    data = PatientParser(text2)
    print(data.parse())
