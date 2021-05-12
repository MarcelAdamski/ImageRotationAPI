# Image Rotation API 
Simple script that rotate image when found solid line which is sequention of three white and three red pixels horizontally or vertically in your PNG image.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to run](#how-to-run)
* [How to use](#how-to-use)
* [Output example](#output-example)

## General info
Rotation......
* White pixel (HEX) - #ffffff
* Red pixel (HEX) - #ff0000

## Technologies
Created with:
* Python 
* Flask
* Docker

## How to run
There are several options to run this script. I will briefly describe two of them from most to least recommended.

# Docker using docker image
In this step Docker is required. Download [docker](https://www.docker.com/products/docker-desktop)
1. Download zip file.
2. In command line type ```docker build -t image-rotation-api .```

## Additional info
The author tested several solutions. In the case of images with low resolution, the differences in script execution time are negligible. However, provided solution is faster for larger images with lots of white pixels compared to
solutions with pixel-by-pixel comparison.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

Rozwiązanie wykonane w języku Python. Aby uruchomić usługę wymagany jest zainstalowany Python na komputerze:
https://www.python.org/downloads/windows/

Instrukcja uruchomienia usługi:
1. Rozpakować plik zip

2.1 Poprzez dowolne IDE (wrzucić plik server.py)

2.2 Poprzez aplikacje Docker.
Wymagany zainstalowany Docker:Cancel changes
https://www.docker.com/products/docker-desktop

W lini komend przejsc do folderu:
cd ./2021_devops_intern_Marcel_Adamski/script-docker

Nastepnie zbudować obraz docker'a:
docker build -t docker-script .
Nazwa jest dowolna - w przykładzie "script-docker" można zastąpić inna nazwą, którą trzeba w dalszym kroku respektować.

docker-images - sprawdź, czy obraz się poprawnie zainstalował

Nastepnie uruchomić i wystartować server komendą (upewnij się, że port 5000 jest wolny):
docker run -p 5000:5000 docker-script

2.3 Ręcznie poprzez linię komend
Zainstalować biblioteki poprzez plik requirement.txt
Otworzyć linię komend i komendą cd przejść do wypakowanego zip'a:
cd ./2021_devops_intern_Marcel_Adamski/script-docker

A nastepnie zainstalować biblioteki:
pip install -r requirements.txt

Uruchomić usługę:
Przejść do folderu /app i w linii komend:
python server.py

4. Wywołać żadanie POST np. poprzez usługę POSTMAN
- W Postman'ie wybrać metodę (POST) i wpisać adres: http://localhost:5000/rotate
- W zakładce body w rubryce Key wpisać "image", oraz w tej samej rubryce zmienić format z "Text" na "File"
- W rubryce value wybrać plik, a następnie kliknąć Send.
