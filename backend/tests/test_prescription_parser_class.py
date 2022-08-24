from backend.source.parser_perscription_class import PrescriptionParser
import pytest


@pytest.fixture()
def example_text1():
    text1 = """Name: Marta Sharapova Date: 5/11/2022
    Address: 9 tennis court, new Russia, DC
    Prednisone 20 mg
    Lialda 2.4 gram
    Directions:
    Prednisone, Taper 5 mg every 3 days,
    Finish in 2.5 weeks a
    Lialda - take 2 pill everyday for 1 month
    Refill: 2 times
    """
    return PrescriptionParser(text1)


@pytest.fixture()
def example_text2():
    text2 = """Dr John >mith, M.D
    2 Non-Important street,
    New York, Phone (900)-323- ~2222
    Name:  Virat Kohli Date: 2/05/2022
    Address: 2 cricket blvd, New Delhi
    | Omeprazole 40 mg
    Directions: Use two tablets daily for three months
    Refill: 3 times
    """
    return PrescriptionParser(text2)


@pytest.fixture()
def example_text3():
    return PrescriptionParser('')


# unit tests for checking all the functionalities of the prescription class
def test_get_name(example_text1, example_text2, example_text3):
    assert example_text1.get_general("patient_name") == "Marta Sharapova"
    assert example_text2.get_general("patient_name") == "Virat Kohli"
    assert example_text3.get_general("patient_name") is None


def test_get_address(example_text1, example_text2, example_text3):
    assert example_text1.get_general("patient_address") == "9 tennis court, new Russia, DC"
    assert example_text2.get_general("patient_address") == "2 cricket blvd, New Delhi"
    assert example_text3.get_general("patient_address") is None


def test_get_instruction(example_text1, example_text2, example_text3):
    assert example_text1.get_general(
        "patient_instruction") == 'Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 weeks a\n    Lialda - take ' \
                                  '2 pill everyday for 1 month'
    assert example_text2.get_general(
        "patient_instruction") == 'Use two tablets daily for three months'
    assert example_text3.get_general("patient_instruction") is None


def test_get_prescription(example_text1, example_text2, example_text3):
    assert example_text1.get_prescription() == 'Prednisone 20 mg\n    Lialda 2.4 gram'
    assert example_text2.get_prescription() == 'Omeprazole 40 mg'
    assert example_text3.get_prescription() is None


def test_get_refill(example_text1, example_text2, example_text3):
    assert example_text1.get_general("patient_refill") == "2"
    assert example_text2.get_general("patient_refill") == "3"
    assert example_text3.get_general("patient_refill") is None


def test_parse(example_text1, example_text2, example_text3):
    assert example_text1.parse() == {'patient_name': 'Marta Sharapova', 'patient_address': '9 tennis court, new '
                                                                                           'Russia, DC',
                                     'patient_prescription': 'Prednisone 20 mg\n    Lialda 2.4 gram',
                                     'patient_instruction': 'Prednisone, Taper 5 mg every 3 days,\n    Finish in 2.5 '
                                                            'weeks a\n    Lialda - take 2 pill everyday for 1 month',
                                     'patient_refill': '2'}

    assert example_text2.parse() == {'patient_name': 'Virat Kohli', 'patient_address': '2 cricket blvd, New Delhi',
                                     'patient_prescription': 'Omeprazole 40 mg',
                                     'patient_instruction': 'Use two tablets daily for three months',
                                     'patient_refill': '3'}

    assert example_text3.parse() == {'patient_name': None, 'patient_address': None, 'patient_prescription': None,
                                     'patient_instruction': None, 'patient_refill': None}
