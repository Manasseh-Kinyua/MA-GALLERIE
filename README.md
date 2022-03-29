# MA-GALERIE  
## Author  
  
>[MANASSEH-KINYUA](https://github.com/Manasseh-Kinyua)  
  
# Description  
This is a Django application for personal gallery that allows a user to upload images for others to see and be able to to share by copying the image link.
  
##  Live Link  
 Click [View Site](https://nassehgalerie.herokuapp.com/)  to visit the site
 
## User Story  
  
* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* Search for different categories   
* Copy a link to the photo to share with my friends.  
* View photos based on the location they were taken.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Manasseh-Kinyua/MA-GALLERIE.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd MA-GALLERIE  
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations Gallery 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python3 manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python3 manage.py runserver 
```
##### Testing the application  
 ```bash 
 python3 manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [nassehkinyua99@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Owiti-Charles/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **Manasseh Kinyua**