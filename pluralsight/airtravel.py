'''Model for aircraft flights.'''

class Flight:
    '''A flight with a particular aircrafts.'''
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError('No airline code in {}'.format(number))
        if not number[:2].isupper():
            raise ValueError('Invalid airline code {}'.format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError('Invalid route number {}'.format(number))
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        '''Number of aircraft.'''
        return self._number

    def airline(self):
        '''Returns airline code.'''
        return self._number[:2]

    def aircraft_model(self):
        '''Returns model of aircraft for this flight.'''
        return self._aircraft.model()

    def parse_seat(self, seat):
        '''Checks if seat is valid.

        Args:
            seat: A seat designator such as "21F".

        Returns:
            row: Row number of the seat.
            letter: Letter os seat.

        Raises:
            ValueError: If the seat is unavailable.
        '''
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError('Invalid seat letter {}'.format(letter))
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError('Invalid seat row {}'.format(row_text))
        if row not in rows:
            raise ValueError('Invalid seat number {}'.format(row_text))

        return row, letter

    def allocate(self, seat, passanger):
        '''Allocate seat to a passanger.

        Args:
            seat: A seat designator such as "21F".
            passanger: The passanger name.

        Raises:
            ValueError: If the seat is unavailable.
        '''
        row, letter = self.parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError('Seat {} already occupied'.format(seat))

        self._seating[row][letter] = passanger

    def num_available_seats(self):
        '''Retrieves number of available seats of the flight.'''
        return sum(
            sum(1 for s in row.values() if s is None)
            for row in self._seating if row is not None)

    def make_boarding_card(self, card_printer):
        '''Prints boarding cards for every passanger.'''
        for passanger, seat in sorted(self._passangers_seats()):
            card_printer(passanger, seat, self.number(), self.aircraft_model())

    def _passangers_seats(self):
        '''An iterable series of passanger seating allocations.'''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passanger = self._seating[row][letter]
                if passanger is not None:
                    yield (passanger, '{}{}'.format(row, letter))

class Aircraft:
    '''Aircraft.'''
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        '''Retrieves a registration of the aircraft.'''
        return self._registration

    def model(self):
        '''Retrieves the aircraft's model.'''
        return self._model

    def seating_plan(self):
        '''Retrieves seat plan of the aircraft.'''
        return (range(1, self._num_rows + 1),
                'ABCDEFGHJK'[:self._num_seats_per_row])

class Boing():
    '''Boing aircraft.'''
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        '''Retrieves registration number.'''
        return self._registration

    def num_of_seats(self):
        '''Retrieves number of seats.'''
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class Boing747(Boing):
    '''Boing 747 aircraft.'''
    def model(self):
        '''Retrieves model.'''
        return 'Boing 747'

    def seating_plan(self):
        '''Retrieves seating plan.'''
        return range(1, 24), 'ABCDEFG'


class Boing767(Boing):
    '''Boing 767 aircraft.'''
    def model(self):
        '''Retrieves model.'''
        return 'Boing 767'

    def seating_plan(self):
        '''Retrieves seating plan.'''
        return range(1, 48), 'ABCDEFGHJ'

def make_flight():
    '''Creates flight and allocates a few passangers.'''
    flight = Flight('AB123', Aircraft('G-EUPT', 'Airbus A319', num_rows=22, num_seats_per_row=6))
    flight.allocate('21A', 'Ben')
    flight.allocate('2A', 'Bob')
    flight.allocate('3F', 'Alan')
    return flight

def console_card_printer(passanger, seat, flight_number, aircraft):
    '''Prints board card to console.'''
    output = "| Name: {0}"     \
             "  Flight: {1}"   \
             "  Seat: {2}"     \
             "  Aircraft: {3}" \
             " |".format(passanger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()
