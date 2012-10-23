from abc import ABCMeta, abstractmethod, abstractproperty


class TurnTicket(object):
    def __init__(self, turnNumber):
        self.turnNumber = turnNumber


class NumberSequenceGenerator(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def next_turn_number(self):
        raise NotImplementedError("Should implement next_turn_number()!")

    @abstractproperty
    def turn_number(self):
        raise NotImplementedError("Should implement turn_number()!")

class TurnNumberSequence(NumberSequenceGenerator):
    _turnNumber = -1

    def next_turn_number(self):
        TurnNumberSequence._turnNumber += 1
        return self.turn_number

    @property
    def turn_number(self):
        return TurnNumberSequence._turnNumber


class TicketDispenser(object):

    def __init__(self, sequence_generator):
        self.sequence_generator = sequence_generator

    def getTurnTicket(self):
        newTurnNumber = self.sequence_generator.next_turn_number()
        newTurnTicket = TurnTicket(newTurnNumber)
        return newTurnTicket
