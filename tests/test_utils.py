'''
Xiyu Fan
CS 5001
Final Project

This is a unit test file for the utils file of the
parks and facilities program.
'''
from models.model_1_park_class import Park
from models.model_2_facility_class import Facility
import unittest
from utils import (
    remove_invalid_park_instances, create_park_instances,
    create_facility_instances, ZERO, INDEX_ONE)


class TestUtils(unittest.TestCase):
    def test_create_park_instances(self):
        park_data = [
            ['Arbutus Village Park', 'Arbutus-Ridge', '1.41', '49.249783,\
             -123.15525'],
            ['Park Site on Puget Drive', 'Arbutus-Ridge', '0.09',
             '49.247723, -123.168194']]
        expected_result = [Park('Arbutus Village Park', 'Arbutus-Ridge',
                                '1.41', '49.249783,-123.15525'),
                           Park('Park Site on Puget Drive',
                                'Arbutus-Ridge', '0.09',
                                '49.247723, -123.168194')]
        result = create_park_instances(park_data)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected_result[i].name)
            self.assertEqual(result[i].neighbourhood_name,
                             expected_result[i].neighbourhood_name)
            self.assertEqual(result[i].hectare, expected_result[i].hectare)
            self.assertEqual(result[i].latitude, expected_result[i].latitude)
            self.assertEqual(result[i].longitude, expected_result[i].longitude)

    def test_create_facility_instances(self):
        facility_data = [['Central Park', 'Restroom', '5'],
                         ['Central Park', 'Playground', '2'],
                         ['Another Park', 'Restroom', '3']]
        expected_result = [Facility('Central Park', 'Restroom', 5),
                           Facility('Central Park', 'Playground', 2),
                           Facility('Another Park', 'Restroom', 3)]
        result = create_facility_instances(facility_data)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_remove_invalid_park_instances(self):
        # Create valid park and facility instances
        valid_park_instances = [
            Park('Park1', 'Neighbourhood1', '5', '49.249783,-123.15525'),
            Park('Park2', 'Neighbourhood2', '0', '49.247723, -123.168194')]
        valid_facility_instances = [
            Facility('Park1', 'FacilityType1', 3),
            Facility('Park1', 'FacilityType2', 2),
            Facility('Park2', 'FacilityType1', 1)]

        # Remove invalid park instances
        result_parks, result_facilities = remove_invalid_park_instances(
            valid_park_instances, valid_facility_instances)

        # Check if the invalid park and corresponding facility instances
        # are removed
        self.assertEqual(len(result_parks), 1)
        self.assertEqual(result_parks[ZERO].name, 'Park1')
        self.assertEqual(len(result_facilities), 2)
        self.assertEqual(result_facilities[ZERO].park_name, 'Park1')
        self.assertEqual(result_facilities[INDEX_ONE].park_name, 'Park1')
