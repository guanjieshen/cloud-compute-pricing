from typing import List
import requests
from cloud_price.constants.constants import (
    AZURE_REGIONS,
    AZURE_PRICE_URL,
    AZURE_VM_TYPES,
)


"""
Validation functions - Should be used to verify it the input parameters are valid.
"""


class ValidationFactory(object):
    @staticmethod
    def validateRegion(region: str):
        if region not in AZURE_REGIONS:
            raise ValueError("Azure VM Type not supported")

    @staticmethod
    def validateVMType(region: str):
        if region not in AZURE_VM_TYPES:
            raise ValueError("Azure Region not supported")


"""
OData Query Builder
"""


class ODataFactory:
    def __init__(self):
        self.base_url = AZURE_PRICE_URL
        self.odata_url = self.base_url + "?$filter="

    def buildURI(self, filters: List[str]) -> str:
        return self.odata_url + self.applyANDFilters(filters)

    def submitQuery(self, uri: str):
        response = requests.get(uri)
        # Extract only the items object from the payload
        object = response.json()["Items"]
        print(object)

    def equalsFilter(self, param: str, value: str) -> str:
        return f"{param} eq '{value}'"

    def applyANDFilters(self, filters: List[str]) -> str:
        filter_str = "("
        print(filters)
        for filter in filters[:-1]:
            filter_str += filter + " and "

        filter_str += str(filters[-1]) + ")"
        return filter_str
