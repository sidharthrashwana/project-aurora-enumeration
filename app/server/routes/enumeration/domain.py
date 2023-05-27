from typing import Any
from app.server.database.collections import Collections
import app.server.database.services as model_service
from fastapi import APIRouter,Query,Path, Body, Request,Depends,HTTPException
from bson import json_util
from app.server.services.enumeration import domain as domain_services
from app.server.static import enums

router = APIRouter()
    
@router.get('/domain-info', summary='To get domain information about the target')
async def get_domain_info(options:enums.OPTIONS,target:str = Query(...)):
    """
     Ex : google.com (without protocol)
    """
    data = await domain_services.domain_info(target,options)
    return {"status": "SUCCESS", "data": data}