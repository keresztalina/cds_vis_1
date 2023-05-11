# Assignment 1 - Simple image search
This assignment is ***Part 1*** of the portfolio exam for ***Visual Analytics S23***. The exam consists of 4 assignments in total (3 class assignments and 1 self-assigned project).

## 1.1. Contribution
The initial assignment was created partially in collaboration with other students in the course, also making use of code provided as part of the course. The final code is my own. Several adjustments have been made since the initial hand-in.

Here is the link to the GitHub repository containing the code for this assignment: https://github.com/keresztalina/cds_vis_1.git

## 1.2. Assignment description by Ross
*(**NB!** This description has been edited for brevity. Find the full instructions in ```README_rdkm.md```.)*

For this assignment, you'll be using ```OpenCV``` to design a simple image search algorithm.

The dataset is a collection of over 1000 images of flowers, sampled from 17 different species. The dataset comes from the Visual Geometry Group at the University of Oxford, and full details of the data can be found at https://www.robots.ox.ac.uk/~vgg/data/flowers/17/.

For this exercise, you should write some code which does the following:

- Define a particular image that you want to work with
- For that image
  - Extract the colour histogram using ```OpenCV```
- Extract colour histograms for all of the **other* images in the data
- Compare the histogram of our chosen image to all of the other histograms 
  - For this, use the ```cv2.compareHist()``` function with the ```cv2.HISTCMP_CHISQR``` metric
- Find the five images which are most simlar to the target image
  - Save a CSV file to the folder called ```out```, showing the five most similar images and the distance metric:

|Filename|Distance]
|---|---|
|target|0.0|
|filename1|---|
|filename2|---|

This assignment is designed to test that you can:

1. Work with larger datasets of images
2. Extract structured information from image data using ```OpenCV```
3. Quantaitively compare images based on these features, performing *distant viewing*

## 1.3. Methods
The purpose of this script is to search through a dataset of images in order to find the five that are most similar to the user-defined target image. First, the script identifies and generates a list of all the images contained within the directory and specifies the target image. Then, it loops through every image in the folder. It creates a normalized color histogram for every image, essentially quantifying the prevalence of red, green and blue pixels within the image without regard for their location. It then compares each histogram to the histogram of the target image, calculates the distance between them using the chi-square metric, and saves it into a list. From this list it finally extracts the five lowest values, representing the images with the histograms that are least different compared to the target image.

## 1.4. Usage
### 1.4.1. Prerequisites
This code was written and executed in the UCloud application's Coder Python interface (version 1.77.3, running Python version 3.9.2). UCloud provides virtual machines with a Linux-based operating system, therefore, the code has been optimized for Linux and may need adjustment for Windows and Mac.

### 1.4.2. Installations
1. Clone this repository somewhere on your device.
2. Create a ```/data``` folder within the repository. Download the dataset from https://www.robots.ox.ac.uk/~vgg/data/flowers/17/ into ```/cds_vis_1/data``` and unzip it. The script can only be run if the folder containing the files has been unzipped.
3. Open a terminal and navigate into the ```/cds_vis_1``` folder. Run the following lines in order to install the necessary packages:
        
        pip install --upgrade pip
        python3 -m pip install -r requirements.txt

### 1.4.3 Run the script.
In order to run the script, make sure your current directory is still the ```/cds_vis_1``` folder. From command line, run:

        python3 src/image_search.py <IMAGE_NAME>
        
```<IMAGE_NAME>``` represents a compulsory user-defined argument with which the target image must by defined. There are 1360 images in the dataset, and their names range from ```"image_0001.jpg"``` to ```"image_1360.jpg"```. After the code has finished running, the output file with the list of most similar images can be found in ```/cds_vis_1/out```.

### 1.5 Discussion
When running the code, I opted to use ```"image_0127.jpg"``` as the target image, which contains relatively small white flowers, with large amounts of grass and dirt also in the picture. The output file, ```out/image_0127.csv``` is a .csv file containing 5 rows for the 5 most similar images, and 2 columns for the filename and difference in chisqr for each of these images. 

The most similar images, with a difference in chisqr of 42.67, is ```"image_0319.jpg"```, which does not show the same flower, but *does* show lots of grass and dirt. The next most similar image, ```"image_0751.jpg"```, is of a sunflower, which contains a center that is the same color as soil, and leaves that are the same color as grass. The situation is the same for the rest of the similar images, too: the algorythm has been more successful at finding green and brown than at finding similar flowers.

As such, a principle weakness of the color histogram method is revealed: by using only the distribution of color without taking into account color location, shapes and sizes, a lot of useful information is lost. 
