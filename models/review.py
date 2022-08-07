#!/usr/bin/python3
"""Defines the Review class."""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
    """Initialize a new Review."""
    super().__init__(**kwargs)
