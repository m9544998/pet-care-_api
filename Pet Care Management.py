from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "pets.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS pets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pet_name TEXT NOT NULL,
        pet_type TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


init_db()


# Add Pet
@app.route("/pets", methods=["POST"])
def add_pet():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Data is required"}), 400

    pet_name = data.get("pet_name")
    pet_type = data.get("pet_type")

    if not pet_name or not pet_type:
        return jsonify({
            "error": "pet_name and pet_type are required"
        }), 400

    try:

        conn = get_db()

        cursor = conn.execute(
            """
            INSERT INTO pets(
            pet_name,
            pet_type
            )
            VALUES(?,?)
            """,
            (pet_name, pet_type)
        )

        conn.commit()

        pet_id = cursor.lastrowid

        conn.close()

        return jsonify({
            "message": "Pet added successfully",
            "pet_id": pet_id
        }), 201

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500


# View All Pets
@app.route("/pets", methods=["GET"])
def get_pets():

    try:

        conn = get_db()

        pets = conn.execute(
            "SELECT * FROM pets"
        ).fetchall()

        conn.close()

        return jsonify([
            dict(pet)
            for pet in pets
        ])

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500


# Get Pet By ID
@app.route("/pets/<int:id>", methods=["GET"])
def get_pet(id):

    try:

        conn = get_db()

        pet = conn.execute(
            "SELECT * FROM pets WHERE id=?",
            (id,)
        ).fetchone()

        conn.close()

        if pet is None:
            return jsonify({
                "error": "Pet not found"
            }), 404

        return jsonify(
            dict(pet)
        )

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500


# Delete Pet
@app.route("/pets/<int:id>", methods=["DELETE"])
def delete_pet(id):

    try:

        conn = get_db()

        pet = conn.execute(
            "SELECT * FROM pets WHERE id=?",
            (id,)
        ).fetchone()

        if pet is None:

            conn.close()

            return jsonify({
                "error": "Pet not found"
            }), 404

        conn.execute(
            "DELETE FROM pets WHERE id=?",
            (id,)
        )

        conn.commit()

        conn.close()

        return jsonify({
            "message": "Pet deleted successfully"
        })

    except sqlite3.Error as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)