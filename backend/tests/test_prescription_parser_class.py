from backend.source.parser_perscription_class import PrescriptionParser


# unit tests for checking all the functionalities of the prescription class
def test_get_name():
    obj = PrescriptionParser(data)
    assert obj.get_general("patient_name") == "Marta Sharapova"


def test_get_address():
    obj = PrescriptionParser(data)
    assert obj.get_general("patient_address") == "9 tennis court, new Russia, DC"


def test_get_instruction():
    obj = PrescriptionParser(data)
    assert obj.get_general(
        "patient_instruction") == 'Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'


def test_get_prescription():
    obj = PrescriptionParser(data)
    assert obj.get_prescription() == 'Prednisone 20 mg\nLialda 2.4 gram'


def test_get_refill():
    obj = PrescriptionParser(data)
    assert obj.get_general("patient_refill") == "2"


data = """Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times


"""
test_get_name()
test_get_address()
test_get_instruction()
