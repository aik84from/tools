import device
import unittest


class TestFunctions(unittest.TestCase):

    def test_resistive_divider(self):
        self.assertTrue(device.is_error_acceptable(device.resistive_divider(5.0, 100.0, 100.0), 2.5, 0.0001))

    def test_power(self):
        self.assertTrue(device.is_error_acceptable(device.power(5.0, 2.0), 10.0, 0.0001))

    def test_current_from_voltage_resistance(self):
        self.assertTrue(device.is_error_acceptable(device.current_from_voltage_resistance(5.0, 10.0), 0.5, 0.0001))

    def test_current_from_voltage_power(self):
        self.assertTrue(device.is_error_acceptable(device.current_from_voltage_power(5.0, 10.0), 2.0, 0.0001))

    def test_and_gate(self):
        self.assertTrue(device.is_error_acceptable(device.and_gate(1.0, 1.0), 1.0, 0.0001))
        self.assertTrue(device.is_error_acceptable(device.and_gate(1.0, 0.0), 0.0, 0.0001))

    def test_or_gate(self):
        self.assertTrue(device.is_error_acceptable(device.or_gate(1.0, 1.0), 1.0, 0.0001))
        self.assertTrue(device.is_error_acceptable(device.or_gate(0.0, 0.0), 0.0, 0.0001))

    def test_not_gate(self):
        self.assertTrue(device.is_error_acceptable(device.not_gate(1.0), 0.0, 0.0001))
        self.assertTrue(device.is_error_acceptable(device.not_gate(0.0), 1.0, 0.0001))

    def test_nand_gate(self):
        self.assertTrue(device.is_error_acceptable(device.nand_gate(1.0, 1.0), 0.0, 0.0001))
        self.assertTrue(device.is_error_acceptable(device.nand_gate(0.0, 0.0), 1.0, 0.0001))

    def test_nor_gate(self):
        self.assertTrue(device.is_error_acceptable(device.nor_gate(1.0, 1.0), 0.0, 0.0001))
        self.assertTrue(device.is_error_acceptable(device.nor_gate(0.0, 0.0), 1.0, 0.0001))

    def test_euclidean_distance(self):
        self.assertTrue(device.is_error_acceptable(device.euclidean_distance([1.1, 12.54], [24.87, 16.57]), 24.10920571068238, 0.0001))

    def test_kinetic_energy(self):
        self.assertTrue(device.is_error_acceptable(device.kinetic_energy(2.0, 3.0), 9.0, 0.0001))

    def test_is_error_acceptable(self):
        self.assertTrue(device.is_error_acceptable(2.5, 2.0, 0.6))
        self.assertFalse(device.is_error_acceptable(3.0, 2.0, 0.6))

