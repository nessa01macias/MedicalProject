from parser_generic_class import MedicalDocParser
import re
#re allows selection specific characters in a text

class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)
    
    def get_general(self, option_text: str):
        dictionary = { 
            'patient_name':{
                'pattern': "Name:(.+)Date:",
                'flags': 0
            },
            'patient_address':{
                'pattern': "Address:(.*)\n",
                'flags': 0
            },
            'patient_instructions':{
                'pattern': "Directions:(.*)Refill:",
                'flags': re.DOTALL
            },
            'patient_refill':{
                'pattern': "Refill:(.*)times",
                'flags': re.DOTALL
            }
        }
        new_dictionary = dictionary.get(option_text)
        if new_dictionary != None:
            math = re.findall(new_dictionary['pattern'], self.text, new_dictionary['flags'])
            return math[0].strip() if len(math)>0 else None

    def get_prescription(self):
        pattern = "Address[^\n]*(.*)Directions:"
        # re.DOTALL because now we are working with multiple lines where we dont want \n to count
        math = re.findall(pattern, self.text, flags = re.DOTALL)
        math = "".join(math)
        math = math.replace('K', '')
        return math.strip() if len(math)>0 else None

    def parse(self):
        return {
            'patient_name': self.get_general('patient_name'),
            'patient_address': self.get_general('patient_address'),
            'patient_prescription': self.get_prescription(),
            'patient_instruction' : self.get_general('patient_instruction'),
            'patient_refill' : self.get_general('patient_refill')
        }


if __name__ == "__main__":
    data = PrescriptionParser("""Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times


""")
    print(data.parse())