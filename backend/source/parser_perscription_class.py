from backend.source.parser_generic_class import MedicalDocParser
# re allows selection specific characters in a text
import re
# punctuation includes the special string characters
from string import punctuation


class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    @staticmethod
    def check_punctuation(math: str) -> str:
        # this function will eliminate all the punctuation signs which should not be returned
        for letter in math.strip():
            if letter in punctuation and (letter != "." and letter != "," and letter != '-'):
                new_math = math.replace(letter, "")
                return new_math.strip()
        return math.strip() if len(math) > 0 else None

    def get_general(self, option_text: str) -> str:
        dictionary = {
            'patient_name': {
                'pattern': "Name:(.+)Date:",
                'flags': 0
            },
            'patient_address': {
                'pattern': "Address:(.*)\n",
                'flags': 0
            },
            'patient_instruction': {
                'pattern': "Directions:(.*)Refill:",
                'flags': re.DOTALL
            },
            'patient_refill': {
                'pattern': "Refill:(.*)times",
                'flags': re.DOTALL
            }
        }
        new_dictionary = dictionary.get(option_text)
        if new_dictionary:
            math = re.findall(new_dictionary['pattern'], self.text, new_dictionary['flags'])
            math = "".join(math)
            return self.check_punctuation(math)

    def get_prescription(self) -> str:
        pattern = "Address[^\n]*(.*)Directions:"
        # re.DOTALL because now we are working with multiple lines where we do not want \n to count
        math = re.findall(pattern, self.text, flags=re.DOTALL)
        math = "".join(math)
        math = math.replace('K', '')
        return self.check_punctuation(math)

    def parse(self) -> dict:
        return {
            'patient_name': self.get_general('patient_name'),
            'patient_address': self.get_general('patient_address'),
            'patient_prescription': self.get_prescription(),
            'patient_instruction': self.get_general('patient_instruction'),
            'patient_refill': self.get_general('patient_refill')
        }


if __name__ == "__main__":
    data = PrescriptionParser('')
    print(data.parse())
