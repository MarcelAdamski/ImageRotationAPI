# Image Rotation API 
Simple script that rotate image when found solid line which is sequention of three white and three red pixels horizontally or vertically in your PNG image.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to run](#how-to-run)
* [How to use](#how-to-use)
* [Additional info](#additional-info)

## General info
This script is a service with ```/rotate``` endpoint which is a POST request that accepts only png images. Service is checking whether there is a solid line of three white pixels (#ffffff) and three red pixels (#ff0000). It analyze situations where the line is placed horizontally or vertically. After detecting such a line, the application should rotate the image so that the line is placed vertically, with white pixels up. In case the source image contains a vertical line with white pixels on the bottom, image will be rotated image by 180 degrees. 
* After successful graphic operation, the image is saved again in PNG format and returned in response to the above-mentioned POST request with ```200``` status code (OK).
* If the source image contains more than one solid line and they are contradict, script will return ```400``` status code (Bad request).
* In the situation where the line does not appear in the picture, script automatically will return an empty answer with ```204``` status code (No content).
## Technologies
Created with:
* Python 
* Flask
* Docker

## How to run
There are several options to run this script. I will briefly describe two of them from most to least recommended.

### Docker using docker image
In this step Docker is required. Download [docker](https://www.docker.com/products/docker-desktop).
1. Download zip file.
2. Change directory in command line to folder with ```Dockerfile``` and type ```docker build -t image-rotation-api .```
Name docker image however you want (in this case ```image-rotation-api```), but you will have to respect it in next step.
4. Check if docker image has properly mounted. To do this type in cmd ```docker-images```.
5. Run script and local server with ```docker run -p 5000:5000 image-rotation-api```. Make sure that port ```5000``` is free.

### By running ```server.py``` python file.
1. Python interpreter is required for this step. Download [python](https://www.python.org/downloads/windows/).
2. Change directory in command line to folder with ```requirements.txt``` and install required libraries and packages by typing ```pip install -r requirements.txt```.
3. Change directory to ```app``` folder and run service by typing ```python server.py```.

## How to use
You can POST png image for example by ```curl``` or [postman](https://www.postman.com/)

### Curl
1. Change directory in command line where you have PNG image.
2. Example use of curl:
```
curl -v -F "image=@yourimage.png" http://localhost:5000/rotate -o rotated.png
```
where ```yourimage.png``` is your png file and ```rotated.png``` is output file.

### POSTMAN
1. In Postman choose POST method and in url type: ```http://localhost:5000/rotate```
2. In the body tab in the field Key type ```image```, and in the same field change format from "Text" to "File"
3. As value choose your PNG image and click Send. 

## Additional info
The author tested several solutions. In the case of images with low resolution, the differences in script execution time are negligible. However, provided solution is faster for larger images with lots of white pixels compared to
solutions with pixel-by-pixel comparison.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
