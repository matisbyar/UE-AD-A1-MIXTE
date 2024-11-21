import json
from concurrent import futures

import grpc
import requests

import booking_pb2
import booking_pb2_grpc
import showtime_pb2
import showtime_pb2_grpc


class BookingServicer(booking_pb2_grpc.BookingServicer):

    def __init__(self):
        with open('./data/bookings.json', 'r') as jsf:
            self.db = json.load(jsf)['bookings']

    def get_showtimes_stub(self):
        """
        Get the showtimes stub
        :return: showtimes stub
        """
        with grpc.insecure_channel('localhost:3002') as channel:
            return booking_pb2_grpc.TimesStub(channel)

    def GetAllBookings(self, request, context):
        """
        Get all bookings
        """
        for booking in self.db:
            dates_list = [
                booking_pb2.DateData(
                    date=date_entry['date'],
                    movies=[
                        booking_pb2.MovieId(
                            id=movie_entry
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
                        movies=[
                            booking_pb2.MovieId(
                                id=movie_entry
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
        Get bookings by showtimes of users from one movie and one date
        """
        for booking in self.db:
            for date_entry in booking['dates']:
                if date_entry['date'] == request.date:
                    for movie_entry in date_entry['movies']:
                        if movie_entry == request.movie:
                            dates_list = [
                                booking_pb2.DateData(
                                    date=date_entry['date'],
                                    movies=[
                                        booking_pb2.MovieId(
                                            id=movie_entry
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
        # Check if the user exists
        user_response = requests.get(f'http://localhost:3004/user/{request.user}')
        if user_response.status_code != 200:
            return booking_pb2.AddBookingResponse(
                response=booking_pb2.Response(
                    success=False,
                    message="User does not exist"
                )
            )

        with grpc.insecure_channel('localhost:3003') as channel:
            times_stub = showtime_pb2_grpc.TimesStub(channel)
            times = times_stub.GetShowtimes(showtime_pb2.EmptyTimes())

            for schedule in times:
                if schedule.date == request.date:
                    if request.movie not in [movie.movie for movie in schedule.movies]:
                        return booking_pb2.AddBookingResponse(
                            response=booking_pb2.Response(
                                success=False,
                                message="No showtime for this movie on the given date"
                            )
                        )
                    break
            else:
                return booking_pb2.AddBookingResponse(
                    response=booking_pb2.Response(
                        success=False,
                        message="No showtime for this date"
                    )
                )

        # Check if the user has already booked this movie on the given date
        user_entry = next((entry for entry in self.db if entry["userid"] == request.user), None)
        if user_entry:
            date_entry = next((entry for entry in user_entry["dates"] if entry["date"] == request.date), None)
            if date_entry and request.movie in date_entry["movies"]:
                return booking_pb2.AddBookingResponse(
                    response=booking_pb2.Response(
                        success=False,
                        message="User has already booked this movie on the given date"
                    )
                )

        # Add the booking
        if user_entry is None:
            self.db.append({
                "userid": request.user,
                "dates": [
                    {
                        "date": request.date,
                        "movies": [request.movie]
                    }
                ]
            })
        else:
            if date_entry is None:
                user_entry["dates"].append({"date": request.date, "movies": [request.movie]})
            else:
                date_entry["movies"].append(request.movie)

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
    """
    Starts the gRPC server to serve ShowtimeServicer.

    The server listens on port 3002.
    """
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3002')
    server.start()
    print("Booking service started on port 3002.")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
