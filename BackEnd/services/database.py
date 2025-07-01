import sqlite3 
import os


def get_connection():
    
    # Pega o caminho da pasta onde o script está
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Monta o caminho para a pasta 'data'
    db_path = os.path.join(BASE_DIR, '..', 'data', 'listaCompras.db')

    conn = sqlite3.connect(db_path)
    #comando no SQLite para ativar as regras de integridade
    conn.execute("PRAGMA foreign_keys = ON")
    conn.row_factory = sqlite3.Row
    return conn
