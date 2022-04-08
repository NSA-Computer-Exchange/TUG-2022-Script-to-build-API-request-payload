#######  Build an IDM api request Payload #######
#
#  Author: Rob Thayer
#  Date: Arpil 1 2022
#
#################################################

import xml.etree.ElementTree as ET
import json
from typing import List

class DataInput:
    def __init__(self):
        self.entity = "Purchase_Order"
        self.keyattr = "Purchase_Order_Number"
        self.operator = "="
        self.textSearch = False
        self.logicalType = ""

    def getPO(self):
        with open("Sync.PurchaseOrder.xml") as INPUT:
            root = ET.parse(INPUT)
            ns = {'xs': 'http://schema.infor.com/InforOAGIS/2'}
            poNo = root.find(".//xs:DataArea/xs:PurchaseOrder/xs:PurchaseOrderHeader/xs:DocumentID/xs:ID", ns)
            if poNo is not None:
                pono = poNo.text[:-3] 
            else:
                pono = poNo.text
        return pono     

class Query(object):
    def __init__(self, query: str):
        self.query = query       

class Queries(object):
    def __init__(self, queries: List[Query]):
        self.queries = queries

class QueryKeys(object):
    def __init__(self,entities: str, useTextSearch: str, arguments: str):
        self.entities = entities
        self.useTextSearch = useTextSearch
        self.arguments = arguments

class ArgumentKeys(object):
    def __init__(self, key: str, operator: str, value: str, logicalType: str): 
        self.key = key
        self.operator = operator
        self.value = value
        self.logicalType = logicalType

class ArgumentsArg(object):
    def __init__(self, argument: List[ArgumentKeys]):
        self.argument = argument               

class Request:
    def payload():
        params = DataInput()
        argKeys = ArgumentKeys(key=params.keyattr,operator=params.operator,value=params.getPO(),logicalType=params.logicalType)
        argsArg = ArgumentsArg([argKeys])
        queryKeys = QueryKeys(entities=params.entity,useTextSearch=params.textSearch, arguments=argsArg)
        query = Query(query=[queryKeys])
        result = Queries(queries=query)
        return result

def getIDMItem(result: str):
    result = json.dumps(result, default=lambda o: o.__dict__, indent=4)
    print(result)

getIDMItem(Request.payload())
