# Booking Service - gRPC API

Le service **Booking** est un service gRPC qui permet de gérer les réservations de films. Il permet aux utilisateurs de
réserver des films, de consulter leurs réservations, de supprimer une réservation, etc. Le service interagit avec un
service Showtime pour vérifier la disponibilité des films et avec un service User pour valider les utilisateurs.

Le service expose une API gRPC via le port **3002**.

## Table des matières

1. [Description du service](#description-du-service)
2. [Schéma gRPC](#schéma-grpc)
3. [Méthodes disponibles](#méthodes-disponibles)
4. [Exemples d'utilisation](#exemples-dutilisation)
5. [Installation et démarrage](#installation-et-démarrage)
6. [Technologies utilisées](#technologies-utilisées)

## Description du service

Le service **Booking** permet aux utilisateurs de réserver des films à des dates spécifiques. Il interroge un service
Showtime pour obtenir les horaires disponibles pour les films et vérifie que l'utilisateur existe via un service
externe (User) avant d'effectuer une réservation.

Les principales opérations offertes par ce service sont :

- **GetAllBookings** : Récupère toutes les réservations de films.
- **GetUsersBookings** : Récupère les réservations d'un utilisateur donné.
- **GetShowtimesBookings** : Récupère les réservations pour un film à une date spécifique.
- **AddBooking** : Permet à un utilisateur de réserver un film à une date spécifique.
- **DeleteBooking** : Permet de supprimer une réservation existante.

## Schéma gRPC

### Service : `Booking`

Le service `Booking` expose les méthodes suivantes :

```proto
service Booking {
  rpc GetAllBookings(EmptyBooking) returns (stream BookingData);
  rpc GetUsersBookings(UserId) returns (BookingData);
  rpc GetShowtimesBookings(Showtime) returns (stream BookingData);
  rpc AddBooking(AddBookingData) returns (AddBookingResponse);
  rpc DeleteBooking(DeleteBookingData) returns (DeleteBookingResponse);
}
```

### Messages

#### `BookingData`

```proto
message BookingData {
  string userId = 1;
  repeated DateData dates = 2;
}
```

#### `DateData`

```proto
message DateData {
  string date = 1;
  repeated MovieId movies = 2;
}
```

#### `MovieId`

```proto
message MovieId {
  string id = 1;
}
```

#### `UserId`

```proto
message UserId {
  string id = 1;
}
```

#### `Showtime`

```proto
message Showtime {
  string date = 1;
  string movie = 2;
}
```

#### `AddBookingData`

```proto
message AddBookingData {
  string user = 1;
  string date = 2;
  string movie = 3;
}
```

#### `DeleteBookingData`

```proto
message DeleteBookingData {
  string user = 1;
  string date = 2;
  string movie = 3;
}
```

#### `AddBookingResponse`

```proto
message AddBookingResponse {
  Response response = 1;
}
```

#### `DeleteBookingResponse`

```proto
message DeleteBookingResponse {
  Response response = 1;
}
```

#### `Response`

```proto
message Response {
  bool success = 1;
  string message = 2;
}
```

#### `EmptyBooking`

```proto
message EmptyBooking {}
```

## Méthodes disponibles

### 1. `GetAllBookings`

**Description** : Cette méthode récupère toutes les réservations de films dans le système.

**Entrée** : Aucune (message `EmptyBooking`).

**Sortie** : Un flux de messages `BookingData`, un pour chaque réservation.

**Exemple d'appel** :

```proto
rpc GetAllBookings(EmptyBooking) returns (stream BookingData);
```

### 2. `GetUsersBookings`

**Description** : Cette méthode permet de récupérer les réservations d'un utilisateur spécifique en fonction de son
`id`.

**Entrée** : Un message `UserId` contenant l'ID de l'utilisateur.

**Sortie** : Un message `BookingData` avec les réservations de cet utilisateur.

**Exemple d'appel** :

```proto
rpc GetUsersBookings(UserId) returns (BookingData);
```

### 3. `GetShowtimesBookings`

**Description** : Cette méthode permet de récupérer les réservations effectuées pour un film donné à une date
spécifique.

**Entrée** : Un message `Showtime` contenant la date et le titre du film.

**Sortie** : Un flux de messages `BookingData` pour chaque réservation correspondant à cette date et à ce film.

**Exemple d'appel** :

```proto
rpc GetShowtimesBookings(Showtime) returns (stream BookingData);
```

### 4. `AddBooking`

**Description** : Cette méthode permet à un utilisateur de réserver un film à une date donnée. Elle vérifie que
l'utilisateur existe et que le film est disponible via le service Showtime.

**Entrée** : Un message `AddBookingData` contenant l'ID de l'utilisateur, la date et le film à réserver.

**Sortie** : Un message `AddBookingResponse` contenant un message indiquant si la réservation a été effectuée avec
succès.

**Exemple d'appel** :

```proto
rpc AddBooking(AddBookingData) returns (AddBookingResponse);
```

### 5. `DeleteBooking`

**Description** : Cette méthode permet de supprimer une réservation existante pour un utilisateur donné.

**Entrée** : Un message `DeleteBookingData` contenant l'ID de l'utilisateur, la date et le film à supprimer.

**Sortie** : Un message `DeleteBookingResponse` contenant un message indiquant si la suppression a réussi.

**Exemple d'appel** :

```proto
rpc DeleteBooking(DeleteBookingData) returns (DeleteBookingResponse);
```

## Exemples d'utilisation

### Requête : Obtenir toutes les réservations

```graphql
query {
    GetAllBookings {
        userId
        dates {
            date
            movies {
                id
            }
        }
    }
}
```

### Requête : Ajouter une réservation

```graphql
mutation {
    AddBooking(user: "1234", date: "2024-11-20", movie: "Inception") {
        response {
            success
            message
        }
    }
}
```

### Requête : Supprimer une réservation

```graphql
mutation {
    DeleteBooking(user: "1234", date: "2024-11-20", movie: "Inception") {
        response {
            success
            message
        }
    }
}
```

## Installation et démarrage

1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre-utilisateur/booking-service.git
   cd booking-service
   ```

2. Installez les dépendances nécessaires :
   ```bash
   pip install grpcio grpcio-tools requests
   ```

3. Générez les fichiers Python à partir du fichier `.proto` :
   ```bash
   python -m grpc_tools.protoc --python_out=. --grpc_python_out=. booking.proto
   ```

4. Démarrez le serveur gRPC :
   ```bash
   python server.py
   ```

Le serveur gRPC sera maintenant accessible sur `localhost:3002`.

## Technologies utilisées

- **gRPC** : Framework pour la communication entre services via RPC.
- **Protocol Buffers (proto3)** : Format de sérialisation pour définir les messages et services.
- **Python** : Langage pour implémenter le serveur et la logique métier.
- **Requests** : Bibliothèque pour effectuer des requêtes HTTP (utilisée pour vérifier les utilisateurs).

## Conclusion

Le service **Booking** permet de gérer les réservations de films pour les utilisateurs via une API gRPC. Il s'intègre
avec des services externes (Showtime pour vérifier les horaires des films, User pour valider les utilisateurs) et offre
une interface simple pour ajouter, supprimer et consulter les réservations.