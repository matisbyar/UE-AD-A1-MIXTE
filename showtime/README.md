# Showtime Service - gRPC API

Le service **Showtime** permet d'obtenir les informations sur les horaires des films à partir d'une base de données. Il
est accessible via le port **3003** et expose une API gRPC définie dans un fichier `proto`.

## Table des matières

1. [Description du service](#description-du-service)
2. [Schéma gRPC](#schéma-grpc)
3. [Méthodes disponibles](#méthodes-disponibles)
4. [Exemples d'utilisation](#exemples-dutilisation)
5. [Technologies utilisées](#technologies-utilisées)

## Description du service

Le service **Showtime** permet aux clients de consulter les horaires des films disponibles à des dates spécifiques.
L'API offre deux méthodes principales :

- **GetShowtimeByDate** : Récupère les horaires des films pour une date donnée.
- **GetShowtimes** : Récupère un flux continu des horaires des films disponibles.

Le service expose une interface gRPC sur le port **3003**.

## Schéma gRPC

Le service gRPC est défini dans le fichier `showtime.proto`. Voici la structure de ce fichier.

### Service : `Times`

```proto
service Times {
  rpc GetShowtimeByDate(ShowtimeDate) returns (ShowtimeData) {}
  rpc GetShowtimes(EmptyTimes) returns (stream ShowtimeData) {}
}
```

### Messages :

#### `ShowtimeDate`

```proto
message ShowtimeDate {
  string date = 1;  // La date pour laquelle on souhaite récupérer les horaires (format : "YYYY-MM-DD")
}
```

#### `ShowtimeData`

```proto
message ShowtimeData {
  string date = 1;  // La date des horaires retournés
  repeated MovieData movies = 2;  // Liste des films avec leurs horaires
}
```

#### `MovieData`

```proto
message MovieData {
  string movie = 1;  // Le nom du film
}
```

#### `EmptyTimes`

```proto
message EmptyTimes {}
```

## Méthodes disponibles

### 1. `GetShowtimeByDate`

- **Description** : Cette méthode permet de récupérer les horaires des films pour une date spécifique.
- **Entrée** : Un message `ShowtimeDate` contenant la date sous le format `"YYYY-MM-DD"`.
- **Sortie** : Un message `ShowtimeData` qui contient la date et la liste des films pour cette date.

**Exemple d'appel** :

```proto
rpc GetShowtimeByDate(ShowtimeDate) returns (ShowtimeData);
```

**Paramètres d'entrée** :

```json
{
  "date": "2024-11-15"
}
```

**Réponse possible** :

```json
{
  "date": "2024-11-15",
  "movies": [
    {
      "movie": "Le Seigneur des Anneaux"
    },
    {
      "movie": "Harry Potter"
    }
  ]
}
```

### 2. `GetShowtimes`

- **Description** : Cette méthode permet de récupérer un flux continu d'horaires de films disponibles. Cela peut être
  utile pour les services qui souhaitent mettre à jour en continu les horaires.
- **Entrée** : Le message `EmptyTimes`, ce qui signifie qu'aucun paramètre n'est requis.
- **Sortie** : Un flux (`stream`) de messages `ShowtimeData`, chaque message contenant les horaires pour une date
  spécifique.

**Exemple d'appel** :

```proto
rpc GetShowtimes(EmptyTimes) returns (stream ShowtimeData);
```

**Réponse possible** :

```json
{
  "date": "2024-11-15",
  "movies": [
    {
      "movie": "Avatar"
    },
    {
      "movie": "Interstellar"
    }
  ]
}
```

## Exemples d'utilisation

### Client gRPC en Python

Voici un exemple de client gRPC en Python pour interagir avec le service Showtime.

1. Installez les dépendances nécessaires :
   ```bash
   pip install grpcio grpcio-tools
   ```

2. Générez les fichiers Python à partir du fichier `.proto` :
   ```bash
   python -m grpc_tools.protoc --python_out=. --grpc_python_out=. showtime.proto
   ```

3. Code du client pour appeler `GetShowtimeByDate` :
   ```python
   import grpc
   import showtime_pb2
   import showtime_pb2_grpc

   def get_showtimes_by_date(date):
       channel = grpc.insecure_channel('localhost:3003')
       stub = showtime_pb2_grpc.TimesStub(channel)
       request = showtime_pb2.ShowtimeDate(date=date)
       response = stub.GetShowtimeByDate(request)
       for movie in response.movies:
           print(f"Movie: {movie.movie}")

   if __name__ == '__main__':
       get_showtimes_by_date("2024-11-15")
   ```

4. Code du client pour appeler `GetShowtimes` :
   ```python
   import grpc
   import showtime_pb2
   import showtime_pb2_grpc

   def get_showtimes():
       channel = grpc.insecure_channel('localhost:3003')
       stub = showtime_pb2_grpc.TimesStub(channel)
       request = showtime_pb2.EmptyTimes()
       for response in stub.GetShowtimes(request):
           print(f"Date: {response.date}")
           for movie in response.movies:
               print(f"  Movie: {movie.movie}")

   if __name__ == '__main__':
       get_showtimes()
   ```

## Technologies utilisées

- gRPC : Framework pour la communication entre services via RPC.
- Protocol Buffers (proto3) : Format de sérialisation pour définir les messages et les services.
- Python : Langage pour démonstration de l'appel du service via gRPC.

## Conclusion

Le service Showtime fournit une API simple et rapide pour récupérer les horaires des films. Vous pouvez l'utiliser pour
obtenir des informations sur les films disponibles pour une date donnée ou pour recevoir un flux en continu des
horaires.