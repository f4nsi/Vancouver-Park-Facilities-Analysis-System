'''
Xiyu Fan
CS 5001
Final Project

This is a unit test file for the Park class of the parks and facilities
program.
'''
import unittest
from models.model_1_park_class import Park


class TestPark(unittest.TestCase):
    def setUp(self):
        self.park = Park('Central Park', 'Downtown', '10.5', '49.25, -123.17')

    def test_initialization(self):
        self.assertEqual(self.park.name, 'Central Park')
        self.assertEqual(self.park.neighbourhood_name, 'Downtown')
        self.assertEqual(self.park.hectare, 10.5)
        self.assertEqual(self.park.latitude, 49.25)
        self.assertEqual(self.park.longitude, -123.17)

    def test_expand_area(self):
        self.park.expand_area('5.5')
        self.assertEqual(self.park.hectare, 16.0)

    def test_reduce_area(self):
        self.park.reduce_area('2.5')
        self.assertEqual(self.park.hectare, 8.0)

    def test_is_neighbourhood_same(self):
        self.assertTrue(self.park.is_neighbourhood("Downtown"))

    def test_is_neighbourhood_none(self):
        self.assertTrue(self.park.is_neighbourhood())

    def test_is_neighbourhood_different(self):
        self.assertFalse(self.park.is_neighbourhood("West End"))

    def test_init_hectare_negative(self):
        with self.assertRaises(ValueError) as error:
            self.park = Park(
                'Central Park', 'Downtown', '-1', '49.25, -123.17')
        self.assertEqual(str(error.exception),
                         'The hectare must not be negative.')

    def test_expand_area_negative(self):
        with self.assertRaises(ValueError) as error:
            self.park.expand_area('-5.5')
        self.assertEqual(str(error.exception),
                         'The expansion area must be positive.')

    def test_expand_area_zero(self):
        with self.assertRaises(ValueError) as error:
            self.park.expand_area('0')
        self.assertEqual(str(error.exception),
                         'The expansion area must be positive.')

    def test_reduce_area_negative(self):
        with self.assertRaises(ValueError) as error:
            self.park.reduce_area('-2.5')
        self.assertEqual(str(error.exception),
                         'The reduction area must be positive.')

    def test_reduce_area_zero(self):
        with self.assertRaises(ValueError) as error:
            self.park.reduce_area('0')
        self.assertEqual(str(error.exception),
                         'The reduction area must be positive.')

    def test_reduce_area_greater_than_original(self):
        with self.assertRaises(ValueError) as error:
            self.park.reduce_area('15')
        self.assertEqual(str(error.exception),
                         'The reduction area must be smaller than the'
                         'original area')
