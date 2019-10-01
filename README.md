# PngToTxt
This is just a small project to play around. The goal is to re-create images with characters. There is no real value to this project, but it certainly was a lot of fun. 

## How does it work?
First, we create a database that contains all characters with their average RGB value. The input for the actual conversion is an image. 
We match the average RGB value for each N by M adjacent rectangle in the input image with the most similar character in our character database. The similarity here is measured with Euclidean distance. The output is thus a large string of characters, representing the respective rectangle of pixels in the original image.

## Performance
### Twitter Logo:
![twitter original](https://icon-library.net/images/twitter-app-icon/twitter-app-icon-22.jpg)
![twitter re-creation](https://github.com/STrucks/PngToTxt/blob/master/Pictures/twitter_logo_recr.jpg)


### Google Chrome Logo:
![Google Chrome original](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Google_Chrome_icon_%282011%29.svg/768px-Google_Chrome_icon_%282011%29.svg.png)
![Google Chrome re-creation](https://github.com/STrucks/PngToTxt/blob/master/Pictures/google_chrome_logo_recr.jpg)

### New York Skyline:
![NY skyline original](https://cdn.getyourguide.com/img/tour_img-1096032-146.jpg)
![NY skyline re-creation](https://github.com/STrucks/PngToTxt/blob/master/Pictures/skyline_NY_recr.jpg)

We can see that the reproduction looks very similar to the originals for simple images. For more complex images (e.g. the skyline), the reproduction still features some noticeable  similarities to the original image.

Non of these pictures are mine, they are taken from 
* https://icon-library.net/images/twitter-app-icon/twitter-app-icon-22.jpg
* https://de.wikipedia.org/wiki/Datei:Google_Chrome_icon_(2011).svg
* https://www.getyourguide.de/new-york-city-l59/half-day-panoramic-night-tour-of-new-york-city-t151778/?utm_force=0
