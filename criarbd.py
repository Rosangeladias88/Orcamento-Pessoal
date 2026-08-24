# importando SQLite
import sqlite3 as lite


# Criando conexao
con = lite.connect('dados.db')

# Criando tabelas de categoria
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE inventorio(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DECIMAL, serie TEXT, imagem TEXT)')
