# 📝 **Exercice TDD - Application de gestion de tâches**

## **Objectif**
Dans cet exercice, vous devez appliquer la **méthode TDD** (Test Driven Development) pour développer une API de gestion de tâches. Vous devez écrire les tests **avant** de coder les fonctionnalités.  

## **Fonctionnalités à développer**
1. **Créer une nouvelle tâche** via une requête **POST /tasks**.  
2. **Lister toutes les tâches** via une requête **GET /tasks**.  

## **Structure du projet**
tdd-todo-app/ 
├── app/ 
│ ├── app.py # Contient l'API Flask 
├── tests/ 
│ └── test_taches.py # Écrivez vos tests ici 
├── requirements.txt # Dépendances du projet 
└── README.md # Instructions de l'exercice


---

## ⚙️ **Étapes à suivre**
1. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
 ```
2. **Lancer les tests** :

   ```bash
   pytest 
 ```
3. **Écrire les tests (RED)** : Complétez les tests vides dans tests/test_taches.py.

4. **Écrire le code (GREEN)** : Complétez le fichier app/app.py pour faire passer les tests au vert.

5. **Refactoriser (REFACTOR)** : Améliorez le code, supprimez les répétitions, etc.

---

## ⚙️ **Exemple de test à écrire**

 Exemple de test à compléter (dans tests/test_taches.py) :

 ```python
def test_creer_tache_sans_titre(client):
    """
    Teste la tentative de création d'une tâche sans titre.
    """
    response = client.post('/tasks', json={})
    assert response.status_code == 400  # On attend un statut 400
    data = response.get_json()
    assert 'erreur' in data  # Vérifiez qu'un message d'erreur est renvoyé

 ```
--- 
## ⚙️ **Commandes utiles**

Lancer l'application :
```bash
python app/app.py
```

Lancer les tests :
```bash
pytest
```

---

## ⚙️ **Tâches des étudiants**

Compléter les tests manquants dans tests/test_taches.py.
Écrire des tests supplémentaires pour les cas non couverts (par exemple, tester la suppression de tâches).
Respecter la méthodologie RED - GREEN - REFACTOR.

---

## **Bonne chance et n'oubliez pas de suivre la méthodologie TDD ! 🚀**