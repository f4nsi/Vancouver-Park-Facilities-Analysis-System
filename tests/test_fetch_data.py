'''
Xiyu Fan
CS 5001
Final Project

This is a unit test file for the fetch data file of the
parks and facilities program.
'''
from models.model_1_park_class import Park
from models.model_2_facility_class import Facility
import unittest
from unittest.mock import patch, Mock
from models.fetch_data import (
    get_parks_csv, get_facilities_csv, get_needed_park_data,
    create_park_instances, get_needed_facility_data,
    create_facility_instances, remove_invalid_park_instances,
    FILE_NOT_FOUND_CODE, SUCCESS_RESPONSE_CODE, ZERO, INDEX_ONE)
from requests.exceptions import HTTPError


class TestFetchData(unittest.TestCase):
    @patch('models.fetch_data.requests.get')
    def test_get_parks_csv_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = SUCCESS_RESPONSE_CODE
        mock_response.text = "Mock parks data"
        mock_get.return_value = mock_response

        result = get_parks_csv()

        self.assertEqual(result, "Mock parks data")

    @patch('models.fetch_data.requests.get')
    def test_get_parks_csv_file_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = FILE_NOT_FOUND_CODE
        mock_get.return_value = mock_response

        with self.assertRaises(FileNotFoundError) as e:
            get_parks_csv()
        self.assertEqual(str(e.exception), 'The URL does not exist.')

    @patch('models.fetch_data.requests.get')
    def test_get_parks_csv_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(HTTPError) as e:
            get_parks_csv()
        self.assertEqual(
            str(e.exception),
            'HTTP request returned an unsuccessful response status code.')

    @patch('models.fetch_data.requests.get')
    def test_get_facilities_csv_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = SUCCESS_RESPONSE_CODE
        mock_response.text = "Mock facilities data"
        mock_get.return_value = mock_response

        result = get_facilities_csv()

        self.assertEqual(result, "Mock facilities data")

    @patch('models.fetch_data.requests.get')
    def test_get_facilities_csv_file_not_found(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = FILE_NOT_FOUND_CODE
        mock_get.return_value = mock_response

        with self.assertRaises(FileNotFoundError) as e:
            get_facilities_csv()
        self.assertEqual(str(e.exception), 'The URL does not exist.')

    @patch('models.fetch_data.requests.get')
    def test_get_facilities_csv_http_error(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(HTTPError) as e:
            get_facilities_csv()
        self.assertEqual(
            str(e.exception),
            'HTTP request returned an unsuccessful response status code.')

    def test_get_needed_park_data(self):
        parks_text = "ParkID;Name;Official;Advisories;SpecialFeatures;Facili"
        "ties;Washrooms;StreetNumber;StreetName;EWStreet;NSStreet;Neighbourho"
        "odName;NeighbourhoodURL;Hectare;GoogleMapDest\r\n1;Arbutus Village "
        "Park;1;N;N;Y;N;4202;Valley Drive;"
        "King Edward Avenue;Valley Drive;Arbutus-Ridge;https://vancouver"
        ".ca/news-calendar/arbutus-ridge.aspx;1.41;49.249783, -123.15525\r\n"
        "4;Park Site on Puget Drive;0;N;N;N;N;4309;Puget Drive;Puget Drive;"
        "MacDonald Street;Arbutus-Ridge;https://vancouver.ca/news-calendar/"
        "arbutus-ridge.aspx;0.09;49.247723, -123.168194"
        expected_result = [
            ['Arbutus Village Park', 'Arbutus-Ridge', '1.41', '49.249783,\
             -123.15525'],
            ['Park Site on Puget Drive', 'Arbutus-Ridge', '0.09',
             '49.247723, -123.168194']]
        result = get_needed_park_data(parks_text)
        self.assertEqual(result, expected_result)

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

    def test_get_needed_facility_data(self):
        facility_text = ("ParkID;Name;FacilityType;FacilityCount;FacilityURL"
                         "\r\n"
                         "2;Carnarvon Park;Softball;2;\r\n"
                         "14;Coopers' Park;Basketball Courts;1;")
        expected_result = [
            ['Carnarvon Park', 'Softball', '2'],
            ["Coopers' Park", 'Basketball Courts', '1']
        ]
        result = get_needed_facility_data(facility_text)
        self.assertEqual(result, expected_result)

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
