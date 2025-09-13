'''
Xiyu Fan
CS 5001
Final Project

This is the data fetching file of the parks and facilities program's Model.
'''
import requests
SUCCESS_RESPONSE_CODE = 200
FILE_NOT_FOUND_CODE = 404
INDEX_ONE = 1
INDEX_TWO = 2
INDEX_THREE = 3
INDEX_ELEVEN = 11
INDEX_THIRTEEN = 13
INDEX_FORTEEN = 14
PARKS_CSV_LINK = 'https://opendata.vancouver.ca/api/explore/v2.1/catalog/'\
        'datasets/parks/exports/csv?lang=en&timezone=America%2FLos_Angeles&'\
        'use_labels=true&delimiter=%3B'
FACILITIES_CSV_LINK = 'https://opendata.vancouver.ca/api/explore/v2.1/'\
        'catalog/datasets/parks-facilities/exports/csv?lang=en&timezone='\
        'America%2FLos_Angeles&use_labels=true&delimiter=%3B'


def get_parks_csv():
    '''
    Purpose:
        To fetch data from a URL.
    Parameters:
        Nothing
    Returns:
        parks_text(str): the text of the parks data.
    Raises:
        ConnectionError: If unable to connect to the URL.
        HTTPError: If the HTTP request returns an unsuccessful response
        status code.
    '''
    parks_response = requests.get(PARKS_CSV_LINK)
    if parks_response.status_code == SUCCESS_RESPONSE_CODE:
        parks_text = parks_response.text
        return parks_text
    else:
        if parks_response.status_code == FILE_NOT_FOUND_CODE:
            raise FileNotFoundError("The URL does not exist.")
        else:
            raise requests.exceptions.HTTPError(
                "HTTP request returned an unsuccessful response status code.")


def get_needed_park_data(parks):
    '''
    Purpose:
        Get needed data from the parks data.

    Parameters:
        parks_text(string): '1;Arbutus Village Park;1;N;N;Y;N;4202...'
    Returns:
        parks_list(list): [['Arbutus Village Park',... ]]
    Raises:
        Nothing.
    '''
    parks_list = []
    parks_text_list = parks.split('\r\n')
    for park_text in parks_text_list[INDEX_ONE:]:
        if park_text:
            park_data_list = park_text.split(';')
            park_name = park_data_list[INDEX_ONE]
            neighbourhood_name = park_data_list[INDEX_ELEVEN]
            hectare = park_data_list[INDEX_THIRTEEN]
            location = park_data_list[INDEX_FORTEEN]
            parks_list.append([park_name, neighbourhood_name, hectare,
                               location])
    return parks_list


def get_facilities_csv():
    '''
    Purpose:
        To fetch the facility data from a URL.
    Parameters:
        Nothing.
    Returns:
        facilities_text(str): the text of facility data from a csv file.
    Raises:
        ConnectionError: If unable to connect to the URL.
        HTTPError: If the HTTP request returns an unsuccessful response
        status code.
    '''
    facilities_response = requests.get(FACILITIES_CSV_LINK)
    if facilities_response.status_code == SUCCESS_RESPONSE_CODE:
        facilities_text = facilities_response.text
        return facilities_text
    else:
        if facilities_response.status_code == FILE_NOT_FOUND_CODE:
            raise FileNotFoundError("The URL does not exist.")
        else:
            raise requests.exceptions.HTTPError(
                "HTTP request returned an unsuccessful response status code.")


def get_needed_facility_data(facility):
    '''
    Purpose:
        To get a list of needed facility data.
    Parameters:
        facility(text): the text of facility data from a csv file.
    Returns:
        facility_list(list): a list of facility data strings.
    Raises:
        Nothing.
    '''
    facility_list = []
    facility_text_list = facility.split('\r\n')
    for facility_text in facility_text_list[INDEX_ONE:]:
        if facility_text:
            facility_data_list = facility_text.split(';')
            park_name = facility_data_list[INDEX_ONE]
            facility_type = facility_data_list[INDEX_TWO]
            facility_count = facility_data_list[INDEX_THREE]
            facility_list.append([park_name, facility_type, facility_count])
    return facility_list
