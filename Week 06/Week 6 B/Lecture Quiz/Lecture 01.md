Lecture 01 Quiz
===============  

Question
--------  
What information do you need to draw a single image from a tiled image?  

### Answer  
* The size (width and height) of each image and how the images are arranged in the tiled image.  

#### Explanation  
Note that given the size of each image, you can compute the center of the upper left image easily. If you knew the center of every image within the tiled image, you could use that, but you can also compute that information given the size of a single image and the layout of the tiled image (assuming all images are the same size).  