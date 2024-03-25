import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('todo_list.db')
cursor = conn.cursor()

# User Authentication Logic
def register_user(username, password):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Task CRUD Operations
def add_task(user_id, description, due_date, priority, notes, tags):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (user_id, description, due_date, priority, notes, tags) VALUES (?, ?, ?, ?, ?, ?)', (user_id, description, due_date, priority, notes, tags))
    conn.commit()
    conn.close()

def get_tasks(username):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE user_id = ?', (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def mark_task_complete(task_id):
    cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()

def edit_task(task_id, description, due_date, priority, notes, tags):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET description=?, due_date=?, priority=?, notes=?, tags=? WHERE id=?',
                   (description, due_date, priority, notes, tags, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    conn.close()

def get_task_details(task_id):
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task_details = cursor.fetchone()
    conn.close()
    return task_details

cursor.execute('''
               CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   username TEXT UNIQUE,
                   password TEXT
               )
        ''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    description TEXT,
                    due_date TEXT,
                    priority TEXT,
                    notes TEXT,
                    tags TEXT,
                    completed INTEGER DEFAULT 0,
                    FOREIGN KEY (user_id) REFERENCES users(id)
               )
        ''')


conn.commit()