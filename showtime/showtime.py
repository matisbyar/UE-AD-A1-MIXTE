import json
from concurrent import futures

import grpc

import showtime_pb2
import showtime_pb2_grpc


class ShowtimeServicer(showtime_pb2_grpc.TimesServicer):

    def __init__(self):
        with open('{}/data/times.json'.format("."), "r") as jsf:
            self.db = json.load(jsf)["schedule"]

    def GetShowtimes(self, request, context):
        for schedule in self.db:
            yield showtime_pb2.ShowtimeData(
                date=schedule['date'],
                movies=[
                    showtime_pb2.MovieData(movie=movie)
                    for movie in schedule['movies']
                ]
            )

    def GetShowtimeByDate(self, request, context):
        for schedule in self.db:
            if schedule['date'] == request.date:
                return showtime_pb2.ShowtimeData(
                    date=schedule['date'],
                    movies=[
                        showtime_pb2.MovieData(movie=movie)
                        for movie in schedule['movies']
                    ]
                )
        return showtime_pb2.ShowtimeData(date="", movies=[])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_TimesServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3003')
    server.start()
    print("Showtime server running in port 3003")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
