'''
Xiyu Fan
CS 5001
Final Project

This is the unit test file for the data analysing file of the parks and
facilities program's Model.
'''
from models.model_1_park_class import Park
from models.model_2_facility_class import Facility
from models.model_3_parks_and_facilities_analysis_functions import \
    (create_park_facility_dictionary, create_neighbourhood_facility_dictionary,
     expand_the_park_area, reduce_the_park_area, add_a_new_facility,
     delete_a_facility, increase_a_facility_number, reduce_a_facility_number,
     filter_parks, ZERO)
import unittest
# python -m unittest tests.test_model_3_parks_and_facilities_analysis_functions


class TestModel3(unittest.TestCase):
    def test_create_park_facility_dictionary(self):
        facility1 = Facility('Park1', 'Facility1', '1')
        facility2 = Facility('Park2', 'Facility2', '2')
        facility3 = Facility('Park1', 'Facility2', '1')
        facility_objects = [facility1, facility2, facility3]
        expected_result = {'Park1': [['Facility1', 1], ['Facility2', 1]],
                           'Park2': [['Facility2', 2]]}
        result = create_park_facility_dictionary(facility_objects)
        self.assertEqual(result, expected_result)

    def test_create_neighbourhood_facility_dictionary(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility3 = Facility('Park3', 'Facility1', '1')
        facility4 = Facility('Park3', 'Facility2', '3')
        facility_instances = [facility1, facility2, facility3, facility4]
        result = create_neighbourhood_facility_dictionary(
            park_instances, facility_instances)
        expected_result = {
            'Neighbourhood1': {'Facility1': [3, 0.75], 'Facility2': [1, 0.25]},
            'Neighbourhood2': {'Facility1': [1, 0.25], 'Facility2': [3, 0.75]}}
        self.assertEqual(result, expected_result)

    def test_expand_the_park_area_found(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]
        result = expand_the_park_area('Park1', '1', park_instances)
        self.assertEqual(result[ZERO].hectare, 2)

    def test_expand_the_park_area_not_found(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        result = [park1, park2, park3]
        expected_result = reduce_the_park_area('Park4', '1', result)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected_result[i].name)
            self.assertEqual(result[i].neighbourhood_name,
                             expected_result[i].neighbourhood_name)
            self.assertEqual(result[i].hectare, expected_result[i].hectare)
            self.assertEqual(result[i].latitude, expected_result[i].latitude)
            self.assertEqual(result[i].longitude, expected_result[i].longitude)

    def test_reduce_the_park_area_found(self):
        park1 = Park('Park1', 'Neighbourhood1', '2', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]
        result = reduce_the_park_area('Park1', '1', park_instances)
        self.assertEqual(result[ZERO].hectare, 1)

    def test_reduce_the_park_area_not_found(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        result = [park1, park2, park3]
        expected_result = reduce_the_park_area('Park4', '1', result)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].name, expected_result[i].name)
            self.assertEqual(result[i].neighbourhood_name,
                             expected_result[i].neighbourhood_name)
            self.assertEqual(result[i].hectare, expected_result[i].hectare)
            self.assertEqual(result[i].latitude, expected_result[i].latitude)
            self.assertEqual(result[i].longitude, expected_result[i].longitude)

    def test_add_a_new_facility_found(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility3 = Facility('Park3', 'Facility1', '1')
        facility_instances = [facility1, facility2]

        result = add_a_new_facility(
            'Park3', 'Facility1', '1', park_instances, facility_instances)
        expected_result = [facility1, facility2, facility3]
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_add_a_new_facility_not_found(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = add_a_new_facility(
            'Park4', 'Facility1', '1', park_instances, facility_instances)
        expected_result = [facility1, facility2]
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_delete_a_facility_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = [facility1]
        expected_result = delete_a_facility('Park2', 'Facility2',
                                            facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_delete_a_facility_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = delete_a_facility('Park3', 'Facility2',
                                            facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_increase_a_facility_number_both_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility2_new = Facility('Park2', 'Facility2', '2')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2_new]
        expected_result = increase_a_facility_number(
            'Park2', 'Facility2', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_increase_a_facility_number_park_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = increase_a_facility_number(
            'Park3', 'Facility2', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_increase_a_facility_number_facility_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = increase_a_facility_number(
            'Park2', 'Facility3', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_increase_a_facility_number_both_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = increase_a_facility_number(
            'Park3', 'Facility3', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_reduce_a_facility_number_both_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '2')
        facility2_new = Facility('Park2', 'Facility2', '1')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2_new]
        expected_result = reduce_a_facility_number(
            'Park2', 'Facility2', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_reduce_a_facility_number_park_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '2')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = reduce_a_facility_number(
            'Park3', 'Facility2', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_reduce_a_facility_number_facility_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '2')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = reduce_a_facility_number(
            'Park2', 'Facility3', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_reduce_a_facility_number_both_not_found(self):
        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '2')
        facility_instances = [facility1, facility2]

        result = [facility1, facility2]
        expected_result = reduce_a_facility_number(
            'Park3', 'Facility3', '1', facility_instances)
        self.assertEqual(len(result), len(expected_result))
        for i in range(len(result)):
            self.assertEqual(result[i].park_name, expected_result[i].park_name)
            self.assertEqual(result[i].type, expected_result[i].type)
            self.assertEqual(result[i].count, expected_result[i].count)

    def test_filter_parks_both_none(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]

        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility3 = Facility('Park3', 'Facility1', '1')
        facility4 = Facility('Park3', 'Facility2', '3')
        facility_instances = [facility1, facility2, facility3, facility4]
        result = filter_parks(park_instances, facility_instances)
        self.assertEqual(len(result), 3)

    def test_filter_parks_only_neighbourhood(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]

        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility3 = Facility('Park3', 'Facility1', '1')
        facility4 = Facility('Park3', 'Facility2', '3')
        facility_instances = [facility1, facility2, facility3, facility4]
        result = filter_parks(park_instances, facility_instances,
                              required_neighbourhood='Neighbourhood1')
        self.assertEqual(len(result), 2)

    def test_filter_parks_facility_and_neighbourhood(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]

        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility3 = Facility('Park3', 'Facility1', '1')
        facility4 = Facility('Park3', 'Facility2', '3')
        facility_instances = [facility1, facility2, facility3, facility4]
        result = filter_parks(
            park_instances, facility_instances,
            required_facility=['Facility1', '3'],
            required_neighbourhood='Neighbourhood1')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Park1')

    def test_filter_parks_only_facility(self):
        park1 = Park('Park1', 'Neighbourhood1', '1', '40, -120')
        park2 = Park('Park2', 'Neighbourhood1', '1', '40, -121')
        park3 = Park('Park3', 'Neighbourhood2', '1', '40, -121.1')
        park_instances = [park1, park2, park3]

        facility1 = Facility('Park1', 'Facility1', '3')
        facility2 = Facility('Park2', 'Facility2', '1')
        facility3 = Facility('Park3', 'Facility1', '1')
        facility4 = Facility('Park3', 'Facility2', '3')
        facility_instances = [facility1, facility2, facility3, facility4]
        result = filter_parks(park_instances, facility_instances,
                              required_facility=['Facility1', '3'])
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, 'Park1')
