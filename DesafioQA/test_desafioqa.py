import requests

def test_numero_extenso_um():
    ret= requests.get("http://challengeqa.staging.devmuch.io/1")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'um'

def test_numero_extenso_zero():
    ret= requests.get("http://challengeqa.staging.devmuch.io/0")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'zero'

def test_numero_extenso_dez_mil():
    ret= requests.get("http://challengeqa.staging.devmuch.io/10000")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'dez mil'

def test_numero_extenso_dez_mil_um():
    ret= requests.get("http://challengeqa.staging.devmuch.io/10001")
    retjson = ret.json()
    assert ret.status_code == 400
    assert retjson['extenso'] == 'Invalid data'

def test_numero_extenso_menos_dez_mil():
    ret= requests.get("http://challengeqa.staging.devmuch.io/-10000")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'menos dez mil'

def test_numero_extenso_menos_dez_mil_um():
    ret= requests.get("http://challengeqa.staging.devmuch.io/-10001")
    retjson = ret.json()
    assert ret.status_code == 400
    assert retjson['extenso'] == 'Invalid data'


#testes números inglês
def test_numero_extenso_en_um():
    ret= requests.get("http://challengeqa.staging.devmuch.io/1")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'pne'

def test_numero_extenso_en_zero():
    ret= requests.get("http://challengeqa.staging.devmuch.io/0")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'zero'

def test_numero_extenso_en_dez_mil():
    ret= requests.get("http://challengeqa.staging.devmuch.io/10000")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'ten thousand'

def test_numero_extenso_en_dez_mil_um():
    ret= requests.get("http://challengeqa.staging.devmuch.io/10001")
    retjson = ret.json()
    assert ret.status_code == 400
    assert retjson['extenso'] == 'Invalid data'

def test_numero_extenso_en_menos_dez_mil():
    ret= requests.get("http://challengeqa.staging.devmuch.io/-10000")
    retjson = ret.json()
    assert ret.status_code == 200
    assert retjson['extenso'] == 'minus ten thousand'

def test_numero_extenso_en_menos_dez_mil_um():
    ret= requests.get("http://challengeqa.staging.devmuch.io/-10001")
    retjson = ret.json()
    assert ret.status_code == 400
    assert retjson['extenso'] == 'Invalid data'