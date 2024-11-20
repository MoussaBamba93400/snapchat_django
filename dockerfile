# Étape 1 : Utilisation d'une image Python de base
FROM python:3.10-slim

# Étape 2 : Définir le répertoire de travail
WORKDIR /app

# Étape 3 : Copier les fichiers nécessaires pour installer les dépendances
COPY requirements.txt /app/

# Étape 4 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Copier tout le projet dans le conteneur
COPY . /app/

# Étape 6 : Ajouter les commandes pour le conteneur
# Exposition du port 8000 (Django utilise généralement ce port)
EXPOSE 8000

# Commande pour collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Commande par défaut pour démarrer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
