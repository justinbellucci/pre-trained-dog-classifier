#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Justin Bellucci 
# DATE CREATED: 03_08_2020                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
# 
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
              - resnet, alexnet, or vgg
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Creates Arguement Parser object named parser
    parser = argparse.ArgumentParser()
    # Argument 1: Path to a folder
    parser.add_argument('--dir', type = str, default = 'intropyproject-classify-pet-images/pet_images', help = 'Path to the folder of pet images')
    # Argument 2: CNN Model Architecture
    parser.add_argument('--arch', type = str, default = 'vgg', help = 'CNN Model Architecture')
    # Argument 3: Text file with valid dognames
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt', help = 'Text file with list of valid dog names')

    # Assigns variable in_args to parse_args()
    in_args = parser.parse_args()
    print("\nArgument 1", in_args.dir)
    print("\nArgument 2", in_args.arch)
    print("\nArgument 3", in_args.dogfile)
    return in_args