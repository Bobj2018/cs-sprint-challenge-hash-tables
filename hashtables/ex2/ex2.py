class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hash_tickets = {}
    route = [None] * length

    for ticket in tickets:
        hash_tickets[ticket.source] = ticket.destination

    curr_destination = hash_tickets["NONE"]

    for i in range(length):
        route[i] = curr_destination
        curr_destination = hash_tickets[curr_destination]

    return route
