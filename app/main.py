from fastapi import FastAPI
from .routes import router
from fastapi.responses import RedirectResponse

app = FastAPI(title="ImmoPrice API", version="1.0", description = "Bienvenue sur l'API d'estimation immobilière" )

app.include_router(router)

@app.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")
