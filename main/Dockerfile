# app/Dockerfile
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Ajoutez /app au PYTHONPATH
ENV PYTHONPATH=/app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu du projet dans le conteneur
COPY . .

# Spécifier le fichier principal à exécuter
CMD ["python", "app.py"]