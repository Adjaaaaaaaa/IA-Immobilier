from fastapi import FastAPI
from .routes import router
from fastapi.responses import RedirectResponse
"""
main.py
This module initializes the FastAPI application for the ImmoPrice API, an API for price estimation.
- Imports FastAPI for API creation and management.
- Imports the API router from the local routes module.
- Imports RedirectResponse to handle HTTP redirects.
Attributes:
    app (FastAPI): The FastAPI application instance with metadata such as title, version, and description.
Routes:
    - "/" (GET): Redirects the root URL to the API documentation at "/docs".
    - Includes additional routes from the imported router.
Usage:
    Run this module to start the ImmoPrice API server.
"""


app = FastAPI(title="ImmoPrice API", version="1.0", description = "Bienvenue sur l'API d'estimation immobilière" )


app.include_router(router)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")
