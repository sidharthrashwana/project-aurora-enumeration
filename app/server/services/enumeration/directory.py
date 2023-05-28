from datetime import datetime
import os
import re
import subprocess
from fastapi import UploadFile
from app.server.database.collections import Collections
from app.server.database import services as core_services
from app.server.logger.custom_logger import logger
from app.server.static import enums
from threading import Thread
from app.server.utils import pdf_utils
#import concurrent.futures
import asyncio
from pydantic import HttpUrl

current_file_path = os.path.abspath(__file__)
current_file_parent = os.path.dirname(current_file_path)
current_file_grandparent = os.path.dirname(current_file_parent)
current_file_great_grandparent = os.path.dirname(current_file_grandparent)

def sys_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

async def directory_bruteforce(target:HttpUrl,port:int):
    try :
        port_regex = re.compile(r'^(80|443)$')
        if not port_regex.match(str(port)):
            raise ValueError("Invalid port. Port must be either 80 or 443.")
        host=f"{target}:{port}/FUZZ/"
        dictionary = os.path.join(current_file_great_grandparent, 'dictionary', 'directory-list-2.3-medium.txt')
        logger.debug('kill existing all instances of wfuzz')
        process = sys_cmd('killall wfuzz')
        logger.debug('starting directory bruteforcing dns scan')
        cmd=f"wfuzz -u {host} -w {dictionary} --hl 0 -R 3 -v -f ./reports/enumeration/directory/wfuzz/directory_bruteforce.html,html"
        process =  sys_cmd(cmd)
        logger.debug(f"Process finished")
        return {'message':'Directory Bruteforce is running in background.'}
    except Exception as e:
        raise Exception(str(e))
