# Movie Service - GraphQL API

Le service **Movie** permet de gérer des informations sur les films et les acteurs dans une base de données via une API
GraphQL. Il permet de récupérer des données sur les films et les acteurs, ainsi que d'ajouter, de modifier ou de
supprimer ces informations.

Le service expose une API GraphQL en port **3002** qui peut être utilisée pour interagir avec la base de données des
films et des acteurs.

## Table des matières

1. [Description du service](#description-du-service)
2. [Schéma GraphQL](#schéma-graphql)
3. [Requêtes disponibles](#requêtes-disponibles)
4. [Mutations disponibles](#mutations-disponibles)
5. [Exemples d'utilisation](#exemples-dutilisation)
6. [Technologies utilisées](#technologies-utilisées)

## Description du service

Le service **Movie** expose une API GraphQL pour interagir avec les films et les acteurs. Vous pouvez effectuer des
requêtes pour obtenir des informations détaillées sur les films, les acteurs, ou effectuer des mutations pour modifier
ces données.

L'API prend en charge les opérations suivantes :

- **Films** : Rechercher des films par différents critères (titre, ID, réalisateur, note, etc.).
- **Acteurs** : Rechercher des acteurs, ajouter ou modifier des acteurs, et les associer à des films.

## Schéma GraphQL

Le schéma GraphQL définit deux types principaux (`Movie` et `Actor`), ainsi que plusieurs requêtes et mutations
disponibles pour interagir avec ces types.

### Types

#### `Movie`

```graphql
type Movie {
    id: String!
    title: String!
    director: String!
    rating: Float!
    actors: [Actor]
}
```

#### `Actor`

```graphql
type Actor {
    id: String!
    firstname: String!
    lastname: String!
    birthyear: Int!
    films: [String!]
}
```

#### `RatingType`

```graphql
enum RatingType {
    eq
    gt
    gte
    lt
    lte
}
```

### Requêtes disponibles

Les requêtes suivantes permettent de récupérer des informations sur les films et les acteurs.

#### 1. `movies`

```graphql
movies: [Movie]
```

Récupère la liste de tous les films disponibles.

#### 2. `movieWithId`

```graphql
movieWithId(id: String!): Movie
```

Récupère un film par son ID.

**Paramètres** :

- `id` : L'ID du film.

#### 3. `movieWithTitle`

```graphql
movieWithTitle(title: String!): Movie
```

Récupère un film par son titre.

**Paramètres** :

- `title` : Le titre du film.

#### 4. `moviesWithRating`

```graphql
moviesWithRating(rating: Float!, rating_type: RatingType!): [Movie]
```

Récupère les films dont la note correspond à un certain critère.

**Paramètres** :

- `rating` : La note du film.
- `rating_type` : Le type de comparaison pour la note (`eq`, `gt`, `gte`, `lt`, `lte`).

#### 5. `moviesWithDirector`

```graphql
moviesWithDirector(director: String!): [Movie]
```

Récupère les films réalisés par un réalisateur donné.

**Paramètres** :

- `director` : Le nom du réalisateur.

#### 6. `actors`

```graphql
actors: [Actor]
```

Récupère la liste de tous les acteurs.

#### 7. `actorWithId`

```graphql
actorWithId(id: String!): Actor
```

Récupère un acteur par son ID.

**Paramètres** :

- `id` : L'ID de l'acteur.

### Mutations disponibles

Les mutations suivantes permettent de créer, modifier ou supprimer des films et des acteurs.

#### 1. `addMovie`

```graphql
addMovie(id: String!, title: String!, director: String!, rating: Float!): Movie
```

Ajoute un nouveau film.

**Paramètres** :

- `id` : L'ID du film.
- `title` : Le titre du film.
- `director` : Le nom du réalisateur.
- `rating` : La note du film.

#### 2. `updateMovieRate`

```graphql
updateMovieRate(id: String!, rate: Float!): Movie
```

Met à jour la note d'un film existant.

**Paramètres** :

- `id` : L'ID du film.
- `rate` : La nouvelle note du film.

#### 3. `deleteMovie`

```graphql
deleteMovie(id: String!): Movie
```

Supprime un film par son ID.

**Paramètres** :

- `id` : L'ID du film à supprimer.

#### 4. `addActor`

```graphql
addActor(id: String!, firstname: String!, lastname: String!, birthyear: Int!, films: [String]): Actor
```

Ajoute un nouvel acteur.

**Paramètres** :

- `id` : L'ID de l'acteur.
- `firstname` : Le prénom de l'acteur.
- `lastname` : Le nom de l'acteur.
- `birthyear` : L'année de naissance de l'acteur.
- `films` : Une liste d'IDs des films dans lesquels l'acteur a joué.

#### 5. `updateActorInfo`

```graphql
updateActorInfo(id: String!, firstname: String, lastname: String, birthyear: Int): Actor
```

Met à jour les informations d'un acteur.

**Paramètres** :

- `id` : L'ID de l'acteur.
- `firstname` : Le prénom de l'acteur (optionnel).
- `lastname` : Le nom de l'acteur (optionnel).
- `birthyear` : L'année de naissance de l'acteur (optionnel).

#### 6. `addMovieToActor`

```graphql
addMovieToActor(actor_id: String!, movie_id: String!): Actor
```

Ajoute un film à la liste des films d'un acteur.

**Paramètres** :

- `actor_id` : L'ID de l'acteur.
- `movie_id` : L'ID du film.

#### 7. `deleteActor`

```graphql
deleteActor(id: String!): Actor
```

Supprime un acteur par son ID.

**Paramètres** :

- `id` : L'ID de l'acteur à supprimer.

## Exemples d'utilisation

### Requête : Obtenir tous les films

```graphql
query {
    movies {
        id
        title
        director
        rating
    }
}
```

### Requête : Obtenir un film par ID

```graphql
query {
    movieWithId(id: "1") {
        id
        title
        director
        rating
    }
}
```

### Mutation : Ajouter un film

```graphql
mutation {
    addMovie(id: "10", title: "Inception", director: "Christopher Nolan", rating: 9.0) {
        id
        title
        director
        rating
    }
}
```

### Mutation : Mettre à jour la note d'un film

```graphql
mutation {
    updateMovieRate(id: "1", rate: 8.7) {
        id
        title
        rating
    }
}
```

### Mutation : Ajouter un acteur à un film

```graphql
mutation {
    addMovieToActor(actor_id: "2", movie_id: "1") {
        id
        firstname
        lastname
        films
    }
}
```

## Technologies utilisées

- GraphQL : Langage de requête pour les API.
- Python : Environnement d'exécution pour le serveur.

## Conclusion

Le service **Movie** permet une gestion complète des films et des acteurs via une API GraphQL. Vous pouvez facilement
récupérer des informations, ajouter ou modifier des films et acteurs, ainsi que gérer les relations entre les acteurs et
les films.