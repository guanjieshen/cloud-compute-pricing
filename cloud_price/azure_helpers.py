from typing import List
import requests
from cloud_price.constants.constants import (
    AZURE_REGIONS,
    AZURE_PRICE_URL,
    AZURE_VM_OS,
    AZURE_VM_PRICING_TYPES,
    AZURE_VM_TYPES,
)


"""
Validation functions - Should be used to verify it the input parameters are valid.
"""


class ValidationFactory(object):
    @staticmethod
    def validateRegion(region: str):
        if region not in AZURE_REGIONS:
            raise ValueError("Azure Region not supported")

    @staticmethod
    def validateVMPricingType(pricingType: str):
        if pricingType not in AZURE_VM_PRICING_TYPES:
            raise ValueError("Azure VM Pricing Type not supported")

    @staticmethod
    def validateVMType(type: str):
        if type not in AZURE_VM_TYPES:
            raise ValueError("Azure VM Type not supported")

    @staticmethod
    def validateOsType(os: str):
        os_list = ""
        if os not in AZURE_VM_OS:
            for os in AZURE_VM_OS:
                os_list += os + " "
            raise ValueError(
                f"Azure VM OS not supported. Please select from the following: {os_list}"
            )


"""
OData Query Builder
"""


class ODataFactory:
    def __init__(self, base_url=AZURE_PRICE_URL):
        self.base_url = base_url
        self.odata_url = self.base_url + "?$filter="

    def buildURI(self, filters: List[str]) -> str:
        return self.odata_url + self.applyANDFilters(filters)

    def submitQuery(self, uri: str):
        response = requests.get(uri)
        return response.json()

    def equalsFilter(self, param: str, value: str) -> str:
        return f"{param} eq '{value}'"

    def containsFilter(self, param: str, value: str) -> str:
        return f"contains({param},'{value}')"

    def applyANDFilters(self, filters: List[str]) -> str:
        filter_str = "("
        for filter in filters[:-1]:
            filter_str += filter + " and "

        filter_str += str(filters[-1]) + ")"
        return filter_str
