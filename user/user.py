# REST API
import json

import requests
from flask import Flask, request, jsonify, make_response

# CALLING gRPC requests
# import grpc
# from concurrent import futures
# import booking_pb2
# import booking_pb2_grpc
# import movie_pb2
# import movie_pb2_grpc

# from movie.movie import query

# CALLING GraphQL requests
# todo to complete

app = Flask(__name__)

PORT = 3004
HOST = '0.0.0.0'
MOVIES_GRAPHQL_ENDPOINT = "http://0.0.0.0:3001/graphql"

with open('{}/data/users.json'.format("."), "r") as jsf:
    users = json.load(jsf)["users"]


def write(bookings):
    data = {"users": bookings}
    with open('{}/databases/users.json'.format("."), 'w') as f:
        json.dump(data, f)


@app.route("/", methods=['GET'])
def home():
    return "<h1 style='color:blue'>Welcome to the User service!</h1>"


@app.route("/users", methods=['GET'])
def get_json():
    res = make_response(jsonify(users), 200)
    return res


@app.route("/user/<userId>", methods=['GET'])
def get_user_by_id(userId):
    for user in users:
        if str(user["id"]) == str(userId):
            res = make_response(jsonify(user), 200)
            return res
    return make_response(jsonify({"error": "No user with this ID"}), 400)


@app.route("/users/<userId>", methods=['POST'])
def add_user(userId):
    req = request.get_json()

    for user in users:
        if str(user["id"]) == str(userId):
            return make_response(jsonify({"error": "user ID already exists"}), 409)

    users.append(req)
    write(users)

    return make_response(jsonify({"message": "user added"}), 200)


@app.route("/user/<userId>", methods=['DELETE'])
def del_user(userId):
    for user in users:
        if str(user["id"]) == str(userId):
            users.remove(user)
            write(users)

            return make_response(jsonify(user), 200)

    return make_response(jsonify({"error": "user not found"}), 400)


@app.route("/user/<userId>", methods=['PUT'])
def update_user_lastactive(userId):
    last_active = request.args.get('last_active')

    for user in users:
        if str(user["id"]) == str(userId):
            user["last_active"] = last_active
            write(users)

            res = make_response(jsonify(user), 200)
            return res

    res = make_response(jsonify({"error": "user not found"}), 201)
    return res


@app.route("/user/<userId>/bookings/movies", methods=['GET'])
def get_movies_from_usersbooking(userId):
    # todo: call booking service to get user bookings
    # bookings_url = f"http://{request.remote_addr}:3201/bookings/{userId}"
    # bookings = requests.get(bookings_url)
    #
    # if bookings.status_code != 200:
    #     return make_response(jsonify({"error": "User has no bookings"}), 409)
    #
    # bookings_list = bookings.json()
    # movies = [movie for booking in bookings_list["dates"] for movie in booking["movies"]]
    #
    # if not movies:
    #     return make_response(jsonify({"error": "User has no bookings"}), 409)

    movies = ['276c79ec-a26a-40a6-b3d3-fb242a5947b6', 'OEHFUKE-ZLJEFHK2-92340824',
              '720d006c-3a57-4b6a-b18f-9b713b073f3c']

    movies_detailed = []
    for movie in movies:
        try:
            response = requests.post(MOVIES_GRAPHQL_ENDPOINT, json={
                "query": "{ movieWithId(id: \"" + movie + "\") { id title director rating actors { id firstname } } }"})
            response.raise_for_status()
            movies_detailed.append(response.json()['data']['movieWithId'])
        except requests.exceptions.RequestException as e:
            return make_response(jsonify({"error": str(e)}), 409)

    return make_response(jsonify({"movies": movies_detailed}), 200)


@app.route("/help", methods=['GET'])
def get_help_users():
    help = [
        {"path_and_method": "GET /users", "description": "Get all users"},
        {"path_and_method": "GET /user/<userId>", "description": "Get user by ID"},
        {"path_and_method": "GET /user/<userId>/bookings/movies",
         "description": "Retrieve all user's bookings by their ID"},
        {"path_and_method": "PUT /user/<userId>", "description": "Update user last_active timestamp by their ID"},
        {"path_and_method": "DELETE /user/<userId>", "description": "Delete user by ID"},
        {"path_and_method": "GET /help", "description": "Get help"}
    ]
    return make_response(jsonify(help), 200)


if __name__ == "__main__":
    print("Server running in port %s" % (PORT))
    app.run(host=HOST, port=PORT)
