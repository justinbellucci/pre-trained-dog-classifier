#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """

    # Create an empty dictionary named results_dic
    # Open the image folder and put contents in a list
    results_dic = dict()
    filename_list = listdir(image_dir)

    # Set string to lower case letters and assign to new name
    # Split the string into words by '_' deliminator
    # Creat an empty string
    for name in filename_list:
        low_pet_image = name.lower()
        word_list_pet_image = low_pet_image.split('_')
        pet_name = ""

        # Loop through each word in the list and place only words with letters in the pet_name string
        for word in word_list_pet_image:
            if word.isalpha():
              pet_name += word + " "
        
        # Strip off the leading and trailing whitespace
        # Assign Key: name, Value: pet_name to results_dic
        pet_name = pet_name.strip()
        results_dic[name] = [pet_name]
        
    return results_dic
