#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
David Dell
MET CS 521
06/24/20
Description:
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
    # used for initially
    def set_positive_cell(self, x, y):
        print('setting cell')
        print('setting cell y {} x {}'.format(y, x))
        # row , column
        self.__matrix[y][x] = int(1)
        self.set_cell(x,y, 1)
        # see if row has been set already

        if len(self.__positive_values) == 0:
            self.__positive_values.append([x,y])
        else:
            for i in range(len(self.__positive_values)):
                #if its been set then see if its now negative and unslice it
                if self.__positive_values[i] == [x,y] and cell_type == 0:
                    self.__positive_values.pop(i)
                elif self.__positive_values[i] != [x,y]:
                    #else lets now set it
                    self.__positive_values.append([x,y])

    def set_cell(self, x, y, value):

        try:
            # if it fails then the grid space doesnt exist
            self.__matrix[y][x] = int(value)
            #need to now check if cordinate has been counted before adding to count
            self.__cell_count = self.__cell_count + 1
        except IndexError:
            #index not found cnt
            self.__invalid_cell_count = self.__invalid_cell_count + 1

    def __set_matrix(self):
        print('setting matrix')
        self.__matrix = np.zeros((self.__height, self.__width), dtype=np.int32)


    def run(self):
        if self.__steps == 0:
            print('1 Cell for 0 Steps')
            return

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

                #next level stuff
                inner_count = 0
                while inner_count <= self.__steps - count:

                    #populate first column, gotta go left right up and down
                    self.set_cell(new_column_right, current_row + inner_count, 2)
                    self.set_cell(new_column_left, current_row + inner_count, 2)
                    self.set_cell(new_column_right, current_row - inner_count, 2)
                    self.set_cell(new_column_left, current_row - inner_count, 2)

                    #populate first row
                    self.set_cell(current_column + inner_count, new_row_up, 2)
                    self.set_cell(current_column + inner_count, new_row_down, 2)
                    self.set_cell(current_column - inner_count, new_row_up, 2)
                    self.set_cell(current_column - inner_count, new_row_down, 2)

                    inner_count = inner_count + 1
                count = count + 1


        print(self.__matrix)




# steps, width, height
n = Neighborhood(2, 11, 11)
# x,y
n.set_positive_cell(2,4)
n.set_positive_cell(8,8)
n.run()

#lets turn this into a program for the user to enter the values 
"""
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
"""
