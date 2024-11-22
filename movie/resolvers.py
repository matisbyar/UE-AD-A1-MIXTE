import json
import os

# Helper to get file paths
BASE_DIR = os.path.dirname(__file__)
MOVIES_FILE = os.path.join(BASE_DIR, 'data', 'movies.json')
ACTORS_FILE = os.path.join(BASE_DIR, 'data', 'actors.json')


# Helper functions for file operations
def load_json_file(filepath):
    with open(filepath, "r") as file:
        return json.load(file)


def save_json_file(filepath, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


# MOVIES RESOLVERS

def get_movies_file():
    return load_json_file(MOVIES_FILE)


def movies(_, info):
    """Return all movies"""
    return get_movies_file().get('movies', [])


def movie_with_id(_, info, id):
    """Return movie by ID"""
    return next((movie for movie in get_movies_file().get('movies', []) if movie['id'] == id), None)


def movie_with_title(_, info, title):
    """Return movie by title"""
    return next((movie for movie in get_movies_file().get('movies', []) if movie['title'] == title), None)


def add_movie(_, info, id, title, director, rating):
    movies_data = get_movies_file()
    if any(movie['id'] == id for movie in movies_data.get('movies', [])):
        return None

    new_movie = {"id": id, "title": title, "director": director, "rating": rating}
    movies_data['movies'].append(new_movie)
    save_json_file(MOVIES_FILE, movies_data)
    return new_movie


def update_movie_rate(_, info, id, rate):
    movies_data = get_movies_file()
    for movie in movies_data.get('movies', []):
        if movie['id'] == id:
            movie['rating'] = rate
            save_json_file(MOVIES_FILE, movies_data)
            return movie
    return None


def delete_movie(_, info, id):
    movies_data = get_movies_file()
    movie_to_delete = next((movie for movie in movies_data.get('movies', []) if movie['id'] == id), None)
    if movie_to_delete:
        movies_data['movies'].remove(movie_to_delete)
        save_json_file(MOVIES_FILE, movies_data)
    return movie_to_delete


def movies_with_director(_, info, director):
    """Return movies with director"""
    return [movie for movie in get_movies_file().get('movies', []) if movie['director'] == director]


def movies_with_rating(_, info, rating, rating_type):
    """
    Return movies by rating with a comparison type (gt(e): greater than, lt(e): less than, eq: equal)
    """
    movies_data = get_movies_file()
    movies = movies_data.get('movies', [])
    if rating_type == 'gt':
        return [movie for movie in movies if movie['rating'] > rating]
    elif rating_type == 'gte':
        return [movie for movie in movies if movie['rating'] >= rating]
    elif rating_type == 'lt':
        return [movie for movie in movies if movie['rating'] < rating]
    elif rating_type == 'lte':
        return [movie for movie in movies if movie['rating'] <= rating]
    elif rating_type == 'eq':
        return [movie for movie in movies if movie['rating'] == rating]
    return []


# ACTORS RESOLVERS

def get_actors_file():
    return load_json_file(ACTORS_FILE)


def resolve_actors_in_movie(movie, info):
    """Return actors in a specific movie by movie ID"""
    return [actor for actor in get_actors_file().get('actors', []) if movie['id'] in actor['films']]


def actors(_, info):
    """Return all actors"""
    return get_actors_file().get('actors', [])


def actor_with_id(_, info, id):
    """Return actor by ID"""
    return next((actor for actor in get_actors_file().get('actors', []) if actor['id'] == id), None)


def add_actor(_, info, id, firstname, lastname, birthyear, films):
    actors_data = get_actors_file()
    if any(actor['id'] == id for actor in actors_data.get('actors', [])):
        return None

    new_actor = {"id": id, "firstname": firstname, "lastname": lastname, "birthyear": birthyear, "films": films}
    actors_data['actors'].append(new_actor)
    save_json_file(ACTORS_FILE, actors_data)
    return new_actor


def update_actor_info(_, info, id, firstname, lastname, birthyear):
    actors_data = get_actors_file()
    for actor in actors_data.get('actors', []):
        if actor['id'] == id:
            if firstname:
                actor['firstname'] = firstname

            if lastname:
                actor['lastname'] = lastname

            if birthyear:
                actor['birthyear'] = birthyear

            save_json_file(ACTORS_FILE, actors_data)
            return actor
    return None


def add_movie_to_actor(_, info, actor_id, movie_id):
    actors_data = get_actors_file()
    for actor in actors_data.get('actors', []):
        if actor['id'] == actor_id:
            actual_list = actor['films']
            actual_list.append(movie_id)

            save_json_file(ACTORS_FILE, actors_data)
            return actor
    return None


def delete_actor(_, info, id):
    actors_data = get_actors_file()
    actors_to_delete = next((actor for actor in actors_data.get('actors', []) if actor['id'] == id), None)
    if actors_to_delete:
        actors_data["actors"].remove(actors_to_delete)
        save_json_file(ACTORS_FILE, actors_data)
    return actors_to_delete
