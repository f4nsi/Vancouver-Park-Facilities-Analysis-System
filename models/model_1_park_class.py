'''
Xiyu Fan
CS 5001
Final Project

This is the module file for the Park class of the parks and facilities program.

Description: A module that provides functionalities to manage a park model
in the Vancouver City.

The main features of the park module include expanding the park area,
decreasing the park area, and checking whether the park belongs to a
certain neighbourhood.
'''
ZERO = 0
INDEX_ZERO = 0
INDEX_ONE = 1


class Park():
    '''
    Represents a park located in a neighbourhood with a certain hectare.

    Attributes:
        name(str): The name of the park.
        neighbourhood_name(str): The name of the neighbourhood that the park
        is located.
        hectare(float): The area of the park.
        location(str): The GoogleMapDest of the park.

    Methods:
        is_neighbourhood: To check whether the park is in the input
        neighbourhood.
        expand_area: Expand the area of the park.
        reduce_area: Reduce the area of the park.
    '''
    def __init__(self, name, neighbourhood_name, hectare, location):
        '''
        Purpose:
            To set initial attributes.
        Parameters:
            name(str): The name of the park.
            neighbourhood_name(str): The name of the neighbourhood that the
            park is located.
            hectare(str): The area of the park.
            location(str): The GoogleMapDest of the park.
        Returns:
            Nothing
        Raises:
            ValueError: Raised when the input hectare is not integer or float,
            or not positive.
        '''
        self.name = name
        self.neighbourhood_name = neighbourhood_name
        self.hectare = float(hectare)
        location_list = location.split(',')
        latitude = float(location_list[INDEX_ZERO])
        longitude = float(location_list[INDEX_ONE])
        self.latitude = latitude
        self.longitude = longitude
        if self.hectare < ZERO:
            raise ValueError('The hectare must not be negative.')

    def is_neighbourhood(self, input_neighbourhood=None):
        '''
        Purpose:
            To check whether the park is in the input neighbourhood.
        Parameters:
            input_neighbourhood(str): A specified neighbourhood.
        Returns:
            A boolean value representing whether the park is in the
            input neighbourhood. If input_neighbourhood is None,
            then return True.
        Raises :
            Nothing
        '''
        if input_neighbourhood:
            if self.neighbourhood_name == input_neighbourhood:
                return True
            return False
        return True

    def expand_area(self, expansion_area):
        '''
        Purpose:
            To expand the area of the park.
        Parameters:
            expansion_area(str): The expansion area of the park.
        Returns:
            Nothing
        Raises:
            ValueError: Raised when the input expansion area is not integer
            or float, or not positive.
        '''
        expansion_area = float(expansion_area)
        if expansion_area <= 0:
            raise ValueError('The expansion area must be positive.')
        elif expansion_area > 0:
            self.hectare += expansion_area

    def reduce_area(self, reduction_area):
        '''
        Purpose:
            To reduce the area of the park.
        Parameters:
            reduction_area(str): The reduction area of the park.
        Returns:
            Nothing
        Raises:
            ValueError: Raised when the input reduction area is not integer
            or float, or not positive, or greater than the original area.
        '''
        reduction_area = float(reduction_area)
        if reduction_area <= 0:
            raise ValueError('The reduction area must be positive.')
        elif reduction_area >= self.hectare:
            raise ValueError('The reduction area must be smaller than the'
                             'original area')
        else:
            self.hectare -= reduction_area
