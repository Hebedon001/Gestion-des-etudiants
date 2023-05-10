from flask import Flask, jsonify, request
import sqlite3


app = Flask(__name__)

# Route pour obtenir tous les enregistrements de la base de données

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

# Route pour ajouter un nouvel enregistrement à la base de données
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (nom, postnom,prenom) VALUES (?, ?,?)', (data['nom'], data['postnom'],data['prenom']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User added successfully'})

# Route pour mettre à jour un enregistrement existant dans la base de données
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET nom=?, postnom=? ,prenom=? WHERE id=?', (data['nom'], data['postnom'],data['prenom'], user_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User updated successfully'})

# Route pour supprimer un enregistrement de la base de données
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id=?', (user_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
