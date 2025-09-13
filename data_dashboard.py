'''
Xiyu Fan
CS 5001
Final Project

This is the main file of the parks and facilities program's Controller.
'''
from models.fetch_data import \
    (get_parks_csv, get_needed_park_data, get_facilities_csv,
     get_needed_facility_data)
from utils import (
    create_park_instances, create_facility_instances,
    remove_invalid_park_instances)
from models.model_3_parks_and_facilities_analysis_functions import \
    (create_park_facility_dictionary,
     filter_parks, create_neighbourhood_facility_dictionary,
     expand_the_park_area, reduce_the_park_area, add_a_new_facility,
     delete_a_facility, increase_a_facility_number, reduce_a_facility_number,)
from views.view_parks_and_facilities_interface import \
    (display_the_main_menu, display_the_park_menu, display_the_facility_menu,
     display_details_of_a_park, display_details_of_all_parks,
     display_details_of_a_park_facility, display_the_analysis_menu,
     display_details_of_all_park_facilities, display_find_on_map_menu,
     display_string_or_chart_menu, display_filter_conditions,
     display_neighbourhood_facility_distribution, choose_from_the_main_menu,
     display_all_neighbourhood_facility_distribution, get_a_park,
     get_a_neighbourhood, choose_from_the_park_menu, get_facility_details,
     choose_from_the_facility_menu, choose_from_the_find_menu,
     choose_from_the_analysis_menu, get_a_park_and_area,
     get_park_name_and_facility_type)
from views.view_visualization_map import \
    (create_map, find_a_park_on_map, display_the_map, find_filtered_parks,
     find_a_neighbourhood_pie_chart, display_neighbourhood_facility_bar_chart)
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
ALL_PARKS_MAP = "VancouverCity_parks_and_facility.html"
FILTERED_PARKS_MAP = "VancouverCity_filter_parks.html"
A_PARK_MAP = "VancouverCity_find_a_park.html"
global park_instances, facility_instances


def initialize_data():
    '''
    Purpose:
        To create and clean park objects and facility objects with fetched
        park data.
    Parameters:
        Nothing.
    Returns:
        park_instances(list): a list of park objects.
        facility_instances(list): a list of facility objects.
    Raises:
        Nothing.
    '''
    parks_csv = get_parks_csv()
    needed_park_data = get_needed_park_data(parks_csv)
    park_instances = create_park_instances(needed_park_data)
    facilities_csv = get_facilities_csv()
    needed_facility_data = get_needed_facility_data(facilities_csv)
    facility_instances = create_facility_instances(needed_facility_data)
    park_instances, facility_instances = remove_invalid_park_instances(
            park_instances, facility_instances)
    return park_instances, facility_instances


def process_option_one(park_instances):
    '''
    Purpose:
        To operate the program when users choose option 1 from the main
        menu.
    Parameters:
        park_instances(list): a list of park objects.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    display_the_park_menu()
    park_menu_option = choose_from_the_park_menu()
    if park_menu_option == ONE:
        # expand area
        name, expanded_area = get_a_park_and_area()
        park_instances = expand_the_park_area(
            name, expanded_area, park_instances)
    elif park_menu_option == TWO:
        # reduce area
        name, reduction_area = get_a_park_and_area()
        park_instances = reduce_the_park_area(
            name, reduction_area, park_instances)
    elif park_menu_option == THREE:
        # get details of a park
        display_details_of_a_park(park_instances)
    elif park_menu_option == FOUR:
        # get details of all parks
        display_details_of_all_parks(park_instances)


def process_option_two(park_instances, facility_instances):
    '''
    Purpose:
        To operate the program when users choose option 2 from the main
        menu.
    Parameters:
        park_instances(list): a list of park objects.
        facility_instances(list): a list of facility objects.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    display_the_facility_menu()
    facility_menu_option = choose_from_the_facility_menu()
    if facility_menu_option == ONE:
        # add
        park_name, type, count = get_facility_details()
        facility_instances = add_a_new_facility(
            park_name, type, count,
            park_instances, facility_instances)
    elif facility_menu_option == TWO:
        # delete
        park_name, type = get_park_name_and_facility_type()
        facility_instances = delete_a_facility(
            park_name, type, facility_instances)
    elif facility_menu_option == THREE:
        # increase
        park_name, type, count = get_facility_details()
        facility_instances = increase_a_facility_number(
            park_name, type, count, facility_instances)
    elif facility_menu_option == FOUR:
        # reduce
        park_name, type, count = get_facility_details()
        facility_instances = reduce_a_facility_number(
            park_name, type, count, facility_instances)
    elif facility_menu_option == FIVE:
        # get details of a park facility
        display_details_of_a_park_facility(facility_instances)
    elif facility_menu_option == SIX:
        # get details of all park facilities
        display_details_of_all_park_facilities(facility_instances)


def process_option_three(park_instances, facility_instances,
                         park_facility_dictionary):
    '''
    Purpose:
        To operate the program when users choose option 3 from the main
        menu.
    Parameters:
        park_instances(list): a list of park objects.
        facility_instances(list): a list of facility objects.
        park_facility_dictionary(dic): adictionary whose keys are park
        names and values are facility types and counts.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    display_find_on_map_menu()
    find_option = choose_from_the_find_menu()
    if find_option == ONE:
        # Show all parks
        create_map(
            park_instances, facility_instances,
            park_facility_dictionary)
        display_the_map(ALL_PARKS_MAP)
    elif find_option == TWO:
        # Filter parks by certain conditions
        required_facility, required_neighbourhood = \
            display_filter_conditions()
        filtered_parks = filter_parks(
            park_instances, facility_instances,
            required_facility, required_neighbourhood)
        find_filtered_parks(
            filtered_parks, park_instances, facility_instances,
            park_facility_dictionary)
        display_the_map(FILTERED_PARKS_MAP)
    elif find_option == THREE:
        # Find a park by name
        park_name = get_a_park()
        find_a_park_on_map(
            park_name, park_instances, facility_instances,
            park_facility_dictionary)
        display_the_map(A_PARK_MAP)


def process_option_four(park_instances, facility_instances):
    '''
    Purpose:
        To operate the program when users choose option 4 from the main
        menu.
    Parameters:
        park_instances(list): a list of park objects.
        facility_instances(list): a list of facility objects.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    display_the_analysis_menu()
    neighbourhood_facility_dictionary = \
        create_neighbourhood_facility_dictionary(
            park_instances, facility_instances)
    analysis_menu_option = choose_from_the_analysis_menu()
    # Analysis of the number and type of park facilities in
    # neighbourhoods
    if analysis_menu_option == ONE:
        # Check the analysis of one neighbourhood
        display_string_or_chart_menu()
        string_or_chart_option_one = \
            choose_from_the_analysis_menu()
        input_neighbourhood = get_a_neighbourhood()
        if string_or_chart_option_one == ONE:
            # Check by string
            display_neighbourhood_facility_distribution(
                input_neighbourhood,
                neighbourhood_facility_dictionary)
        elif string_or_chart_option_one == TWO:
            # Check by a pie chart
            find_a_neighbourhood_pie_chart(
                input_neighbourhood,
                neighbourhood_facility_dictionary)
    elif analysis_menu_option == TWO:
        # Check the analysis of all neighbourhoods
        display_string_or_chart_menu()
        string_or_chart_option_two = \
            choose_from_the_analysis_menu()
        if string_or_chart_option_two == ONE:
            # Check by string
            display_all_neighbourhood_facility_distribution(
                neighbourhood_facility_dictionary)
        elif string_or_chart_option_two == TWO:
            # Check by a bar chart
            display_neighbourhood_facility_bar_chart(
                neighbourhood_facility_dictionary)


def main():
    try:
        # create park and facility instances
        park_instances, facility_instances = initialize_data()

        # create a park-facility dictionary
        park_facility_dictionary = create_park_facility_dictionary(
            facility_instances)

    # Set a loop flag
        quit = False
        while quit is not True:
            # Choose from the main menu
            display_the_main_menu()
            main_menu_option = choose_from_the_main_menu()
            # When the user chooses to manage parks
            if main_menu_option == ONE:
                process_option_one(park_instances)
            elif main_menu_option == TWO:
                process_option_two(park_instances, facility_instances)
            elif main_menu_option == THREE:
                # Find parks and facilities on map
                process_option_three(
                    park_instances, facility_instances,
                    park_facility_dictionary)
            elif main_menu_option == FOUR:
                process_option_four(park_instances, facility_instances)
            elif main_menu_option == FIVE:
                quit = True
    except ValueError as e:
        print('ValueError:', e)
    except TypeError as e:
        print('TypeError:', e)
    except NameError as e:
        print('NameError:', e)
    except AttributeError as e:
        print('AttributeError:', e)
    except FileNotFoundError as e:
        print('FileNotFoundError:', e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError:', e)


if __name__ == "__main__":
    main()
