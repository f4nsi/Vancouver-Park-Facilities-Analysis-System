'''
Xiyu Fan
CS 5001
Final Project

This is the map visualization file of the parks and facilities program's View.
'''
import folium
import webbrowser
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
ZERO = 0
ONE = 1
ONE_POINT_ONE = 1.1
TWO = 2
HUNDRED = 100
MAX_WIDTH = 300
ZOOM_LEVEL = 13
HIGHER_ZOOM_LEVEL = 15
MAP_CENTER = [49.240978, -123.112028]
BAR_WIDTH = 0.35
BOTTOM = 0.28
RIGHT = 0.8
FORTY = 40
GREEN = 'green'
GRAY = 'lightgray'
ORANGE = 'orange'


def get_popup_content_facility_details(park_name, park_facility_dictionary):
    '''
    Purpose:
        To get facility details for the popup content.
    Parameters:
        park_name(str): Name of a park.
        park_facility_dictionary(dictionary):
        {'Park1': [[Pool, 1], [Playground, 2]]}
    Returns:
        popup_facility_details(str):'1 Pool, 2 Playground'
    >>> get_popup_content_facility_details
    ... ('Park1', {'Park1': [[Pool, 1], [Playground, 2]]})
    '1 Pool, 2 Playground'
    '''
    facility_list = park_facility_dictionary[park_name]
    details_list = []
    for facility in facility_list:
        facility_str = f'{facility[ONE]} {facility[ZERO]}'
        details_list.append(facility_str)
    popup_facility_details = ','.join(details_list)
    return popup_facility_details


def create_popup_content(park, facility=None,
                         park_facility_dictionary=None):
    '''
    Purpose:
        To create popup content for parks with facility and without facility
    separately.
    Parameters:
        park(object): a park object.
        facility(object): a facility object.
        park_facility_dictionary(dictionary): a dictionary whose keys are park
        names and values are lists of facility details.
    Returns:
        folium.Popup(popup_html, max_width=300): a popup content for parks with
        facility and without facility
    Raises:
        Nothing.
    '''
    if facility is not None and park_facility_dictionary is not None:
        popup_html = f'<b>{park.name}(with facility)</b><br>'
        popup_html += f'<b>Neighbourhood:</b> {park.neighbourhood_name}<br>'
        popup_html += f'<b>Hectare:</b> {park.hectare} hectare<br>'
        popup_facility = get_popup_content_facility_details(
            park.name, park_facility_dictionary)
        popup_html += f'<b>Facility:</b> {popup_facility}<br>'
    else:
        popup_html = f'<b>{park.name}(no facility)</b><br>'
        popup_html += f'<b>Neighbourhood:</b> {park.neighbourhood_name}<br>'
        popup_html += f'<b>Hectare:</b> {park.hectare} hectare<br>'
    return folium.Popup(popup_html, max_width=MAX_WIDTH)


def create_marker(park, color, facility=None, park_facility_dictionary=None):
    '''
    Purpose:
        Create a marker for a park.
    Parameters:
        park(object): a park object.
        color(str): the color of a marker.
        facility(object): a facility object
        facility_density_dictionary(dictionary): a dictionary whose keys are
        park names and values are corresponding park facility density.
    Returns:
        marker(folium.Marker): a marker on the map created by folium.
    '''
    location = [park.latitude, park.longitude]
    if facility:
        popup_content = create_popup_content(park, facility,
                                             park_facility_dictionary)
    else:
        popup_content = create_popup_content(park)
    icon = folium.Icon(color=color)
    marker = folium.Marker(location=location, popup=popup_content, icon=icon)
    return marker


def create_map(park_instances, facility_instances, park_facility_dictionary):
    '''
    Purpose:
        Create the a map with all park instances.
    Parameters:
        park_instances(list): a list of park objects.
        faciliity_instances(list): a list of facility objects.
        park_facility_dictionary(dictionary): a dictionary whose keys are park
        names and values are lists of facility details.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    # Create the centre of map
    map = folium.Map(location=MAP_CENTER, zoom_start=ZOOM_LEVEL)

    # Add green markers for parks with facility
    # Add grey markers for parks without facility
    for park in park_instances:
        with_facility = False
        for facility in facility_instances:
            if facility.park_name == park.name:
                marker = create_marker(
                    park, GREEN, facility, park_facility_dictionary)
                marker.add_to(map)
                with_facility = True
        if with_facility is False:
            marker = create_marker(park, GRAY)
            marker.add_to(map)

    # Save the map
    map.save("VancouverCity_parks_and_facility.html")


def find_a_park_on_map(park_name, park_instances, facility_instances,
                       park_facility_dictionary):
    '''
    Purpose:
        Find a park by its name on map and color its marker into Orange.
    Parameters:
        park_name(str): a park's name.
        park_instances(list): a list of park objects.
        faciliity_instances(list): a list of facility objects.
        park_facility_dictionary(dictionary): a dictionary whose keys are park
        names and values are lists of facility details.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    # Find the park instance and create the map centre
    found = False
    for park in park_instances:
        if park.name == park_name:
            map = folium.Map(location=[park.latitude, park.longitude],
                             zoom_start=HIGHER_ZOOM_LEVEL)
            found = True
            # Add orange marker for the wanted park
            with_facility = False
            for facility in facility_instances:
                if facility.park_name == park_name:
                    marker = create_marker(
                        park, ORANGE, facility, park_facility_dictionary)
                    marker.add_to(map)
                    with_facility = True
            if with_facility is False:
                marker = create_marker(park, ORANGE)
                marker.add_to(map)
            park_instances_new = park_instances[:]
            park_instances_new.remove(park)
    if found is False:
        raise ValueError(f"{park_name} can't be found.")

    # Add green markers for parks with facility
    # Add grey markers for parks without facility
    for park in park_instances_new:
        with_facility = False
        for facility in facility_instances:
            if facility.park_name == park.name:
                marker = create_marker(
                    park, GREEN, facility, park_facility_dictionary)
                marker.add_to(map)
                with_facility = True
        if with_facility is False:
            marker = create_marker(park, GRAY)
            marker.add_to(map)

    # Save the map
    map.save("VancouverCity_find_a_park.html")


def find_filtered_parks(filtered_parks, park_instances, facility_instances,
                        park_facility_dictionary):
    '''
    Purpose:
        Show filtered park on a map.
    Parameters:
        filtered_parks(list): a list of parks qualified for the user's
        requirements.
        park_instances(list): a list of park objects.
        faciliity_instances(list): a list of facility objects.
        park_facility_dictionary(dictionary): a dictionary whose keys are park
        names and values are lists of facility details.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    map = folium.Map(location=MAP_CENTER, zoom_start=ZOOM_LEVEL)
    park_instances_new = park_instances[:]

    # Add orange markers for filtered parks
    for filtered_park in filtered_parks:
        with_facility_one = False
        for facility in facility_instances:
            if facility.park_name == filtered_park.name:
                marker = create_marker(
                    filtered_park, ORANGE, facility,
                    park_facility_dictionary)
                marker.add_to(map)
                # Remove added park instance from the list
                for park_intance in park_instances_new:
                    if park_intance.name == filtered_park.name:
                        park_instances_new.remove(park_intance)
                with_facility_one = True
        if with_facility_one is False:
            marker = create_marker(filtered_park, ORANGE)
            marker.add_to(map)
            # Remove added park instance from the list
            for park_intance in park_instances_new:
                if park_intance.name == filtered_park.name:
                    park_instances_new.remove(park_intance)

    # Add green markers for parks with facility
    # Add grey markers for parks without facility
    for park in park_instances_new:
        with_facility_two = False
        for facility in facility_instances:
            if facility.park_name == park.name:
                marker = create_marker(
                    park, GREEN, facility, park_facility_dictionary)
                marker.add_to(map)
                with_facility_two = True
        if with_facility_two is False:
            marker = create_marker(park, GRAY)
            marker.add_to(map)

    # Save the map
    map.save("VancouverCity_filter_parks.html")


def display_a_neighbourhood_facility_pie_chart(
        neighbourhood, facility_dictionary):
    '''
    Purpose:
        To display the number and distribution of different facility in a
    neighbourhood by a pie chart.
    Parameters:
        neighbourhood(str): the name of neighbourhood.
        facility_dictionary(dictionary): the number and distribution of
        facility.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    labels = list(facility_dictionary.keys())
    sizes = [value[0] for value in facility_dictionary.values()]
    percentages = [value[1] for value in facility_dictionary.values()]

    label_strings = []
    for i in range(len(labels)):
        label_strings.append(f'{labels[i]}: ({sizes[i]}, '
                             f'{round(percentages[i] * HUNDRED, TWO)}%)')

    plt.pie(sizes, labels=label_strings)
    plt.title(f'The number and distribution of different facility in '
              f'{neighbourhood}')

    plt.axis('equal')
    plt.show()


def find_a_neighbourhood_pie_chart(
        neighbourhood, facility_distribution_dictionary):
    '''
    Purpose:
        To ask the user to input a neighbourhood name and display its
    pie chart of facility number and distribution.
    Parameters:
        facility_dictionary(dictionary): the number and distribution of
        facility.
    Returns:
        Nothing.
    Raises:
        ValueError: Raises when the input neighbourhood can't be found.
    '''
    found = False
    for key, value in facility_distribution_dictionary.items():
        if neighbourhood == key:
            facility_dictionary = value
            found = True
    if found is False:
        raise ValueError(f"{neighbourhood} can't be found.")
    display_a_neighbourhood_facility_pie_chart(neighbourhood,
                                               facility_dictionary)


def display_neighbourhood_facility_bar_chart(facility_dictionary):
    '''
    Purpose:
        To display the number and distribution of different facilities in each
    neighbourhood by a bar chart.
    Parameters:
        facility_dictionary (dictionary): The dictionary containing facility
        information for each neighbourhood.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    plt.rcParams['figure.subplot.right'] = RIGHT
    plt.rcParams['figure.subplot.bottom'] = BOTTOM
    neighbourhoods = list(facility_dictionary.keys())
    num_neighbourhoods = len(neighbourhoods)

    # Create a dictionary to map each facility to a unique color
    unique_colors = {}
    color_index = ZERO

    _, ax = plt.subplots()

    # Track the cumulative values of each facility
    bottom_values = [0] * num_neighbourhoods

    # Store the colors of each facility
    facility_colors = {}

    for i, (_, facility_values) in enumerate(facility_dictionary.items()):
        facilities = list(facility_values.keys())
        values = [value[ZERO] for value in facility_values.values()]

        # Calculate the index position of each neighbourhood
        position = i

        # Create bars for each facility in each neighbourhood
        for j, facility in enumerate(facilities):
            # Check if the current facility already has a color assigned
            # if not, assign a new color
            if facility not in unique_colors:
                unique_colors[facility] = color_index
                facility_colors[facility] = plt.cm.get_cmap('tab20c', FORTY)(
                    unique_colors[facility])
                color_index += ONE
            # Get the color corresponding to the facility
            color = facility_colors[facility]

            ax.bar(position, values[j], BAR_WIDTH, color=color,
                   bottom=bottom_values[i])
            # Update the bottom value
            bottom_values[i] += values[j]  # Update the bottom value

    # Display the legend showing facilities and their corresponding colors
    unique_facilities = list(unique_colors.keys())
    unique_colors = [facility_colors[facility]
                     for facility in unique_facilities]
    ax.legend(handles=[Patch(color=color, label=facility) for color, facility
                       in zip(unique_colors, unique_facilities)],
              bbox_to_anchor=(ONE, ONE_POINT_ONE), loc='upper left')

    ax.set_xlabel('Neighbourhood Name')
    ax.set_ylabel('Facility Count')
    ax.set_title('Facility Distribution in Neighbourhoods')
    ax.set_xticks(range(num_neighbourhoods))
    # Rotate labels for vertical display
    ax.set_xticklabels(neighbourhoods, rotation=90)

    plt.show()


def display_the_map(file_path):
    '''
    Purpose:
        To display the map.
    Parameters:
        file_path(str): the file path of the map that users want to
        read.
    Returns:
        Nothing.
    Raises:
        Nothing.
    '''
    webbrowser.open(file_path)
