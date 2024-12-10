from flask import Flask, request, jsonify

app = Flask(__name__)

# Données en mémoire pour stocker les tâches (à améliorer)
taches = []

@app.route('/tasks', methods=['POST'])
def creer_tache():
    """Créer une tâche à partir des données reçues dans la requête POST."""
    data = request.json
    if not data or 'titre' not in data:
        return jsonify({'erreur': 'Titre requis'}), 400
    tache = {
        'id': len(taches) + 1,
        'titre': data['titre']
    }
    taches.append(tache)
    return jsonify(tache), 201

@app.route('/tasks', methods=['GET'])
def lister_taches():
    """Retourner la liste des tâches."""
    return jsonify(taches), 200

if __name__ == '__main__':
    app.run(debug=True)
