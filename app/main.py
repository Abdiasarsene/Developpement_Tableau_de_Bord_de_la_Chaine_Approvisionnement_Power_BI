# Importation des librairies
from fastapi import FastAPI,HTTPException, Request, Depends
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
import mlflow.sklearn
import pandas as pd
from typing import Dict
from database import insert_data
from concurrent.futures import ThreadPoolExecutor
import mlflow.pyfunc
import logging

# ====== CONFIGURATION ======
class Setting(BaseSettings) : 
    mlflow_model_name : str = "logistic"
    mlflow_model_version : str = "2"
    max_workers : int = 5
    
    class Config: 
        env_file = ".env"
settings = Settings()

# ====== LOGGING ======
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ====== CREATION DE L'API =====
app = FastAPI(
    title= "API de Logistique",
    description="API pour prédire le statut de livraison",
    version="1.0.0",
    contact={
        "name": "Support Technique",
        "email": "support@logistick.com"
    },
)
# ====== EXECUTOR ======
executor = ThreadPoolExecutor(max_workers=settings.max_workers)

# ====== HOME ======
@app.get("/home")
async def homepage(): 
    return{"Status": "OK"}

# ====== SCHEME D'ENTREE ======
class LogistikData(BaseModel):
    Stock_Level : int = Field (..., lt=1000)
    Sales : int = Field(..., lt=1000)
    Transportation_Cost : float = Field(..., lt=1000)
    Region : str = Field(..., min_length=2, max_length=50)
    Delivery_Urgency : str = Field(..., min_length=2, max_length=(50))
    Estimated_Day : int = Field(..., ge=1, le=17)

# ====== CHARGEMENT DU MODELE PREDICTIF ======
async def get_model():
    try : 
        model = mlflow.pyfunc.load_model(f"models:/{settings.mlflow_model_name}/{settings.mlflow_model_version}")
        logger.info("Modèle Chargé ✅✅")
        return model
    except Exception as e : 
        logger.error(f"Erreur de chargement du modèle : {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur de chargement du modèle")

# ====== ENDPOINTS ======
@app.post("/v1/predict")
async def predict_logistic(
    request : Request,
    data : LogistikData,
    model : mlflow.pyfunc.PythonModel = Depends(get_model)
):
    try : 
        input_data = pd.DataFrame([data.dict()])
        prediction = model.predict(input_data)
        predicted_class = int(prediction[0])
        
        logistik_mapping ={
            0 : "On Time",
            1 : "Late"
        }
        
        message = f"Delivery Status : {logistik_mapping.get(predicted_class, 'Unknown')}"
        
        # Insertion asynchrone
        executor.submit(insert_data, data, message)
        logger.info("Prédiction et insertion réussies")
        
        return {"Deliver Status": message}
    
    except Exception as e: 
        logger.error(f"Erreur de prédiction: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erreur de prédiction : {str(e)}")