from datetime import datetime
import os
import subprocess
from app.server.database.collections import Collections
from app.server.database import services as core_services
from app.server.logger.custom_logger import logger
from app.server.static import enums

current_file_path = os.path.abspath(__file__)
current_file_parent = os.path.dirname(current_file_path)
current_file_grandparent = os.path.dirname(current_file_parent)
current_file_great_grandparent = os.path.dirname(current_file_grandparent)

def sys_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def indepth_dns(host):
    try:
        logger.debug('starting indepth dns scan')
        dictionary = os.path.join(current_file_great_grandparent, 'dictionary', 'directory-list-2.3-medium.txt')
        cmd = f"dnsrecon -d {host} -D {dictionary} -t std,rvl,srv,axfr,bing,yand,crt,snoop,tld,zonewalk -v --threads 75 > ./reports/domain/indepth_scan.log"
        process =  sys_cmd(cmd)
        logger.debug(f"Process finished")
    except Exception as e:
        raise Exception(str(e))
    
async def domain_info(host:str,options):
    try :
        logger.debug('starting normal dns scan')
        cmd=f"dnsrecon -d {host} > ./reports/enumeration/domain/domain_info.log"
        process = sys_cmd(cmd)
        if options == enums.OPTIONS.ALL:
            indepth_dns(host)
        return {'message':'Domain Scan is running in background.'}
    except Exception as e:
        raise Exception(str(e))