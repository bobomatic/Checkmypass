# Checkmypass
Check if your password has ever been hacked

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Examples of Use](#examples-of-use)
* [Status](#status)
* [Sources](#sources)

## General Info
This project determines whether a password provided by the user has ever been hacked. From the command line the user provides a list of passwords. The first 5 chars of the SHA1 hashed password is sent to the 'pwned' password database which responds with SHA1 tails with leak count > 0.

## Technologies
This project is created with

Python 3.8

hashlib

requests - http requests

## Setup
To run this project install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

## Features
* check multiple passwords against the Pwned hash database
* Secure checking of passwords (only shares first 5 characters of SHA1 hashed password)

### To do:
NA

## Examples of Use

Usage: 

python3 checkmypass.py password1 password_2 "!password3"

Code example:

Command line
`$ python3 checkmypass.py paswwword123`

## Status
Complete

## Sources
This project is inspired by Andrei Neagoie Python Zero to Mastery course:

https://www.udemy.com/course/complete-python-developer-zero-to-mastery
