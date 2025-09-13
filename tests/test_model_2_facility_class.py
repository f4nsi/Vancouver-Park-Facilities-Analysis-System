'''
Xiyu Fan
CS 5001
Final Project

This is the test file for the Facility class of the parks and facilities
program.
'''
import unittest
from models.model_2_facility_class import Facility


class TestFacility(unittest.TestCase):
    def setUp(self):
        self.facility = Facility('Central Park', 'Playgrounds', '5')

    def test_initialization(self):
        self.assertEqual(self.facility.park_name, 'Central Park')
        self.assertEqual(self.facility.type, 'Playgrounds')
        self.assertEqual(self.facility.count, 5)

    def test_increase_facility_count(self):
        self.facility.increase_facility_count('3')
        self.assertEqual(self.facility.count, 8)

    def test_reduce_facility_count(self):
        self.facility.reduce_facility_count('2')
        self.assertEqual(self.facility.count, 3)

    def test_is_type_same(self):
        self.assertFalse(self.facility.is_type("Restrooms"))

    def test_is_type_different(self):
        self.assertTrue(self.facility.is_type("Playgrounds"))

    def test_is_type_none(self):
        self.assertTrue(self.facility.is_type())

    def test_is_count_valid(self):
        self.assertTrue(self.facility.is_count('3'))

    def test_is_count_same(self):
        self.assertTrue(self.facility.is_count('5'))

    def test_is_count_invalid(self):
        self.assertFalse(self.facility.is_count('6'))

    def test_is_count_negative(self):
        self.assertFalse(self.facility.is_count('-1'))

    def test_is_count_none(self):
        self.assertTrue(self.facility.is_count())

    def test_init_count_zero(self):
        with self.assertRaises(ValueError) as e:
            self.facility = Facility('Central Park', 'Playgrounds', '0')
        self.assertEqual(str(e.exception), 'The count must be positive.')

    def test_increase_facility_count_negative(self):
        with self.assertRaises(ValueError) as e:
            self.facility.increase_facility_count('-3')
        self.assertEqual(str(e.exception),
                         'The increase facility count must be positive.')

    def test_increase_facility_count_non_integer(self):
        with self.assertRaises(ValueError) as e:
            self.facility.increase_facility_count('3.5')
        self.assertEqual(str(e.exception),
                         'The increase facility count must be an integer')

    def test_reduce_facility_count_negative(self):
        with self.assertRaises(ValueError) as e:
            self.facility.reduce_facility_count('-2')
        self.assertEqual(str(e.exception),
                         'The reduction facility count must be positive.')

    def test_reduce_facility_count_greater_than_original(self):
        with self.assertRaises(ValueError) as e:
            self.facility.reduce_facility_count('10')
        self.assertEqual(str(e.exception),
                         'The reduction facility count must be smaller'
                         'than the original count.')
