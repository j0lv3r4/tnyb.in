import os

DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY', '<secret key>')
SALT = os.getenv('SALT', '<salt>')

DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///tnybin.sqlite')

HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', 8088)
