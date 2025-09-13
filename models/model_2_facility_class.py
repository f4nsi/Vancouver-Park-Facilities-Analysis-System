'''
Xiyu Fan
CS 5001
Final Project

This is the module file for the Facility class of the parks and facilities
program.

Description: A module that provides functionalities to manage a park facility
model in the Vancouver City.

The main features of the park facility module include increasing and decreasing
the facility count, and checking if the facility type corresponds to a certain
type.
'''
ZERO = 0


class Facility():
    '''
    Represents a park facility's location, type, and count.

    Attributes:
        park_name(str): The name of the park that the facility is located.
        type(str): The type of the park facility.
        count(int): The count of the park facility.

    Methods:
        is_type: To check if the facility type corresponds to the input type.
        increase_facility_count: To increase the facility count.
        reduce_facility_count: To reduce the facility count.
    '''
    def __init__(self, park_name, facility_type, facility_count):
        '''
        Purpose:
            To set initial attributes.
        Parameters:
            park_name(str): the name of the park that the facility is located.
            type(str): The type of the park facility.
        count(int): The count of the park facility.
        Returns:
            Nothing
        Raises:
            ValueError: Raised when the input facility count is not integer or
            float, or not positive.
        '''
        self.park_name = park_name
        self.type = facility_type
        self.count = int(facility_count)
        if self.count <= ZERO:
            raise ValueError('The count must be positive.')

    def is_type(self, input_type=None):
        '''
        Purpose:
            To check if the facility type corresponds to the input type.
        Parameters:
            input_type(str): A specified facility type.
        Returns:
            A boolean value: Represents whether the facility type is the same
            with the input facility type. If the input_type is none, then
            return True.
        '''
        if input_type:
            if self.type == input_type:
                return True
            return False
        else:
            return True

    def is_count(self, input_count=None):
        '''
        Purpose:
            To check if the facility count is greater than the input count.
        Parameters:
            input_count(str): A specified facility count.
        Returns:
            A boolean value: Represents whether the facility count is the same
            with the input facility count. If the input_count is none, then
            return True.
        '''
        if input_count:
            if self.count >= int(input_count) >= ZERO:
                return True
            return False
        else:
            return True

    def increase_facility_count(self, new_facility_count):
        '''
        Purpose:
            To increase the facility count of park facilities that already
            exist.
        Parameters:
            new_facility_count(str): The count of increased facility.
        Returns:
            Nothing
        Raises:
            ValueError: Raised when the increase of facility count
            is negative, or not an integer.
        '''
        new_facility_count = float(new_facility_count)
        # Check whether the input facility count is an integer
        if new_facility_count != int(new_facility_count):
            raise ValueError('The increase facility count must be'
                             ' an integer')
        else:
            # Check whether the count is positive
            if new_facility_count <= ZERO:
                raise ValueError('The increase facility count must be'
                                 ' positive.')
            elif new_facility_count > ZERO:
                self.count += int(new_facility_count)

    def reduce_facility_count(self, reduction_facility_count):
        '''
        Purpose:
            To reduce the facility count of park facilities that already exist.
        Parameters:
            reduction_facility_count(str): The count of reduced facility.
        Returns:
            Nothing
        Raises:
            ValueError: Raised when the reduction count is negative, or not
            an integer, or not smaller than the original account.
        '''
        reduction_facility_count = float(reduction_facility_count)
        if reduction_facility_count <= ZERO:
            raise ValueError('The reduction facility count must be positive.')
        elif self.count <= reduction_facility_count:
            raise ValueError('The reduction facility count must be smaller'
                             'than the original count.')
        elif self.count > reduction_facility_count:
            self.count -= int(reduction_facility_count)
