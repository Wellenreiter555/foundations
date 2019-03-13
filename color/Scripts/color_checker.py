#!/usr/bin/python

# A simple script to accept input from an html form,
# parse the information, and do something - which in this case
# is to give user feedback with a simple html page.

# use python's the CGI package
import cgi
import sys
import csv

# get the output of the form.
form = cgi.FieldStorage()

# get an input filed from the form called 'user_color'
# and assign it's value to a local variable called user_color
user_color = form.getvalue('color')

with open('colors.csv') as _filehandler:
    csv_file_reader = csv.reader(_filehandler)
    check = False
    for row in csv_file_reader:
        if user_color.title() == row[1]:
        	check = True
        	break
    if check == True:
    	print("""
    		<!DOCTYPE html>
			<html>
			<head>
			<style>
			p {
				font-family: Courier New;
				font-size: 30px;
				color: %s;
				filter: invert(1);
			}
			#big{
				font-size: 120px;
			}
			</style>
			<title> Hey Adam </title>
			</head>
			<body style="background-color:%s">
			<br><br><br><br><br><br><br><br><br><br><br><br>
			<center>
			<p> %s is a valid color! The Hexcode is: %s </p>
			<p> The color of this text is the complementary of the Backgroundcolor.
			<p>#WhenYourCodeGameIsStrong!</p>
			<br><p> what do you think Adam?</p>
			</center>
			</body>
			</html>
    		"""%(row[2], row[2], user_color, row[2]))
    if check == False:
    	print("""
    		<!DOCTYPE html>
			<html>
			<head>
			<style>
			div.container {
  				border: 2px solid black;
  				width: 200px;
			}
			</style>
			<title> Server Answer </title>
			</head>
			<body>
			<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
			<center>
			<div class="container">
			<p> %s is not a valid color.</p>
			<p id="big"> Sorry, bro</p>
			</div>
			</center>
			</body>
			</html>
    		"""% user_color)