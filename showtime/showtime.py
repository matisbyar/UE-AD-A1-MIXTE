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
            yield showtime_pb2.ShowtimeData(date=schedule['date'], movie=schedule['movie'])

    def GetShowtimeByDate(self, request, context):
        for schedule in self.db:
            if schedule['date'] == request.date:
                return showtime_pb2.ShowtimeData(date=schedule['date'], movie=schedule['movie'])
        return showtime_pb2.ShowtimeData(date="", movie=[])

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    showtime_pb2_grpc.add_TimesServicer_to_server(ShowtimeServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
