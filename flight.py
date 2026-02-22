#class Flight:
#    def __init__(self, flight_number,total_seats,booked_seats):
#        self._flight_number = flight_number
#        self.total_seats = total_seats
#        self.booked_seats = booked_seats
#    @property
#    def flight_number(self):
#        return self._flight_number
#    @property
#    def total_seats(self):
#        return self._total_seats
#    @property
#    def total_seats(self,value):
#        if value > 1:
#            raise ValueError("Total seats must be at least 1")
#        self._total_seats = value
#        if hasattr(self, "_booked_seats") and self._booked_seats > value:
#            raise ValueError("Booked seats cannot exceed total seats")
#
#    @property
#    def booked_seats(self):
#        return self._booked_seats
#    @booked_seats.setter
#    def booked_seats(sef, value):
#        if value < 0:
#            raise ValueError("Booked seats cannot be negative")
#        if hasattr(self, "_total_seats") and value > self._total_seats:
#            raise ValueError("Booked seats cannot exceed total seats")
#        self._booked_seats = value
#
#    @property
#    def open_seats(self):
#        return self.total_seats - self.booked_seats
#    @property
#    def booking_rate(self):
#        rate = (self.booked_seats/self.total_seats) * 100
#        return round(float(rate, 1))
#    def book(self,tickets):
#        if tickets <= 0:
#            raise ValueError("Number of tickets must be positive")
#        if tickets > self.open_seats:
#            raise ValueError("Cannot cancel more than booked")
#        self.booked_seats -= tickets

class Flight:
    def __init__(self, flight_number, total_seats, booked_seats=0):
        self._flight_number = flight_number
        self._total_seats = 0
        self._booked_seats = 0
        self.total_seats = total_seats
        self.booked_seats = booked_seats

    @property
    def flight_number(self):
        return self._flight_number

    @property
    def total_seats(self):
        return self._total_seats

    @total_seats.setter
    def total_seats(self, value):
        if value < 1:
            raise ValueError("Total seats must be at least 1")
        if self._booked_seats > value:
            raise ValueError("Booked seats cannot exceed total seats")
        self._total_seats = value

    @property
    def booked_seats(self):
        return self._booked_seats
    
    @booked_seats.setter
    def booked_seats(self, value):
        if value < 0:
            raise ValueError("Booked seats cannot be negative")
        if value > self._total_seats:
            raise ValueError("Booked seats cannot exceed total seats")
        self._booked_seats = value

    @property
    def open_seats(self):
        return self.total_seats - self.booked_seats
    
    @property
    def booking_rate(self):
        return round((self.booked_seats / self.total_seats) * 100, 1)
    def book(self, tickets):
        if tickets <= 0:
            raise ValueError("Number of tickets must be positive")
        if tickets > self.open_seats:
            raise ValueError("Not enough open seats")
        self.booked_seats += tickets

    def cancel(self, tickets):
        if tickets <= 0:
            raise ValueError("Number of tickets must be positive")
        if tickets > self.booked_seats:
            raise ValueError("Cannot cancel more than booked")
        self.booked_seats -= tickets

f = Flight("UZ-101", 180)
print(f.flight_number, f.open_seats, f.booking_rate)

f.book(120)
print(f.booked_seats, f.booking_rate)

f.cancel(30)
print(f.open_seats)

try:
    f.book(100)
except ValueError as e:
    print(e)

try:
    f.flight_number = "X"
except AttributeError:
    print("Cannot change flight number")
    
        


