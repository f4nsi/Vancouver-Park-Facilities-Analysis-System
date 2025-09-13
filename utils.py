'''
Xiyu Fan
CS 5001
Final Project

This is the utils file of the parks and facilities program's Controller.
It's main functionality is to create objects and clean them.
'''
from models.model_1_park_class import Park
from models.model_2_facility_class import Facility
ZERO = 0
INDEX_ZERO = 0
INDEX_ONE = 1
INDEX_TWO = 2
INDEX_THREE = 3


def create_park_instances(needed_parks_list):
    '''
    To encapsulate park data into instances using the Park class.

    Parameters:
        needed_parks_list(list): a list of needed park data created by
        the get_needed_park_data function above.
    Returns:
        park_instances(list): a list of park instances.
    Raises:
        Nothing.
    '''
    park_instances = []
    for park_data in needed_parks_list:
        name = park_data[INDEX_ZERO]
        neighbourhood_name = park_data[INDEX_ONE]
        hectare = park_data[INDEX_TWO]
        location = park_data[INDEX_THREE]
        park_instance = Park(name, neighbourhood_name, hectare, location)
        park_instances.append(park_instance)
    return park_instances


def create_facility_instances(needed_facilities_list):
    '''
    Purpose:
        To encapsulate the facility data into instances using the Facility
    class.
    Parameters:
        needed_parks_list(list): a list of needed park data created by
        the get_needed_park_data function above.
    Returns:
        park_instances(list): a list of park instances.
    Raises:
        Nothing.
    '''
    facility_instances = []
    for facility_data in needed_facilities_list:
        park_name = facility_data[INDEX_ZERO]
        facility_type = facility_data[INDEX_ONE]
        facility_count = facility_data[INDEX_TWO]
        facility_instance = Facility(park_name, facility_type,
                                     facility_count)
        facility_instances.append(facility_instance)
    return facility_instances


def remove_invalid_park_instances(park_instances, facility_instances):
    '''
    Purpose:
        To remove invalid park instances whose hectare is zero and their
        correspond facility instances.

    Parameters:
        park_instances(list): list of all the park instances.
        facility_instances(list): list of all the facility instances.
    Returns:
        Nothing.
    Raises:
        Nothing
    '''
    for park_instance in park_instances:
        if park_instance.hectare == ZERO:
            for facility_instance in facility_instances:
                if facility_instance.park_name == park_instance.name:
                    facility_instances.remove(facility_instance)
            park_instances.remove(park_instance)
    return park_instances, facility_instances
