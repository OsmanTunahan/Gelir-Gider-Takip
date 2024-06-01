import os

class Config:
    DATABASE_HOST = os.environ.get('DATABASE_HOST') or 'localhost'
    DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'gelirgider'
    DATABASE_USER = os.environ.get('DATABASE_USER') or 'root'
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD') or ''