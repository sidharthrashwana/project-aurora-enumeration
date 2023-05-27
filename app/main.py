#import metadata for API
from app.server.document.api_meta_data import TAGS_META_DATA
#for error handling
from app.server.handler.error_handler import (
    CustomException,
    catch_exceptions_middleware,
    custom_exception_handler,
    http_exception_handler,
    validation_exception_handler
)
#for logging
from app.server.logger.custom_logger import logger
#import routes
from app.server.routes.enumeration.domain import router as domain_router
from app.server.routes.enumeration.location import router as location_router
from app.server.routes.enumeration.vulnerability import router as vulnerability_router
from app.server.routes.enumeration.directory import router as directory_router

#date related operations
from app.server.utils import date_utils
#implement fastAPI
from fastapi import FastAPI
#exception to validate error
from fastapi.exceptions import RequestValidationError
#before request and after response
'''
CORSMiddleware is used to enable Cross-Origin Resource Sharing (CORS) for your FastAPI application. 
CORS is a security feature implemented by web browsers that prevents web pages from making requests to a different domain 
than the one that served the original page. This middleware adds the necessary headers to allow cross-origin requests to 
be made to your FastAPI application from different domains.
'''
from fastapi.middleware.cors import CORSMiddleware
'''
GZipMiddleware is used to enable gzip compression of HTTP responses sent from your FastAPI application. 
Gzip compression can significantly reduce the size of response data, resulting in faster transfer times and reduced bandwidth usage. 
This middleware automatically compresses response data if the requesting client supports gzip compression.
'''
from fastapi.middleware.gzip import GZipMiddleware

from fastapi.responses import ORJSONResponse
from starlette.exceptions import HTTPException

app=FastAPI(openapi_tags=TAGS_META_DATA , default_response_class=ORJSONResponse ,title='AURORA')

# add routes
app.include_router(domain_router, tags=['Domain'], prefix='/enumeration/domain')
app.include_router(location_router, tags=['Geolocation'], prefix='/enumeration/location')
app.include_router(vulnerability_router, tags=['Vulnerability'], prefix='/enumeration/vulnerability')
app.include_router(directory_router, tags=['Directory'], prefix='/enumeration/directory')

# add exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(CustomException, custom_exception_handler)
# add middlewares
app.middleware('http')(catch_exceptions_middleware)
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

#log when application start
@app.on_event('startup')
async def startup_event():
    logger.debug(f'Application Started: {str(date_utils.get_current_date_time())}')

#log when application shutdown
@app.on_event('shutdown')
def shutdown_event():
    logger.debug(f'App shutdown: {str(date_utils.get_current_date_time())}')

#welcome message
@app.get('/', tags=['Root'])
async def read_root():
    return {'message': 'Welcome to Core Layer'}