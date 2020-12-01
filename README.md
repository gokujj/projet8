# Créez une plateforme pour amateurs de Nutella 🍫

## Introduction

For this project, the main goal is to create a web application that allows the user to search for a product into our database of Purbeurre. Indeed, the data that you will find in this application has been retrieved and cleaned off from OpenFoodFacts and fed to our database.

## Dependencies

The Pur Beurre application was developed using Python 3.8, Django, Boostrap4 web framework & SQLite.

To install the dependencies, the user will need to install the `pipenv` package using the `python3 -m pip install pipenv`

## Installation

The application can be installed by following the following steps:

1. Download the project from https://github.com/gokujj/projet8
2. Go to the project directory with the terminal
3. Install dependencies using the `pipenv install`
4. For launch app first start virtual environement `pipenv shell`
5. Current local database is empty for feed it `python manage.py makemigrations ` and `python manage.py migrate`
6. Load products from OpenFoodFacts with `python manage.py load_products`
7. Start app with `python manage.py runserver` and you can follow the instructions.
8.
