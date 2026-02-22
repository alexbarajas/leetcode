from enum import Enum


class FlightStatus(Enum):
    DELAY = 1
    ONTIME = 2
    CANCELLED = 3


class Flight:
    def __init__(self, flight_number: int, airline_company: str, seat_capacity: int, seats: list, schedule: list):
        self.flight_number = flight_number
        self.airline_company = Airline(airline_company)
        self.seat_capacity = seat_capacity
        self.seats = [Seat(seat['seat_number'], seat['class_name']) for seat in seats]
        self.schedule = schedule


class Airline:
    def __init__(self, airline_company: str):
        self.name = airline_company


class Seat:
    def __init__(self, seat_number: int, class_name: str):
        self.seat_number = seat_number
        self.class_name = class_name


class FlightSeat(Seat):
    def __init__(self, seat_number: int, class_name: str, price: float):
        super().__init__(seat_number, class_name)
        self.price = price
        self.available = True


class Schedule:
    def __init__(self, departure_time: str, arrival_time: str, departure_airport: str, arrival_airport: str,
                 status: FlightStatus):
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.status = status


seats_list = [
    {"seat_number": 1, "class_name": "Economy"},
    {"seat_number": 2, "class_name": "Business"},
    # Add more seats as needed
]

schedule = [
    Schedule(departure_time='2023-08-02 10:00', arrival_time='2023-08-02 14:00', departure_airport='JFK',
             arrival_airport='LAX', status=FlightStatus.ONTIME),
    Schedule(departure_time='2023-08-02 12:30', arrival_time='2023-08-02 16:30', departure_airport='LAX',
             arrival_airport='JFK', status=FlightStatus.DELAY),
    Schedule(departure_time='2023-08-02 09:45', arrival_time='2023-08-02 13:45', departure_airport='SFO',
             arrival_airport='SEA', status=FlightStatus.CANCELLED)
]

flight = Flight(flight_number=123, airline_company="Cocaina Airlines", seat_capacity=200, seats=seats_list,
                schedule=schedule)


# print(flight.schedule)


def hello(m, n, h, v):
    h_pointer = 0
    v_pointer = 0

    horizontal = 0
    vertical = 0

    current_horizontal = 0
    for i in range(1, m + 2):
        if h_pointer < len(h) and i == h[h_pointer]:
            h_pointer += 1
            continue
        horizontal = max(horizontal, i - current_horizontal)
        current_horizontal = i

    current_vertical = 0
    for j in range(1, n + 2):
        if v_pointer < len(h) and j == v[v_pointer]:
            v_pointer += 1
            continue
        vertical = max(vertical, j - current_vertical)
        current_vertical = j

    return horizontal * vertical


print(hello(m=6, n=6, h=[1], v=[2]))
