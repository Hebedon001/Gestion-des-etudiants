import requests

SERVER_URL = 'http://localhost:5000'


# Fonction pour obtenir tous les utilisateurs de la base de données
def get_users():
    response = requests.get(f'{SERVER_URL}/users')
    if response.status_code == 200:

        return response.json()
    else:
        return []


# Fonction pour ajouter un nouvel utilisateur à la base de données
def add_user(nom, postnom, prenom):
    data = {'nom': nom, 'postnom': postnom, 'prenom': prenom}
    response = requests.post(f'{SERVER_URL}/users', json=data)
    if response.status_code == 200:
        return True
    else:
        return False

# Fonction pour mettre à jour un utilisateur existant dans la base de données
def update_user(user_id, nom, postnom, prenom):
    data = {'nom': nom, 'postnom': postnom, 'prenom': prenom}
    response = requests.put(f'{SERVER_URL}/users/{user_id}', json=data)
    if response.status_code == 200:
        return True
    else:
        return False


# Fonction pour supprimer un utilisateur de la base de données
def delete_user(user_id):
    response = requests.delete(f'{SERVER_URL}/users/{user_id}')
    if response.status_code == 200:
        return True
    else:
        return False


import tkinter as tk
from tkinter import ttk, messagebox

from tkinter import *


def GetValue(event):
    id.delete(0, END)
    nom.delete(0, END)
    postnom.delete(0, END)
    prenom.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    id.insert(0, select['id'])
    nom.insert(0, select['Nom'])
    postnom.insert(0, select['Postnom'])
    prenom.insert(0, select['Prenom'])


def Add():
    nm = nom.get()
    ptm = postnom.get()
    prn = prenom.get()
    try:
        add_user(nm, ptm, prn)

        id.delete(0, END)
        nom.delete(0, END)
        postnom.delete(0, END)
        prenom.delete(0, END)
        id.focus_set()
        show()
    except Exception as e:
        print(e)


def update():
    try:
        update_user(id.get(), nom.get(), postnom.get(), prenom.get())

        id.delete(0, END)
        nom.delete(0, END)
        postnom.delete(0, END)
        prenom.delete(0, END)
        id.focus_set()
        show()
    except Exception as e:

        print(e)


def delete():
    try:
        delete_user(id.get())
        id.delete(0, END)
        nom.delete(0, END)
        postnom.delete(0, END)
        prenom.delete(0, END)
        id.focus_set()
        show()
    except Exception as e:

        print(e)


def show():
    users = get_users()
    # Supprime les enregistrements existants dans le Treeview
    listBox.delete(*listBox.get_children())
    for i in users:
        listBox.insert("", "end", values=(i[0], i[1], i[2], i[3]))


root = Tk()
root.geometry("800x500")
global id  # id
global nom
global postnom
global prenom

tk.Label(root, text=" GESTION DES ETUDIANTS ", fg="red", font=(None, 30)).place(x=300, y=5)

tk.Label(root, text="ID").place(x=10, y=10)
Label(root, text="Nom").place(x=10, y=40)
Label(root, text="Postnom").place(x=10, y=70)
Label(root, text="Prenom").place(x=10, y=100)

id = Entry(root)
id.place(x=140, y=10)

nom = Entry(root)
nom.place(x=140, y=40)

postnom = Entry(root)
postnom.place(x=140, y=70)

prenom = Entry(root)
prenom.place(x=140, y=100)

Button(root, text="Ajouter", command=Add, height=3, width=13).place(x=30, y=130)
Button(root, text="Modiffier", command=update, height=3, width=13).place(x=140, y=130)
Button(root, text="Supprimer", command=delete, height=3, width=13).place(x=250, y=130)

cols = ('id', 'Nom', 'Postnom', 'Prenom')
listBox = ttk.Treeview(root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>', GetValue)

root.mainloop()