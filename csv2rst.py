#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# convert csv file into reStucturedText
#
# Use :
#       python csv2rst.py data.csv data.txt
#       ./csv2rst.py data.csv data.txt
#
#
# Created:     03/09/2012
#
# Licence:     "THE BEER-WARE LICENSE" (Revision 42):
# As long as you retain this notice you can do whatever you want with this stuff.
# If we meet some day, and you think this stuff is worth it, you can buy me a
# beer in return
# Noémie Lehuby
#-------------------------------------------------------------------------------

import sys
import csv


def csv2rst():
    ############ read the input file ##############
    try:
        file_name = sys.argv[1]
    except IndexError:
        return "Use : python csv2rst.py data.csv data.txt"

    input_rows = []

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            input_rows.append(row)

    ############ get columns sizes ##############
    col_nb = len(input_rows[0])

    col_sizes = []
    try :
        for col_index in range(col_nb):
            column = [ row[col_index] for row in input_rows ]
            longuest_content_in_column = max(column, key=len)
            col_sizes.append(len(longuest_content_in_column))
    except:
        raise  Exception("Can't process input csv file !")

    ############ generate output text ##############
    output_txt = []

    row_separator_pattern = "+" + "+".join(["-" * (a_col_size + 2) for a_col_size in col_sizes]) + "+"

    output_txt.append(row_separator_pattern)

    for an_input_row in input_rows :
        output_row = "|"
        for a_col in an_input_row :
            nb_spaces_in_col = col_sizes[an_input_row.index(a_col) ] - len(a_col)
            output_row += " {}{} |".format(a_col, " " * nb_spaces_in_col)
        output_txt.append(output_row)
        output_txt.append(row_separator_pattern)

    ############ return output ##############
    if len(sys.argv) > 2 :
        #assume we have output file name
        output_file = sys.argv[2]
        with open(output_file, 'w') as output:
            for an_output_row in output_txt :
                output.write(an_output_row + "\n")

    else :
        return(output_txt)

if __name__ == '__main__':
    output = csv2rst()
    if output :
        for a_line in output:
            print(a_line)
