from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType, MutationType
from flask import Flask, request, jsonify, make_response

import resolvers as r

PORT = 3001
HOST = '0.0.0.0'
app = Flask(__name__)

# Types déclarés dans le fichier movie.graphql
type_defs = load_schema_from_path('movie.graphql')

# Création des types
query = QueryType()
mutation = MutationType()
movie = ObjectType('Movie')
actor = ObjectType('Actor')

# Movie resolvers
query.set_field('movies', r.movies)
query.set_field('movieWithId', r.movie_with_id)
query.set_field('movieWithTitle', r.movie_with_title)

# Actor resolvers
query.set_field('actors', r.actors)
query.set_field('actorWithId', r.actor_with_id)

# Movie fields resolvers (actors)
movie.set_field('actors', r.resolve_actors_in_movie)


# Mutation resolvers
mutation.set_field('addMovie', r.add_movie)
mutation.set_field('updateMovieRate', r.update_movie_rate)
mutation.set_field('deleteMovie', r.delete_movie)

# Schema
schema = make_executable_schema(type_defs, movie, query, mutation, actor)


# root message
@app.route("/", methods=['GET'])
def home():
    return make_response("<h1 style='color:blue'>Welcome to the Movie service!</h1>", 200)


# graphql entry points
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=None,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
