from nose.tools import eq_
import unittest

from turn_ticket import TicketDispenser, TurnNumberSequence


class SequenceInterfaceTests(object):
    def __init__(self, sequence):
        self.sequence = sequence

    def test_implements_next_turn_number(self):
        eq_(True, callable(getattr(self.sequence, 'next_turn_number')))


class TurnNumberSequenceTests(unittest.TestCase, SequenceInterfaceTests):
    def setUp(self):
        self.sequence = TurnNumberSequence()


class TicketDispenserTests(unittest.TestCase, SequenceInterfaceTests):

    def setUp(self):
        self.sequence = TurnNumberSequence()
        self.dispenser1 = TicketDispenser(self.sequence)
        self.dispenser2 = TicketDispenser(self.sequence)
        TurnNumberSequence._turnNumber = -1

    def test_first_customer_should_get_ticket_number_zero(self):
        eq_(0, self.dispenser1.getTurnTicket().turnNumber)

    def test_second_customer_should_get_number_one(self):
        self.dispenser1.getTurnTicket().turnNumber
        eq_(1, self.dispenser1.getTurnTicket().turnNumber)

    def test_dispensers_shouuld_not_return_same_number(self):
        turn_number1 = self.dispenser1.getTurnTicket().turnNumber
        turn_number2 = self.dispenser2.getTurnTicket().turnNumber
        self.assertNotEqual(turn_number1, turn_number2)
