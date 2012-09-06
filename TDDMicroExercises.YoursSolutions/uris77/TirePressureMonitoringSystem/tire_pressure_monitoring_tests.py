import unittest
from nose.tools import eq_

from mock import Mock

from tire_pressure_monitoring import Alarm


class AlarmTests(unittest.TestCase):

    def setUp(self):
        self.sensor = Mock()
        self.alarm = Alarm(self.sensor)
        self.HIGH_PRESSURE = 100
        self.LOW_PRESSURE = 10
        self.NORMAL_PRESSURE = 19

    def test_turn_alarm_on_when_sensor_is_over_high_threshold(self):
        self.sensor.pressure_psi_value.return_value = self.HIGH_PRESSURE
        self.alarm.check()
        self.sensor.pressure_psi_value.assert_called_once_with()
        self.alarm_should_be_on()

    def test_alarm_should_be_off_when_sensor_is_above_low_threshold_but_below_high_threshold(self):
        self.sensor.pressure_psi_value.return_value = self.NORMAL_PRESSURE
        self.alarm.check()
        self.sensor.pressure_psi_value.assert_called_once_with()
        self.alarm_should_be_off()

    def test_turn_alarm_on_when_sensor_is_below_low_threshold(self):
        self.sensor.pressure_psi_value.return_value = self.LOW_PRESSURE
        self.alarm.check()
        self.sensor.pressure_psi_value.assert_called_once_with()
        self.alarm_should_be_on()

    def test_alarm_should_stay_on_after_pressure_returns_to_normal(self):
        self.sensor.pressure_psi_value.return_value = self.LOW_PRESSURE
        self.alarm.check()
        self.sensor.pressure_psi_value.return_value = self.NORMAL_PRESSURE
        self.alarm.check()
        self.alarm_should_be_on()

    def alarm_should_be_on(self):
        eq_(True, self.alarm.is_alarm_on())

    def alarm_should_be_off(self):
        eq_(False, self.alarm.is_alarm_on())
