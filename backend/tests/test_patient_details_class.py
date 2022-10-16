import pytest
from backend.source.parser_patient_details_class import PatientParser


@pytest.fixture()
def doc_1_kathy():
    text = """17/12/2020
            
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
            
            List any Medical Problems (asthma, seizures, headaches):
            
            Migraine"""
    return PatientParser(text)


@pytest.fixture()
def doc_2_jerry():
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
    return PatientParser(text)


def test_get_patient_name(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_general('patient_name') == 'Kathy Crawford'
    assert doc_2_jerry.get_general('patient_name') == 'Jerry Lucas'


def test_get_patient_number(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_general('patient_number') == '(737) 988-0851'
    assert doc_2_jerry.get_general('patient_number') == '(279) 920-8204'


def test_get_patient_hepatitis_status(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_general('hepatitis_status') == 'No'
    assert doc_2_jerry.get_general('hepatitis_status') == 'Yes'


def test_get_patient_medical_problems(doc_1_kathy, doc_2_jerry):
    assert doc_1_kathy.get_general('medical_problems') == 'Migraine'
    assert doc_2_jerry.get_general('medical_problems') == 'N/A'


def test_parse(doc_1_kathy, doc_2_jerry):
    record_kathy = doc_1_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['patient_number'] == '(737) 988-0851'
    assert record_kathy['hepatitis_status'] == 'No'
    assert record_kathy['medical_problems'] == 'Migraine'

    record_kathy = doc_2_jerry.parse()
    assert record_kathy['patient_name'] == 'Jerry Lucas'
    assert record_kathy['patient_number'] == '(279) 920-8204'
    assert record_kathy['hepatitis_status'] == 'Yes'
    assert record_kathy['medical_problems'] == 'N/A'

