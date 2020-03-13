a = 30
b = 45
c = a * b
d = a + b
e = c - d
# print('reaching 1275 by perfroming art operation using 20 and 45' , e)

'''
a = 58
b = 670
c = a + b
d = c + c + c #2184
'''
e = a + a 
f = d + e

Microsoft Windows [Version 6.3.9600]
(c) 2013 Microsoft Corporation. All rights reserved.

C:\Users\Nilanjana Bala>python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (In
tel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> lang = 'python'
>>> latest_version = 3.8
>>> print('current version of python is', latest_version)
current version of python is 3.8
>>> prin(latest_version+0.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prin' is not defined
>>> print(latest_version+0.1)
3.9
>>> print('current version of python is'+ latest_version + 0.1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str
>>> print(10+1.23)
11.23
>>> a = 30
>>> b = 45
>>> c = a * b
>>> d = a + b
>>> e = c - d
>>> print('reaching 1275 by perfroming art operation using 20 and 45' , e)
reaching 1275 by perfroming art operation using 20 and 45 1275
>>> print(e)
1275
>>> f = 'hi i am' + 1275
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> f = 'hi i am' , 1275
>>> print(f)
('hi i am', 1275)
>>> f = 'hi i am at {}'.format(e)
>>> print(f)
hi i am at 1275
>>> name = prasanna
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'prasanna' is not defined
>>> name = 'prasanna'
>>> city = 'bangalore'
>>> pincode = 560068
>>> person_bio ='{} is staying {} and the area pincode is {}'.foramt(name,city,p
incode)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'foramt'
>>> person_bio ='{} is staying {} and the area pincode is {}'.format(name,city,p
incode)
>>> person_bio ='{0} is staying {1} and the area pincode is {2}'.format(name,cit
y,pincode)
>>> person_bio ='{name} is staying {city} and the area pincode is {pincode}'.for
mat(name,city,pincode)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'name'
>>> person_bio =f'{name} is staying {city} and the area pincode is {pincode}'.fo
rmat(name,city,pincode)
>>> print(person_bio)
prasanna is staying bangalore and the area pincode is 560068
>>> person_bio =f'{name} is staying {city} and the area pincode is {pincode}'
>>> print(person_bio)
prasanna is staying bangalore and the area pincode is 560068
>>>
>>> ^A^A^A^