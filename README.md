# UE-AD-A1-MIXTE

# 🪪 Description du projet

Ce projet est une application de réservation de séances de cinéma. L'application est composée de 4 services qui
communiquent entre eux.

✨ Le projet a été réalisé dans le cadre du cours Architectures Distribuées A1 à l'IMT Atlantique par Matis BYAR et
Julien NGUYEN.

# 🗺️ Architecture du projet

Le projet est divisé en plusieurs dossiers qui représentent les différents services de l'application.

- `movie` : Service de gestion des films (port 3001)
- `booking` : Service de réservation (port 3002)
- `showtime` : Service de gestion des séances (port 3003)
- `user` : Service de gestion des utilisateurs (port 3004)

![Architecture du projet](https://helene-coullon.fr/images/graphql.png)

# ▶️ Comment lancer le projet

De prime abord, il faut installer les dépendances de chaque service. Pour cela, il suffit de lancer la commande suivante
dans chaque dossier :

```bash
pip install -r requirements.txt
```

Pour lancer le projet, il suffit de lancer les commandes suivantes dans 4 terminaux différents :

```bash
cd movie
python movie.py
```

```bash
cd booking
python booking.py
```

```bash
cd showtime
python showtime.py
```

```bash
cd user
python user.py
```

# 🚀 Utilisation de l'application

Tous les services ont une documentation disponibles dans les répertoires associés :

- [Booking](booking/UE-archi-distribuees-Booking-1.0.0-resolved.yaml)
- [Movie](movie/README.md)
- [Showtime](showtime/README.md)
- [User](user/README.md)