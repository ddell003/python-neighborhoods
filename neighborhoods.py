#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
David Dell
06/24/20
Description:
To run:  python3 neighborhoods.py

"""
import os.path
import numpy as np


class Neighborhood:

    def __init__(self, steps, width, height):
        """
        Lets initialize the class
        :param n:
        :param side:
        :param x:
        :param y:
        """
        self.__steps = steps
        self.__width = width
        self.__height = height
        self.__set_matrix()
        self.__positive_values = []
        self.__cell_count = 0
        self.__invalid_cell_count = 0

    # assume that all cells are negative unless otherwise specified
    # type is either positive or negative
    def set_positive_cell(self, x, y):
        # row , column
        self.set_cell(x,y, 1)
        # see if row has been set already

        if len(self.__positive_values) == 0:
            self.__positive_values.append([x,y])
        else:
            for i in range(len(self.__positive_values)):

                if self.__positive_values[i] != [x,y]:
                    #else lets now set it
                    self.__positive_values.append([x,y])

    def set_cell(self, x, y, value):

        try:
            # can remove out of try catch now, was relay on failure to catch out of range
            if x > self.__width or y > self.__height or x < 0 or y < 0:
                return
            print('x {} rows {}'.format(x, self.__width))
            # if it fails then the grid space doesnt exist
            print('setting cell y {} x {}'.format(y, x))
            # only increase count if cell not set
            if self.__matrix[y][x] == 0:
                self.__cell_count = self.__cell_count + 1

            self.__matrix[y][x] = int(value)

        except IndexError:
            # index not found cnt
            self.__invalid_cell_count = self.__invalid_cell_count + 1

    def __set_matrix(self):
        print('setting matrix')
        self.__matrix = np.zeros((self.__height, self.__width), dtype=np.int32)


    def run(self):

        for town in self.__positive_values:
            count = 1;
            current_row = town[1]
            current_column = town[0]

            while count <= self.__steps:
                # go left first row, column
                new_column_right = town[0] + count
                new_column_left = town[0] - count

                new_row_up = current_row + count
                new_row_down = current_row - count

                # next level stuff
                inner_count = 0
                while inner_count <= self.__steps - count:

                    # populate first column, gotta go left right up and down
                    self.set_cell(new_column_right, current_row + inner_count, 2)
                    self.set_cell(new_column_left, current_row + inner_count, 2)
                    self.set_cell(new_column_right, current_row - inner_count, 2)
                    self.set_cell(new_column_left, current_row - inner_count, 2)

                    # populate first row
                    self.set_cell(current_column + inner_count, new_row_up, 2)
                    self.set_cell(current_column + inner_count, new_row_down, 2)
                    self.set_cell(current_column - inner_count, new_row_up, 2)
                    self.set_cell(current_column - inner_count, new_row_down, 2)

                    inner_count = inner_count + 1
                count = count + 1


        print(self.__matrix)
        print('\nTotal Cells: {}'.format(self.__cell_count))




# steps, width, height
#n = Neighborhood(2, 10, 11)
# x,y
#n.set_positive_cell(2,4)
#n.set_positive_cell(8,8)
#n.run()

# was setting up a program to prompt user to enter dimensions but I ran out of time
if __name__ == '__main__':

    # start loop for over all program
    while True:

        user_input = input('Enter Steps ').strip()

        try:
            steps = int(user_input)
        except:
            print('You entered {}, Please Enter a valid integer'.format(user_input))

        prompt_for_array_input = True

        while prompt_for_array_input:

            raw_array = input('Enter array dimension X, Y separated by comas: ')
            array_input = raw_array.strip().split(',')
            try:
                x = int(array_input[0])
                y = int(array_input[1])
                neighborhood = Neighborhood(steps, x, y)
                prompt_for_array_input = False
            except:
                print('You entered {}, Please Enter a valid dimension'.format(raw_array))

        # now need to prompt for position of positive numbers (could be many)
        prompt_for_coordinates = True
        while prompt_for_coordinates:

            raw_array = input('Enter positive cell coordinates  X, Y separated by comas or X to exit: ')
            array_input = raw_array.strip().split(',')
            try:
                if raw_array == 'X' or raw_array == 'x':
                    prompt_for_coordinates = False
                    break

                x = int(array_input[0])
                y = int(array_input[1])
                neighborhood.set_positive_cell(x, y)
                #prompt_for_array_input = False
            except:
                print('You entered {}, Please Enter a valid dimension'.format(raw_array))


        neighborhood.run()

        break
