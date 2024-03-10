#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage.py import FileStorage


storage = FileStorage()
storage.reload()
