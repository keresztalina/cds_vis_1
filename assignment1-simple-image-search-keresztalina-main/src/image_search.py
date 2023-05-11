##### LOAD MODULES
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

##### ARGUMENT PARSER
# Create ArgumentParser object.
parser = argparse.ArgumentParser()

# Add argument to allow user to input target filename.
parser.add_argument(
    "target",
    help = "Filename of target image.")

# Parse the arguments.
args = parser.parse_args()

# Access the values of the arguments.
target_image = args.target

##### FUNCTIONS
# IMAGE LOADING FUNCTION
def load_hist_norm(filename):

    # Load image.
    image = cv2.imread(filename)

    # Create histogram for image.
    hist = cv2.calcHist([image], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])

    # Normalize histogram values.
    hist = cv2.normalize(hist, hist, 0, 1.0, cv2.NORM_MINMAX)

    return(hist)

# FINDING SIMILAR IMAGES FUNCTION
def find_similar(target):

    # Define folder in which images are contained.
    image_folder = os.listdir("data")

    # Load target image, create and normalize histogram.
    hist1 = load_hist_norm(
        os.path.join(
            "data", 
            target))

    # Initialize empty list for the results of comparison.
    results = []
    
    # Loop through the files in the folder.
    for image_name in image_folder:

        # Prevent the input image from being compared to itself.
        if image_name == target:
            continue  

        # Load comparison image, create and normalize histogram.
        hist2 = load_hist_norm(
            os.path.join(
                "data", 
                image_name))
        
        # Calculate difference using chisqr metric
        distance = round(
            cv2.compareHist(
                hist1, 
                hist2, 
                cv2.HISTCMP_CHISQR), 
                2)

        # Append results of comparison to list for easier search.
        results.append({
            "Filename": image_name, 
            "Distance": distance})

    # Create dataframe of results.
    results_df = pd.DataFrame(results)

    # Find five most similar images by taking lowest chisqr value.
    top_five = results_df.nsmallest(
        5, 
        "Distance")

    # Fix up the 'target' variable for nicer filename.
    target_name = target.split(".")[0]

    # Save to .csv file.
    top_five.to_csv(
        os.path.join(
            "out", 
            target_name + ".csv"), 
        index = False)

##### RUN IMAGE SEARCH
def main():

    # Run image search function.
    find_similar(target_image)

if __name__ == "__main__":
    main()