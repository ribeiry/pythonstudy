from fastapi.testclient import TestClient
from python.app.main import app

client = TestClient(app)


def test_root():
    """
        Test an endpoint root of package manager
    """
    resp = client.get("/")
    var = "../main.py"
    assert resp.status_code == 200
    assert resp.json() == {"message":"Welcome  manage package !"}


def test_package():
    """
        Test an endpoint create of package manager
    """
    resp = client.post(url="/encomendas",
                        headers={},
                        json={"_id": "066de609-b04a-4b30-b46c-32537c7f1f6s",
                              "endereco": "Avenida Joao de Barros,500",
                              "complemento": "Bloco A",
                              "remente": "MercadoLibre",
                              "apto": "84B",
                              "status": "Recebido",
                              "condominio": "vibe",
                              "destinatario": "Augusto"})

    assert resp.status_code == 201
    
