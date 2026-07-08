Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:/Users/Abhinaya/OneDrive/Desktop/python/variables.py =======
Assign Multiple values to multiple variables
140705002546376 140705002546696 140705002547016
Assign Single value to Multiple variables
140705002546376 140705002546376 140705002546376
>>> 
>>> print(bool(1))
True
>>> print(bool("hi"))
True
>>> a,b=20,30
>>> a,b=b,a
>>> 
>>> 
>>> a,b=10,20
>>> print(id(a), id(b))
140705002546376 140705002546696
>>> a,b=b,a
>>> print(id(a), id(b))
140705002546696 140705002546376
>>> print(a,b)
20 10
