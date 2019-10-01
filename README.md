# PngToTxt
This is just a small project to play around. The goal is to re-create images with characters. There is no real value to this project, but it certainly was a lot of fun. 

## How does it work?
First, we create a database that contains all characters with their average RGB value. The input for the actual conversion is an image. 
We match the average RGB value for each N by M adjacent rectangle in the input image with the most similar character in our character database. The similarity here is measured with Euclidean distance. The output is thus a large string of characters, representing the respective rectangle of pixels in the original image.

## Performance
### Twitter Logo:


### Google Chrome Logo:


### New York Skyline:


We can see that the reproduction looks very similar to the originals for simple images. For more complex images (e.g. the skyline), the reproduction still features some noticeable  similarities to the original image.
