from datetime import datetime
import os
import subprocess
from fastapi import UploadFile
from app.server.database.collections import Collections
from app.server.database import services as core_services
from app.server.logger.custom_logger import logger
from app.server.static import enums
import requests
import os
import re
from dotenv import load_dotenv
load_dotenv()

IPAPI_KEY = os.getenv('IPAPI_KEY')
    
async def geo_location(ip_address:str):
    pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_address = ''.join(re.findall(pattern, ip_address))
    response = requests.get(f"https://ipapi.co/{ip_address}/json/?key={IPAPI_KEY}").json()
    latitude= str(response.get("latitude"))
    longitude=str(response.get("longitude"))
    if latitude and longitude != 'None':
        location_data = {"ip": ip_address,
                         "network":response.get("network"),
                         "version":response.get("version"),
                         "region":response.get("region"),
                         "city": response.get("city"),
                         "country": response.get("country_name"),
                         "longitude": response.get("longitude"),
                         "latitude": response.get("latitude"),
                         "timezone": response.get("timezone"),
                         "isp": response.get("isp"),
                         "org": response.get("org"),
                         "asn": response.get("asn"),
                         "proxy": response.get("proxy"),
                         "country_code": response.get("country_code"),
                         "threat_level": response.get("threat_level")}
        return location_data
    else:
        msg="Latitude or longitude not found due to invalid IP address or Rate Limit."
        raise Exception(msg)