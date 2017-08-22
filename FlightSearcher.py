import urllib.request
import json

API_KEY = "<your API Key>"

def main():
    ### origin & destination -> use IATA code
    ### dates use String in the format of yyyy-mm-dd
    ### pass in two date for round trip results
    origin = input("Origin? ")
    destination = input("Destination? ")
    round_trip = input("Round trip (Y/N)? ")
    departing_year = input("Outbounding year? ")
    departing_month = parse_input(input("Outbounding month? "))
    departing_day = parse_input(input("Outbounding day? "))

    departure_date = str(departing_year) + "-" + str(departing_month) + "-" + str(departing_day)
    returning_date = None

    if round_trip == "Y":
        returning_year = input("Inbounding year? ")
        returning_month = parse_input(input("Inbounding month? "))
        returning_day = parse_input(input("Inbounding day? "))
        returning_date = str(returning_year) + "-" + str(returning_month) + "-" + str(returning_day)
        search_flight(origin, destination, 1, departure_date, returning_date)
    else:
        search_flight(origin, destination, 1, departure_date)

def parse_input(input_string: str):
    if len(input_string) < 2:
        return "0" + input_string
    return input_string

def search_flight(origin: str, destination: str, num: int, departure_date: str, return_date=None):
    request_string = "http://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?"
    origin_string = "origin=" + origin + "&"
    destination_string = "destination=" + destination + "&"
    d_date = "departure_date=" + departure_date + "&"
    r_date = ""
    if return_date is not None:
        r_date = "return_date=" + return_date + "&"
    result_num = "number_of_results=" + str(num) + "&"

    request_string = request_string + origin_string + destination_string + d_date + r_date + result_num + "apikey=" + API_KEY
    print(request_string)
    req = urllib.request.Request(request_string)
    file = urllib.request.urlopen(req)
    json_data = json.loads(file.read())
    if return_date is None:
        print_result(json_data, origin, destination, "One Way")
    else:
        print_result(json_data, origin, destination, "Round Trip")

def print_result(data: dict, origin: str, dest: str, trip_type: str):
    result = data["results"]
    print("Your trip is " + trip_type + " from " + origin + " to " + dest + "\n")
    print("----Cheapest Flight Found----")
    print("Price: " + result[0]["fare"]["total_price"])

    print("Outbound:")
    for flight in result[0]["itineraries"][0]["outbound"]["flights"]:
        flight_info = flight["marketing_airline"] + " " + flight["flight_number"]
        flight_detail = " [" + flight["origin"]["airport"] +"-" + flight["destination"]["airport"] + "]"
        print("\t" + flight_info + flight_detail + "\n")

    if trip_type == "Round Trip":
        print("Inbound:")
        for flight in result[0]["itineraries"][0]["inbound"]["flights"]:
            flight_info = flight["marketing_airline"] + " " + flight["flight_number"]
            # flight_dtime = "<" + flight[""]
            flight_detail = " [" + flight["origin"]["airport"] +"-" + flight["destination"]["airport"] + "]"
            print("\t" + flight_info + flight_detail + "\n")

if __name__ == '__main__':
    main()
