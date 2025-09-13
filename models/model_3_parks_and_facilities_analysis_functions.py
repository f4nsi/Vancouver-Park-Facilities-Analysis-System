'''
Xiyu Fan
CS 5001
Final Project

This is the data analysing file of the parks and facilities program's Model.
'''
from models.model_2_facility_class import Facility
ZERO = 0
ONE = 1


def create_park_facility_dictionary(facility_instances):
    '''
    Purpose:
        To create a dictionary whose keys are park names and values are
        facility types and counts.
    Sample:
        {'Park1': [[Pool, 1], [Playground, 2]]}
    Parameters:
        facility_instances(list): a list of park facility objects.
    Returns:
        park_facility_dictionary(dic): dictionary whose keys are park names
        and values are facility types and counts.
    Raises:
        Nothing.
    '''
    park_facility_dictionary = {}
    for instance in facility_instances:
        if instance.park_name not in park_facility_dictionary:
            park_facility_dictionary[instance.park_name] = []
        facility_type_count_list = [instance.type, instance.count]
        park_facility_dictionary[instance.park_name].append(
            facility_type_count_list)
    return park_facility_dictionary


def create_neighbourhood_facility_dictionary(
        park_instances, facility_instances):
    '''
    Purpose:
        To create a dictionary whose keys are neighbourhood names and values
        are dictionarys with facility types as keys and lists of facility
        types and distribution as values.
    Parameters:
        park_instances(list): a list of park objects.
        facility_instances(list): a list of park facility objects.
    Returns:
        neighbourhood_facility_dictionary(dic): a dictionary whose keys are
        neighbourhood names and values are dictionarys with facility types
        as keys and lists of facility types and distribution as values.
    Raises:
        Nothing.
    '''
    new_dictionary = {}

    for facility in facility_instances:
        for park in park_instances:
            if facility.park_name == park.name:
                # Set keys and values
                if park.neighbourhood_name not in new_dictionary:
                    new_dictionary[park.neighbourhood_name] = {}
                # Add facility count to value representing the facility details
                if facility.type not in new_dictionary[
                        park.neighbourhood_name]:
                    new_dictionary[park.neighbourhood_name][facility.type] = [
                        facility.count]
                else:
                    new_dictionary[park.neighbourhood_name][
                        facility.type][0] += facility.count

    # Calculate the distribution
    for value in new_dictionary.values():
        total_number = sum(value_list[0] for value_list in value.values())
        for value_list in value.values():
            distribution = round(value_list[0] / total_number, 4)
            value_list.append(distribution)
    return new_dictionary


def expand_the_park_area(name, expanded_area,
                         park_instances):
    '''
    Purpose:
        To expand the area of a park.
    Parameters:
        name(str): a park's name.
        expanded_area(str): the expanded area of the park.
        park_instances(list): a list of park objects.
    Returns:
        park_instances(list): a list of park objects.
    Raises:
        Nothing.
    '''
    # Search the park in the park list.
    # Find the park successfully
    found = False
    for instance in park_instances:
        if instance.name == name:
            instance.expand_area(expanded_area)
            print(f'The area of {name} has been expanded successfully!\n')
            found = True
    # Can't find the park
    if found is False:
        print(f"{name} can't be found.\n")
    return park_instances


def reduce_the_park_area(name, reduced_area, park_instances):
    '''
    Purpose:
        To reduce the area of a park.
    Parameters:
        park_instances(list): a list of park objects.
        name(str): a park's name.
        reduced_area(str): the reduced area of the park.
    Returns:
        park_instances(list): a list of park objects.
    Raises:
        Nothing.
    '''
    # Search the park in the park list.
    # Find the park successfully
    found = False
    for instance in park_instances:
        if instance.name == name:
            instance.reduce_area(reduced_area)
            print(f'The area of {name} has been reduced successfully!\n')
            found = True
    # Can't find the park
    if found is False:
        print(f"{name} can't be found.\n")
    return park_instances


def add_a_new_facility(park_name, type, count,
                       park_instances, facility_instances):
    '''
    Purpose:
        To add a new park facility into the facility list.
    Parameters:
        park_name(str): represents a park's name.
        type(str): represents a park facility's type.
        count(str): represents a park facility's count.
        park_instances(list): a list of park objects.
        facility_instances(list): a list of park facility objects.
    Returns:
        facility_instances(list): a list of park facility objects.
    Raises:
        Nothing.
    '''
    # Check whether the park is in the park list
    park_found = False
    for park_instance in park_instances:
        if park_instance.name == park_name:
            new_facility = Facility(park_name, type, count)
            facility_instances.append(new_facility)
            print(f'{count} {type} has been successfully added in'
                  f' {park_name}!\n')
            park_found = True
    if park_found is False:
        print(f'{park_name} does not exist.')
    return facility_instances


def delete_a_facility(name, facility_type, facility_instances):
    '''
    Purpose:
        To delete a park facility from the facility list.
    Parameters:
        name(str): represents a park's name.
        facility_type(str): represents a park facility's type.
        facility_instances(list): a list of park facility objects.
    Returns:
        facility_instances(list): a list of park facility objects.
    Raises:
        Nothing.
    '''
    # Search the park facility in the facility list.
    # Find the park facility successfully
    park_found = False
    facility_found = False
    for instance in facility_instances:
        if instance.park_name == name:
            park_found = True
            if instance.type == facility_type:
                facility_instances.remove(instance)
                print(f"{facility_type} has been deleted from {name}"
                      f" successfully!\n")
                facility_found = True
    # Can't find the park facility
    if park_found is False:
        print(f"{name} can't be found.\n")
    if facility_found is False:
        print(f"{facility_type} can't be found in {name}.\n")
    return facility_instances


def increase_a_facility_number(
        name, facility_type, facility_count, facility_instances):
    '''
    Purpose:
        To increase a facility number in the facility list.
    Parameters:
        name(str): represents a park's name.
        facility_type(str): represents a park facility's type.
        facility_count(str): represents the increased count.
        facility_instances(list): a list of park facility objects.
    Returns:
        facility_instances(list): a list of park facility objects.
    Raises:
        Nothing.
    '''
    # Search the park facility in the facility list.
    # Find the park facility successfully
    park_found = False
    facility_found = False
    for instance in facility_instances:
        if instance.park_name == name:
            park_found = True
            if instance.type == facility_type:
                instance.increase_facility_count(facility_count)
                print(f"{facility_count} {facility_type} has"
                      f" been added to {name} successfully!\n")
                facility_found = True
    # Can't find the park facility
    if park_found is False:
        print(f"{name} can't be found.")
    if facility_found is False:
        print(f"{facility_type} can't be found in {name}.\n")
    return facility_instances


def reduce_a_facility_number(
        name, facility_type, facility_count, facility_instances):
    '''
    Purpose:
        To reduce a facility number in the facility list.
    Parameters:
        name(str): represents a park's name.
        facility_type(str): represents a park facility's type.
        facility_count(str): represents the reduced count.
        facility_instances(list): a list of park facility objects.
    Returns:
        facility_instances(list): a list of park facility objects.
    Raises:
        Nothing.
    '''
    # Search the park facility in the facility list.
    # Find the park facility successfully
    park_found = False
    facility_found = False
    for instance in facility_instances:
        if instance.park_name == name:
            park_found = True
            if instance.type == facility_type:
                instance.reduce_facility_count(facility_count)
                print(f"{facility_count} {facility_type} has"
                      f" been reduced from {name} successfully!\n")
                facility_found = True
    # Can't find the park facility
    if park_found is False:
        print(f"{name} can't be found.")
    if facility_found is False:
        print(f"{facility_type} can't be found in {name}.\n")
    return facility_instances


def filter_parks(park_instances, facility_instances,
                 required_facility=None, required_neighbourhood=None):
    '''
    Purpose:
        To filter parks by facility type, facility count, and neighbourhood.
    Parameters:
        park_instances(list): a list of park objects.
        facility_instances(list): a list of park facility objects.
        required_facility(list): a list of required facility's type and count.
        required_neighbourhood(str): a string of neighbourhood name.
    Returns:
        filtered_parks(list):  a list of park objects meeting the user's
        requirements.
    Raises:
        Nothing.
    '''
    filtered_parks = []

    if required_facility:
        for facility in facility_instances:
            if facility.is_type(required_facility[ZERO]) and \
                    facility.is_count(required_facility[ONE]):
                for park in park_instances:
                    if facility.park_name == park.name and \
                            park.is_neighbourhood(required_neighbourhood):
                        filtered_parks.append(park)
    else:
        for park in park_instances:
            if park.is_neighbourhood(required_neighbourhood):
                filtered_parks.append(park)
    return filtered_parks
