from nose.tools import eq_
import unittest

from turn_ticket import TicketDispenser, TurnNumberSequence


class TicketDispenserTests(unittest.TestCase):

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
        ticket1 = self.dispenser1.getTurnTicket()
        ticket2 = self.dispenser2.getTurnTicket()
        self.assertNotEqual(ticket1.turnNumber, ticket2.turnNumber)
