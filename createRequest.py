#######  Build an IDM api request Payload #######
#
#  Author: Rob Thayer
#  Date: Arpil 1 2022
#
#################################################

import xml.etree.ElementTree as ET
import json
from typing import List
import io

class DataInput:
    @staticmethod
    def getPO():
        with open("Sync.PurchaseOrder.xml") as INPUT:
            root = ET.parse(INPUT)
            # Set the default namespace object
            ns = {'xs': 'http://schema.infor.com/InforOAGIS/2'}
            # Purchase Order Number# is a static value and will be added to each line item under the poNo column
            poNo = root.find(".//xs:DataArea/xs:PurchaseOrder/xs:PurchaseOrderHeader/xs:DocumentID/xs:ID", ns)
            if poNo is not None:
                pono = poNo.text[:-3] 
            else:
                pono = poNo.text
            return pono     

''' IDM entity or Document Type '''
entity = "Invoice"
''' Attribute or Property '''
keyattr = "Order_Number"
''' Operator like = > < etc. '''
operator = "="
''' Set boolean value'''
textSearch = False
''' Set Purchase Order Number '''
inputdata = DataInput()
keyvalue = inputdata.getPO()


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


argKeys = ArgumentKeys(key=keyattr,operator=operator,value=keyvalue,logicalType="string")
argsArg = ArgumentsArg([argKeys])
queryKeys = QueryKeys(entities=entity,useTextSearch=textSearch, arguments=argsArg)
query = Query(query=[queryKeys])
result = Queries(queries=query)

json_result = json.dumps(result, default=lambda o: o.__dict__, indent=4)

print(json_result)

