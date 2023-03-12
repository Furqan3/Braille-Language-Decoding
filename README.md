# Braille-Language-Decoding
## Introduction:
Connected Component Analysis (CCA) is a powerful image processing technique 
used for the segmentation and extraction of useful information from images. It is 
especially useful for the study and analysis of objects present in images. In this 
assignment, we will use CCA to decode Braille language images. Braille is a 
tactile writing system used by visually impaired people, and its characters are 
formed using a combination of six raised dots arranged in a 3 × 2 matrix. Our 
goal is to develop a generic algorithm that can decode any image with Braille 
sequence to the corresponding English version by separating the Braille sequence 
from the background using 8-connectivity based CCA.
## V Set:
V={255}
I am converting the gravyscale image to binary and then invert it.
so the dots become bright and the background become dark.
## Algorithm:
The algorithm consist of the following steps:
- ### Slice: 
To slice each row of the image, we can use the slicing operation in 
Python. This operation allows us to extract a specific portion of the image, 
in this case, a row, as a new image. Once we have sliced each row, we can 
apply the algorithm to each row individually to detect the dots.
- ### Rows:
To get the range of each dotted row, we can iterate over each row 
of the image and check for the presence of dots. We can define a threshold 
value for the intensity of the pixels that are considered as dots. If the 
intensity of a pixel is above this threshold, we consider it as a dot. Once we 
have detected the dots in each row, we can find the range of the dotted 
rows, i.e., the row numbers that contain dots.
- ### Column:
To get the range of each dotted column, we can iterate over each 
column of the image and check for the presence of dots. Similar to the 
rows, we can define a threshold value for the intensity of the pixels that are 
considered as dots. If the intensity of a pixel is above this threshold, we 
consider it as a dot. Once we have detected the dots in each column, we 
can find the range of the dotted columns, i.e., the column numbers that 
contain dots.
- ### Braille Cell:
To check each Braille position and make the Braille cell, we 
can use the range of dotted rows and columns that we obtained in steps 2 
and 3. A Braille cell consists of six dots arranged in a 2x3 matrix. We can 
check each position of the Braille cell, i.e., whether it contains a dot or not, 
by comparing the row and column ranges with the position of each dot in 
the Braille cell.
- ### Decoding: 
To decode the Braille cell and obtain its corresponding 
alphabet, we can create a lookup table that maps each Braille cell to its 
corresponding alphabet. We can compare the Braille cell with this lookup 
table and obtain the corresponding alphabet. Once we have decoded all the 
Braille cells in the image, we can obtain the complete text.
- ## Flow Chart
![image](https://user-images.githubusercontent.com/88136810/224555806-7c28ac69-72af-4629-a12e-3f89ca6da924.png)

