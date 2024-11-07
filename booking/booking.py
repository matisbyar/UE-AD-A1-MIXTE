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
        """
        Get the showtimes stub
        :return: showtimes stub
        """
        channel = grpc.insecure_channel('localhost:3002')
        return booking_pb2_grpc.TimesStub(channel)

    def GetAllBookings(self, request, context):
        """
        Get all bookings
        """
        for booking in self.db:
            dates_list = [
                booking_pb2.DateData(
                    date=date_entry['date'],
                    moviesData=[
                        booking_pb2.MovieData(
                            movieId=movie_entry
                        ) for movie_entry in date_entry['movies']
                    ]
                ) for date_entry in booking['dates']
            ]
            yield booking_pb2.BookingData(
                userId=booking['userid'],
                dates=dates_list
            )

    def GetUsersBookings(self, request, context):
        """
        Get bookings by user
        """
        for booking in self.db:
            if booking['userid'] == request.id:
                dates_list = [
                    booking_pb2.DateData(
                        date=date_entry['date'],
                        moviesData=[
                            booking_pb2.MovieData(
                                movieId=movie_entry
                            ) for movie_entry in date_entry['movies']
                        ]
                    ) for date_entry in booking['dates']
                ]
                return booking_pb2.BookingData(
                    userId=booking['userid'],
                    dates=dates_list
                )
        return booking_pb2.BookingData(
            userId=request.id,
            dates=[]
        )

    def GetShowtimesBookings(self, request, context):
        """
        Get bookings by showtimes
        """
        for booking in self.db:
            for date_entry in booking['dates']:
                if date_entry['date'] == request.date:
                    for movie_entry in date_entry['movies']:
                        if movie_entry == request.movie:
                            dates_list = [
                                booking_pb2.DateData(
                                    date=date_entry['date'],
                                    moviesData=[
                                        booking_pb2.MovieData(
                                            movieId=movie_entry
                                        ) for movie_entry in date_entry['movies']
                                    ]
                                ) for date_entry in booking['dates']
                            ]
                            yield booking_pb2.BookingData(
                                userId=booking['userid'],
                                dates=dates_list
                            )

    def AddBooking(self, request, context):
        """
        Add booking
        """
        times = self.get_showtimes_stub().GetShowtimes(booking_pb2.Empty())

        for time in times:
            if time.date == request.date and request.movie in time.movie:
                for booking in self.db:
                    if booking['userid'] == request.user:
                        for date_entry in booking['dates']:
                            if date_entry['date'] == request.date:
                                date_entry['movies'].append(request.movie)
                                self._save_db()
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
                        self._save_db()
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
                self._save_db()
                return booking_pb2.AddBookingResponse(
                    response=booking_pb2.Response(
                        success=True,
                        message="Booking added successfully"
                    )
                )

    def DeleteBooking(self, request, context):
        """
        Delete booking
        """
        for booking in self.db:
            if booking['userid'] == request.user:
                for date_entry in booking['dates']:
                    if date_entry['date'] == request.date and request.movie in date_entry['movies']:
                        date_entry['movies'].remove(request.movie)
                        self._save_db()
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

    def _save_db(self):
        """
        Save the database to the JSON file
        """
        with open('./data/bookings.json', 'w') as jsf:
            json.dump({"bookings": self.db}, jsf)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
