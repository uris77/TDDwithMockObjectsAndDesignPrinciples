import unittest
from nose.tools import eq_

from mock import Mock

from tire_pressure_monitoring import Alarm


class AlarmTests(unittest.TestCase):

    def setUp(self):
        self.sensor = Mock()
        self.alarm = Alarm(self.sensor)

    def test_turn_alarm_on_when_sensor_is_over_high_threshold(self):
        self.sensor.pressure_psi_value.return_value = 100
        self.alarm.check()
        self.sensor.pressure_psi_value.assert_called_once_with()
        eq_(True, self.alarm.is_alarm_on())

    def test_alarm_should_be_off_when_sensor_is_above_low_threshold_but_below_high_threshold(self):
        self.sensor.pressure_psi_value.return_value = 18
        self.alarm.check()
        self.sensor.pressure_psi_value.assert_called_once_with()
        eq_(False, self.alarm.is_alarm_on())

    def test_turn_alarm_on_when_sensor_is_below_low_threshold(self):
        self.sensor.pressure_psi_value.return_value = 10
        self.alarm.check()
        self.sensor.pressure_psi_value.assert_called_once_with()
        eq_(True, self.alarm.is_alarm_on())

    def test_alarm_should_stay_on_after_pressure_returns_to_normal(self):
        self.sensor.pressure_psi_value.return_value = 10
        self.alarm.check()
        self.sensor.pressure_psi_value.return_value = 19
        self.alarm.check()
        eq_(True, self.alarm.is_alarm_on())
