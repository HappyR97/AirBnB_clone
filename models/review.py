#!/usr/bin/python3

"""

This module defines Review class

"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inheriting from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
