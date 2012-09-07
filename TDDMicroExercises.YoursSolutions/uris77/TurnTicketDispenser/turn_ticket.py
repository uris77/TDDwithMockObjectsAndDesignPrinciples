class TurnTicket(object):
    def __init__(self, turnNumber):
        self.turnNumber = turnNumber


class TurnNumberSequence(object):
    _turnNumber = -1

    @staticmethod
    def next_turn_number():
        TurnNumberSequence._turnNumber += 1
        return TurnNumberSequence._turnNumber


class TicketDispenser(object):

    def __init__(self, sequence_generator):
        self.sequence_generator = sequence_generator

    def getTurnTicket(self):
        newTurnNumber = self.sequence_generator.next_turn_number()
        newTurnTicket = TurnTicket(newTurnNumber)
        return newTurnTicket
