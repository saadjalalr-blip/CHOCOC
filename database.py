import sqlite3
import os

# 📌 تحديد المسار حسب البيئة
if os.name == "nt":  # Windows (VS Code)
    DB_PATH = "chocofit.db"
else:  # Linux (Render)
    DB_PATH = "/var/data/chocofit.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS commandes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prenom TEXT NOT NULL,
            email TEXT NOT NULL,
            telephone TEXT NOT NULL,
            adresse TEXT NOT NULL,
            produit TEXT NOT NULL,
            prix INTEGER NOT NULL,
            remise INTEGER NOT NULL,
            total INTEGER NOT NULL,
            rating INTEGER
        )
    """)

    conn.commit()
    conn.close()


def ajouter_commande(nom, prenom, email, telephone, adresse,
                     produit, prix, remise, total, rating):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO commandes
        (nom, prenom, email, telephone, adresse, produit, prix, remise, total, rating)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (nom, prenom, email, telephone, adresse,
          produit, prix, remise, total, rating))

    conn.commit()
    conn.close()
