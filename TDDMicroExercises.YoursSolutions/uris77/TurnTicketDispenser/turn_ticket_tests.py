from nose.tools import eq_
import unittest

from turn_ticket import TicketDispenser, TurnNumberSequence


class TicketDispenserTests(unittest.TestCase):

    def setUp(self):
        self.dispenser1 = TicketDispenser()
        self.dispenser2 = TicketDispenser()
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
