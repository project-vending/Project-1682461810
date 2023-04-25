
from fastapi import FastAPI

app = FastAPI()

# Import the main endpoints
from .main import (
    get_recommendations
)

