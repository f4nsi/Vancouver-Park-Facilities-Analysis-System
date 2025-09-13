'''
Xiyu Fan
CS 5001
Final Project

This is the interface file of the parks and facilities program's View.
'''
ZERO = 0
ONE = 1
TWO = 2
HUNDRED = 100
ONE_OR_TWO = ['1', '2']
ONE_TO_THREE = ['1', '2', '3']
ONE_TO_FOUR = ['1', '2', '3', '4']
ONE_TO_FIVE = ['1', '2', '3', '4', '5']
ONE_TO_SIX = ['1', '2', '3', '4', '5', '6', '7']


def display_the_main_menu():
    '''
    Purpose:
        To display the main menu for users to choose.
    Parameters:
        Nothing.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    print('Hi! This is the Parks and Facilities program.\n'
          'What would you like to do?\n\n'
          '1. Manage the parks in Vancouver City\n'
          '2. Manage the park facilities in Vancouver City\n'
          '3. Find parks and facilities on a map\n'
          '4. Analyze the park and facility data\n'
          '5. Quit\n')


def choose_from_the_main_menu():
    '''
    Purpose:
        To ask users to input their choices according to the main menu.
    Parameters:
        Nothing.
    Returns:
        main_menu_option(str): represents the user's option.
    Raises:
        Nothing.
    '''
    main_menu_option = input('Enter your option:')
    if main_menu_option not in ONE_TO_FIVE:
        raise ValueError('You must choose from number 1~5.')
    else:
        return main_menu_option


def display_the_park_menu():
    '''
    Purpose:
        To display the park management menu for users to choose.
    Parameters:
        Nothing.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    print('Now you can manage the parks in Vancouver City.\n'
          'Please choose from the following options.\n\n'
          '1. Increase the area of a park.\n'
          '2. Reduce the area of a park.\n'
          '3. Get details of a park.\n'
          '4. Get details of all park.\n')


def choose_from_the_park_menu():
    '''
    Purpose:
        To ask users to input their choices according to the park menu.
    Parameters:
        Nothing.
    Returns:
        park_menu_option(str): represents the user's option.
    Raises:
        Nothing.
    '''
    park_menu_option = input('Enter your option:')
    if park_menu_option not in ONE_TO_FOUR:
        raise ValueError('You must choose from number 1~4.')
    else:
        return park_menu_option


def display_the_facility_menu():
    '''
    Purpose:
        To display the facility management menu for users to choose.
    Parameters:
        Nothing.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    print('Now you can manage the park facilities in Vancouver City.\n'
          'Please choose from the following options.\n\n'
          '1. Add a new park facility.\n'
          '2. Delete a park facility.\n'
          '3. Increase the facility count of a park.\n'
          '4. Reduce the facility count of a park.\n'
          '5. Get details of a park facility.\n'
          '6. Get details of all park facilities.\n')


def choose_from_the_facility_menu():
    '''
    Purpose:
        To ask users to input their choices according to the facility menu.
    Parameters:
        Nothing.
    Returns:
        facility_menu_option(str): represents the user's option.
    Raises:
        Nothing.
    '''
    facility_menu_option = input('Enter your option:')
    if facility_menu_option not in ONE_TO_SIX:
        raise ValueError('You must choose from number 1~6.')
    else:
        return facility_menu_option


def display_the_analysis_menu():
    '''
    Purpose:
        To display the analysis menu for users to choose.
    Parameters:
        Nothing.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    print('Now you can analyze the number and type of park facilities'
          ' in each community in Vancouver City.\n'
          'Please choose from the following options.\n\n'
          '1. Check the analysis of one neighbourhood.\n'
          '2. Check the analysis of all neighbourhoods.\n')


def choose_from_the_analysis_menu():
    '''
    Purpose:
        To ask users to input their choices according to the analysis menu.
    Parameters:
        Nothing.
    Returns:
        analysis_menu_option(str): represents the user's option.
    Raises:
        Nothing.
    '''
    analysis_menu_option = input('Enter your option:')
    if analysis_menu_option not in ONE_OR_TWO:
        raise ValueError('You must choose from number 1~2.')
    else:
        return analysis_menu_option


def display_find_on_map_menu():
    '''
    Purpose:
        To display the find on map menu for users to choose.
    Parameters:
        Nothing.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    print('Now you can check all the parks and park facilities on a map.\n'
          'Please choose from the following options.\n\n'
          '1. Show all the parks in Vancouver City.\n'
          '2. Find parks with certain conditions.\n'
          '3. Find a park by name.\n')


def choose_from_the_find_menu():
    '''
    Purpose:
        To ask users to input their choices according to the find
        on map menu.
    Parameters:
        Nothing.
    Returns:
        find_menu_option(str): represents the user's option.
    Raises:
        Nothing.
    '''
    find_menu_option = input('Enter your option:')
    if find_menu_option not in ONE_TO_THREE:
        raise ValueError('You must choose from number 1~3.')
    else:
        return find_menu_option


def display_string_or_chart_menu():
    '''
    Purpose:
        To display the string or chart menu for users to choose.
    Parameters:
        Nothing.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    print('You can choose to read the analysis by strings or by charts.\n'
          'Please choose from the following options.\n\n'
          '1. Strings\n'
          '2. Charts\n')


def get_a_park():
    '''
    Purpose:
        To ask users to input a park.
    Parameters:
        Nothing.
    Returns:
        input_park(str): represents a park's name.
    Raises:
        Nothing.
    '''
    park_name = input('Enter a park:')
    return park_name


def get_a_neighbourhood():
    '''
    Purpose:
        To ask users to input a neighbourhood.
    Parameters:
        Nothing.
    Returns:
        input_park(str): represents a neighbourhood's name.
    Raises:
        Nothing.
    '''
    neighbourhood_name = input('Enter a neighbourhood:')
    return neighbourhood_name


def get_a_park_and_area():
    '''
    Purpose:
        To ask users to input a park and an area.
    Parameters:
        Nothing.
    Returns:
        park_name(str): represents a park's name.
        area(str): represents an area.
    Raises:
        Nothing.
    '''
    park_name = input('Enter a park:')
    area = input('Please enter the area:')
    return park_name, area


def get_park_name_and_facility_type():
    '''
    Purpose:
        To ask users to input a park and its facility type.
    Parameters:
        Nothing.
    Returns:
        park_name(str): represents a park's name.
        type(str): represents a park facility's type.
    Raises:
        Nothing.
    '''
    park_name = input('Name of the park:')
    type = input('Facility type:')
    return park_name, type


def get_facility_details():
    '''
    Purpose:
        To ask users to input a park and its facility details.
    Parameters:
        Nothing.
    Returns:
        park_name(str): represents a park's name.
        type(str): represents a park facility's type.
        count(str): represents a park facility's count.
    Raises:
        Nothing.
    '''
    park_name = input('Name of the park:')
    type = input('Facility type:')
    count = input('Facility count:')
    return park_name, type, count


def display_details_of_a_park(park_instances):
    '''
    Purpose:
        To display the details of a given park in park instances.
    Parameters:
        park_instances(list): a list of park objects.
    Returns:
        Nothing
    Raises:
        Nothing.
    '''
    name = input('Enter the park name:')
    # Search the park in the park list.
    # Find the park successfully
    found = False
    for instance in park_instances:
        if instance.name == name:
            print(f'{instance.name}: {instance.hectare} hectare, in'
                  f' {instance.neighbourhood_name}\n')
            found = True
    # Can't find the park
    if found is False:
        print(f"{name} can't be found.\n")


def display_details_of_all_parks(park_instances):
    '''
    Purpose:
        To display the details of all parks in park instances.
    Parameters:
        park_instances(list): a list of park objects.
    Returns:
        Nothing
    Raises:
        Nothing.
    '''
    for instance in park_instances:
        print(f'{instance.name}: {instance.hectare} hectare, in'
              f' {instance.neighbourhood_name}')


def display_details_of_a_park_facility(facility_instances, park_name=None):
    '''
    Purpose:
        To display the details of a park facility in the facility instances.
    Parameters:
        facility_instances(list): a list of park facility objects.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    if not park_name:
        park_name = input('Name of the park:')
    # Search the park facility in the facility list.
    # Find the park facility successfully
    facility_string_list = []
    for instance in facility_instances:
        if instance.park_name == park_name:
            facility_string_list.append(f'{instance.count} {instance.type}')

    # Park facility found
    if len(facility_string_list) != ZERO:
        print(f"{park_name}: {','.join(facility_string_list)}")
    # Can't find the park facility
    else:
        print(f"{park_name} can't be found.\n")


def display_details_of_all_park_facilities(facility_instances):
    '''
    Purpose:
        To display the details of all park facilities in the facility
        instances.
    Parameters:
        facility_instances(list): a list of park facility objects.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    already_displayed_park = []
    for instance in facility_instances:
        if instance.park_name not in already_displayed_park:
            display_details_of_a_park_facility(
                facility_instances, instance.park_name)
            already_displayed_park.append(instance.park_name)


def display_neighbourhood_facility_distribution(
        neighbourhood_name, neighbourhood_facility_dictionary):
    '''
    Purpose:
        To display park facilities' types, counts, and distribution in
        one neighbourhood.
    Parameters:
        neighbourhood_name(str): the name of a given neighbourhood.
        neighbourhood_facility_dictionary(dic): a dictionary whose keys are
        neighbourhood names and values are dictionarys with facility types
        as keys and lists of facility types and distribution as values.
    Returns:
        Nothing.
    Raises:
        Nothing.
    Sample:
        {'Neighbourhood1': {'Facility1': [3, 0.75], 'Facility2': [1, 0.25]}}
        'Neighbourhood1: 3 F1(75.0%), 1 F2(25.0%)\n'
    '''
    facility_string_list = []
    for key, value in neighbourhood_facility_dictionary.items():
        if neighbourhood_name == key:
            for facility_type, details in value.items():
                percentage = round(details[ONE] * HUNDRED, TWO)
                facility_string = f'{details[ZERO]} {facility_type}'\
                    f'({percentage}%)'
                facility_string_list.append(facility_string)
    neighbourhood_facility_string = f"{neighbourhood_name}:"\
        f"{','.join(facility_string_list)}\n"
    print(neighbourhood_facility_string)


def display_all_neighbourhood_facility_distribution(
        neighbourhood_facility_dictionary):
    '''
    Purpose:
        To display park facilities' types, counts, and distribution in
        all neighbourhoods in Vancouver City.
    Parameters:
        neighbourhood_facility_dictionary(dic): a dictionary whose keys are
        neighbourhood names and values are dictionarys with facility types
        as keys and lists of facility types and distribution as values.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    for key in neighbourhood_facility_dictionary.keys():
        display_neighbourhood_facility_distribution(
            key, neighbourhood_facility_dictionary)


def display_filter_conditions():
    '''
    Purpose:
        To ask users to input the filter conditions.
    Parameters:
        Nothing
    Returns:
        required_facility(list): a list of input filter conditions on
        the park facility. The first element represents the type and
        the second represents the count.
        required_neighbourhood(str): the input filter conditions on the
        neighbourhood that parks belong.
    Raises:
        Nothing.
    '''
    # Display the instructions
    print('Now you can filter parks by facility type, facility count,'
          ' and neighbourhood.\n'
          'Enter J to jump the requirements.\n')
    print('Please enter your required facility.')

    # Enter requirements
    facility_type = input('Enter the facility type:')
    facility_count = input('Enter the facility count:')
    if facility_type == 'J' or facility_count == 'J':
        required_facility = None
    else:
        facility_count = int(facility_count)
        required_facility = [facility_type, facility_count]

    required_neighbourhood = input('Enter a neighbourhood:')
    if required_neighbourhood == 'J':
        required_neighbourhood = None
    return required_facility, required_neighbourhood
