import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '130964',
    'database': 'sistema_upa'
}

def conectar():
    return mysql.connector.connect(**DB_CONFIG)