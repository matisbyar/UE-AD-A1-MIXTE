# UE-AD-A1-MIXTE

# Réalisé par

- Matis BYAR
- Julien NGUYEN

# Architecture du projet

Le projet est divisé en plusieurs dossiers qui représentent les différents services de l'application.

- `booking` : Service de réservation (port 3002)
- `movie` : Service de gestion des films (port 3001)
- `user` : Service de gestion des utilisateurs (port 3004)
- `showtime` : Service de gestion des séances (port 3003)

![Architecture du projet](https://helene-coullon.fr/images/graphql.png)

# Comment lancer le projet

De prime abord, il faut installer les dépendances de chaque service. Pour cela, il suffit de lancer la commande suivante
dans chaque dossier :

```bash
pip install -r requirements.txt
```

Pour lancer le projet, il suffit de lancer les commandes suivantes dans 4 terminaux différents :

```bash
cd booking
python booking.py
```

```bash
cd movie
python movie.py
```

```bash
cd user
python user.py
```

```bash
cd showtime
python showtime.py
```