class Flight:
    def __init__(self, flight_id, source, destination, price):
        self.flight_id = flight_id
        self.source = source
        self.destination = destination
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []
        self.populate_flights()

    def populate_flights(self):
        data = [
            ("AI161E90", "BLR", "BOM", 5600),
            ("BR161F91", "BOM", "BBI", 6750),
            ("AI161F99", "BBI", "BLR", 8210),
            ("VS171E20", "JLR", "BBI", 5500),
            ("AS171G30", "HYD", "JLR", 4400),
            ("AI131F49", "HYD", "BOM", 3499)
        ]

        for item in data:
            flight = Flight(item[0], item[1], item[2], item[3])
            self.flights.append(flight)

    def search_by_city(self, city):
        result = []
        for flight in self.flights:
            if flight.source == city or flight.destination == city:
                result.append(flight)
        return result

    def search_between_cities(self, source, destination):
        result = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination:
                result.append(flight)
        return result

def main():
    flight_table = FlightTable()

    search_input = input("Enter a city or two cities separated by a space: ")
    search_terms = search_input.split()

    if len(search_terms) == 1:
        city = search_terms[0]
        result = flight_table.search_by_city(city)
    elif len(search_terms) == 2:
        source = search_terms[0]
        destination = search_terms[1]
        result = flight_table.search_between_cities(source, destination)
    else:
        print("Invalid input")
        return

    if result:
        print("Flight ID\tFrom\tTo\tPrice")
        for flight in result:
            print(f"{flight.flight_id}\t{flight.source}\t{flight.destination}\t{flight.price}")
    else:
        print("No flights found.")

if __name__ == "__main__":
    main()
