from typing import Any
from app.server.database.collections import Collections
import app.server.database.services as model_service
from fastapi import APIRouter,Query,Path, Body, Request,Depends,HTTPException
from bson import json_util
from app.server.services.enumeration import location as location_services
from app.server.static import enums

router = APIRouter()
    
@router.get('/geolocation', summary='To get geo information about the target')
async def geo_location(ip_address:str = Query(...)):
    """
        Ex: IP : 8.8.8.8 
    """
    data = await location_services.geo_location(ip_address)
    return {"status": "SUCCESS", "data": data}