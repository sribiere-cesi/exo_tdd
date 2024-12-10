import pytest
from app.app import app

# Configurer le client Flask pour les tests
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_creer_tache_avec_succes(client):
    """
    Teste la création d'une tâche valide.
    Les étudiants doivent compléter ce test.
    """
    # TODO : Complétez la requête POST et les assertions
    response = client.post('/tasks', json={'titre': 'Apprendre le TDD'})
    assert response.status_code == 201  # Le statut de la réponse doit être 201 Created
    data = response.get_json()
    assert data['titre'] == 'Apprendre le TDD'  # Vérifier que le titre de la tâche est correct
    assert 'id' in data  # Vérifier que l'identifiant a bien été généré


def test_creer_tache_sans_titre(client):
    """
    Teste la tentative de création d'une tâche sans titre.
    Les étudiants doivent compléter ce test.
    """
    # TODO : Complétez la requête POST et les assertions
    response = client.post('/tasks', json={})  # On envoie des données vides
    assert response.status_code == 400  # On attend un statut 400 Bad Request
    data = response.get_json()
    assert 'erreur' in data  # Vérifier que l'erreur est bien signalée


def test_lister_taches(client):
    """
    Teste la récupération de la liste des tâches.
    Les étudiants doivent compléter ce test.
    """
    # TODO : Complétez la création de quelques tâches avant de les lister
    client.post('/tasks', json={'titre': 'Tâche 1'})
    client.post('/tasks', json={'titre': 'Tâche 2'})
    response = client.get('/tasks')
    assert response.status_code == 200  # Le statut de la réponse doit être 200 OK
    data = response.get_json()
    assert len(data) == 2  # On doit avoir deux tâches
