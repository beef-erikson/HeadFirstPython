from pprint import pprint
from datetime import datetime

"""CSV manipulation - Creates two dictionaries, one to retain the
   format of the CSV file and a second to improve readability.
"""


def convert_to_ampm(time24: str) -> str:
    """Returns AM/PM from military time
    """
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M %p')


# Custom csv reader, converts to dict
with open('buzzers.csv') as data:
    # ignore header
    ignore = data.readline()

    # writes data to new dict, stripping and splitting
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint(flights)
print('--------')


# Creates new dict and stores converted time and title-cased values
flights2 = {convert_to_ampm(k): v.title() for k, v in flights.items()}

pprint(flights2)
print('--------')


# Creates new dict of key being the destination and value being a list of
# times specific to that destination
flights3 = {destination: [k for k, v in flights2.items() if v == destination]
            for destination in set(flights2.values())}

pprint(flights3)
