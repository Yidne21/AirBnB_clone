#!/usr/bin/python3
"""Defines the State class."""
import models
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new State."""
        super().__init__(**kwargs
