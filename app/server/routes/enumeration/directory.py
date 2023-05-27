from typing import Any
from app.server.database.collections import Collections
import app.server.database.services as model_service
from fastapi import APIRouter,Query,Path, Body, Request,Depends,HTTPException
from bson import json_util
from app.server.services.enumeration import directory as directory_services
from app.server.static import enums
from pydantic import HttpUrl

router = APIRouter()
    
@router.get('/directory-bruteforce', summary='To get list of subdirectory on target')
async def directory_bruteforce(target:HttpUrl = Query(...) , port:int = Query(...)):
    """

    Ex-1 :
        target : http://www.google.com
        port : 80 

    Ex-2:
        target:https://www.google.com
        port : 443
    
    """
    
    data = await directory_services.directory_bruteforce(target,port)
    return {"status": "SUCCESS", "data": data}