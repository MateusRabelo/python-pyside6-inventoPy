import sqlite3
import os

# Função para criar conexão com o banco de dados
def createConnection():
    try:
        conn = sqlite3.connect('./db/users.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None


# Função para criar a tabela de usuários
def createTable():
    conn = createConnection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

# Função para adicionar ou atualizar um usuário
def addOrUpdateUser(username, password):
    conn = createConnection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                # Update the existing user
                cursor.execute('UPDATE users SET password = ? WHERE username = ?',
                               (password, username))
            else:
                # Add a new user
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                               (username, password))
            
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print(f"Error adding/updating user: {e}")

# Função para obter todos os usuários
def getUsers():
    conn = createConnection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT id, username FROM users')
            users = cursor.fetchall()
            conn.close()
            return users
        except sqlite3.Error as e:
            print(f"Error retrieving users: {e}")
    
    return []

# Função para autenticar um usuário
def authUser(username, password):
    conn = createConnection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

if __name__ == '__main__':
    # Apagar o banco de dados existente se houver
    # if os.path.exists('./db/users.db'):
    #     print('Removing existing database...')
    #     os.remove('./db/users.db')

    # Criar a tabela de usuários
    createTable()

    # Adicionar um usuário de exemplo
    addOrUpdateUser('johndoe', 'password123')
    addOrUpdateUser('asda', 'aa')
    addOrUpdateUser('asdffasf', 'asddsa')
    addOrUpdateUser('admin', 'admin')
    addOrUpdateUser('teste1', 'teste1')
    addOrUpdateUser('test', 'test')
    addOrUpdateUser('Mateus', 'Rabelo')
    addOrUpdateUser('mateusaqles@gmail.com', '1232')
    addOrUpdateUser(' ', '1232')
    

    # Exibir todos os usuários
    print(getUsers())

    # Autenticar um usuário
    print(authUser('johndoe', 'password123'))
    print(authUser('asdffasf', 'asddsa'))
    print(authUser('asda', 'aa'))
    print(authUser('johndoe', 'wrongpassword'))
