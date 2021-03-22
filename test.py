import requests


def test():
    response = requests.post(
        'http://pingservice:8080/api/v1/ping',
        headers={'Content-Type': 'application/json'},
        json={'url': 'http://receiverservice:8080/api/v1/info'}
    )
    assert response.json() == {'Receiver': 'Cisco is the best!'}
    assert response.status_code == 200
