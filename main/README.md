# bddd-tp

A faire : 

- Serveur MONGO DB

- Script de remplissage de la BDD (en .py)

- Script pour server web / front (en .py)
- uniformiser les couleurs du questionnaire avec la page home
- route home service, home accueil et home contact redirigent vers home, les enlever


Information que j'ai modifié (ewenn) : 

- app.py = ancien front.py
- création d'un dockerfile utilisant des requirements (dépendance : ne pas toucher). 
- docker compose est implémenté (flask et docker sans shard), mais pb dans les import,
  - en mode dev, le lancement de app.py fonctionne. 
- mise en place d'une bdd, possible de se connecter à la page home avec un id et mdp (fichier init_db)
- quleques modifications de code dans data et route mais rien de méchant normalement