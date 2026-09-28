#!/usr/bin/env bash
# exit on error
set -o errexit

# Installer les dépendances depuis requirements.txt
pip install -r requirements.txt

# Collecter les fichiers statiques
python manage.py collectstatic --no-input

# Appliquer les migrations de base de données
python manage.py migrate
