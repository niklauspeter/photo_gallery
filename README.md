# Photo_gallery

This project was generated with Python version 3.6.

### By Niklauspeter

##  Description
This is a django web appliction that allows a user to view pictures posted by the administrator. users can however not add their own posts.

## User Stories

The user is able to:
* enter the url to load the website
* view a grid of uploaded pics displayed in the root page
* cick on a particular photo to get its description as well as copy its url and share with friends.


## Prerequisites
To develop the application , youll need to preinstall a few application. including
* Python 3.6
* Django
* pip
* postgress

## Technologies Used
* python 3.6
* Django 
* postgress

## Setup Information
* Clone the application repository to your local machine .
* Create a new virtual environment and access the folder through your virtual amchine.
* access the code through your preffered code editor
* create your database and link it in the config.py
* run this on your terminal python3.6 manage.py server
* Once run, the project can be accessed on your localhost using the address: localhost:8000.

## BDD
|Behavior |Input |Output |
|:------------| :---------|:--------|
| user loads url on browser | user loads url on web browser | home page displayed and user can view a variety of uploaded pictures|
|user views description |user clicks on image |image details are displayed as well as the image itself via modal|
|copy image link |click on copy |images link is copied to clipboard and can be shared to other users|


## LICENSE
MIT License

Copyright (c) 2019 niklauspeter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact Information
For any enquiries email me at oriokiklaus@gmail.com or github username niklauspeter