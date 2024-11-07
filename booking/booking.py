import json
from concurrent import futures

import grpc

import booking_pb2
import booking_pb2_grpc


class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('./data/bookings.json', 'r') as jsf:
            self.db = json.load(jsf)['bookings']

    def get_showtimes_stub(self):
        channel = grpc.insecure_channel('localhost:3002')
        return booking_pb2_grpc.TimesStub(channel)

    def GetAllBookings(self, request, context):
        for booking in self.db:
            datesList = [
                booking_pb2.DateData(
                    date=dateEntry['date'],
                    moviesData=[
                        booking_pb2.MovieData(
                            movieId=movieEntry
                        ) for movieEntry in dateEntry['movies']
                    ]
                ) for dateEntry in booking['dates']
            ]
            yield booking_pb2.BookingData(
                userId=booking['userid'],
                dates=datesList
            )

    def GetUsersBookings(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.id:
                datesList = [
                    booking_pb2.DateData(
                        date=dateEntry['date'],
                        moviesData=[
                            booking_pb2.MovieData(
                                movieId=movieEntry
                            ) for movieEntry in dateEntry['movies']
                        ]
                    ) for dateEntry in booking['dates']
                ]
                return booking_pb2.BookingData(
                    userId=booking['userid'],
                    dates=datesList
                )
        return booking_pb2.BookingData(
            userId=request.id,
            dates=[]
        )

    def GetShowtimesBookings(self, request, context):
        for booking in self.db:
            for dateEntry in booking['dates']:
                if dateEntry['date'] == request.date:
                    for movieEntry in dateEntry['movies']:
                        if movieEntry == request.movie:
                            datesList = [
                                booking_pb2.DateData(
                                    date=dateEntry['date'],
                                    moviesData=[
                                        booking_pb2.MovieData(
                                            movieId=movieEntry
                                        ) for movieEntry in dateEntry['movies']
                                    ]
                                ) for dateEntry in booking['dates']
                            ]
                            yield booking_pb2.BookingData(
                                userId=booking['userid'],
                                dates=datesList
                            )

    def AddBooking(self, request, context):
        times = self.get_showtimes_stub().GetShowtimes(booking_pb2.Empty())

        for time in times:
            if time.date == request.date:
                if request.movie in time.movie:
                    for booking in self.db:
                        if booking['userid'] == request.user:
                            for dateEntry in booking['dates']:
                                if dateEntry['date'] == request.date:
                                    dateEntry['movies'].append(request.movie)
                                    with open('./data/bookings.json', 'w') as jsf:
                                        json.dump({"bookings": self.db}, jsf)
                                    return booking_pb2.AddBookingResponse(
                                        response=booking_pb2.Response(
                                            success=True,
                                            message="Booking added successfully"
                                        )
                                    )
                            booking['dates'].append({
                                "date": request.date,
                                "movies": [request.movie]
                            })
                            with open('./data/bookings.json', 'w') as jsf:
                                json.dump({"bookings": self.db}, jsf)
                            return booking_pb2.AddBookingResponse(
                                response=booking_pb2.Response(
                                    success=True,
                                    message="Booking added successfully"
                                )
                            )
                    self.db.append({
                        "userid": request.user,
                        "dates": [
                            {
                                "date": request.date,
                                "movies": [request.movie]
                            }
                        ]
                    })
                    with open('./data/bookings.json', 'w') as jsf:
                        json.dump({"bookings": self.db}, jsf)
                    return booking_pb2.AddBookingResponse(
                        response=booking_pb2.Response(
                            success=True,
                            message="Booking added successfully"
                        )
                    )

    def DeleteBooking(self, request, context):
        for booking in self.db:
            if booking['userid'] == request.user:
                for dateEntry in booking['dates']:
                    if dateEntry['date'] == request.date:
                        if request.movie in dateEntry['movies']:
                            dateEntry['movies'].remove(request.movie)
                            with open('./data/bookings.json', 'w') as jsf:
                                json.dump({"bookings": self.db}, jsf)
                            return booking_pb2.DeleteBookingResponse(
                                response=booking_pb2.Response(
                                    success=True,
                                    message="Booking deleted successfully"
                                )
                            )
        return booking_pb2.DeleteBookingResponse(
            response=booking_pb2.Response(
                success=False,
                message="Booking not found"
            )
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()