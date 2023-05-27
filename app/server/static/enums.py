from enum import Enum

class OPTIONS(str,Enum):
    SIMPLE='SIMPLE'
    ALL='ALL'

class ScanOptions(str,Enum):
    ALL = 'ALL'
    SPECIFIC = 'SPECIFIC'