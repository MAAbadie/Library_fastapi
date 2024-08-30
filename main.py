from fastapi import FastAPI
from router import routes_book, routes_borrowing, routes_user
from db import models
from db.database import engine


app = FastAPI()
# app.include_router(routes_user.router)
# app.include_router(routes_book.router)
# app.include_router(routes_borrowing.router)


@app.get("/")
def index():
    return {'message': 'Welcome to this library API. Check the documentation to use it.'}


# TODO gestion des exceptions
# @app.exception_handler()

models.Base.metadata.create_all(engine)

origins = [
    'http://127.0.0.1:5100'
]


# How will we process
# define routes

# borrowing a book (borrow date, return date)
# add a book
# consult borrowings -

# define DB
# user
# book


## Exo 1: une API base de données

# Construire une API pour une base de données simple d'une bibliothèque avec SQLAlchemy.
# La base de données :
# - 2 entités :
#     - lecteur : nom, prénom, mail, password
#     - livres : titre, auteur, isbn
# - un lecteur peut emprunter un livre avec une date d'emprunt et une date de retour
# - un lecteur peut consulter ses emprunts en cours et passés
# - un lecteur peut consulter si un livre est disponible (pour simplifier on considère qu'il n'y a qu'un seul exemplaire de chaque livre)

# **Contraintes :**
# - Intégrer toutes les requêtes CRUD nécessaires.
# - Gérer les schémas de récupération des données du client et les schémas de réponse au client.
# - Intégrer l'authentification pour permettre à un lecteur authentifié de consulter ses emprunts