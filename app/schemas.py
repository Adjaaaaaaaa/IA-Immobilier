from pydantic import BaseModel, Field
from typing import Literal
"""
This module defines Pydantic schemas for the IA-Immobilier prediction API.

"""

class PredictRequest(BaseModel):
    surface_bati: float = Field(..., gt=0)
    nombre_pieces: int = Field(..., ge=0)
    type_local: Literal["Appartement", "Maison"]
    surface_terrain: float = Field(..., ge=0)
    nombre_lots: int = Field(..., ge=1)

class DynamicPredictRequest(BaseModel):
    ville: Literal["lille", "bordeaux"]
    features: PredictRequest

class PredictResponse(BaseModel):
    prix_m2_estime: float
    ville_modele: str
    model: str
