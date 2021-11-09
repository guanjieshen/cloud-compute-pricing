import json
from typing import List
from cloud_price.azure_helpers import ODataFactory, ValidationFactory
from types import SimpleNamespace


class AzureVMs:
    def __init__(self, region: str, arm_sku_name: str):
        self.vm_price_list = []
        self.odata_factory = ODataFactory()
        self.defaultFilters = [
            self.odata_factory.equalsFilter("serviceName", "Virtual Machines")
        ]
        self.getVMPrices(region, arm_sku_name)

    def __filterForOs(self, list_of_prices: List[object], os: str) -> List[object]:
        ValidationFactory.validateOsType(os)
        if os == "Linux":
            return filter(lambda x: "Windows" not in x.productName, list_of_prices)
        else:
            return filter(lambda x: "Windows" in x.productName, list_of_prices)

    def getVMPrices(self, region: str, arm_sku_name: str):
        ValidationFactory.validateRegion(region)

        filters = self.defaultFilters
        filters.extend(
            [
                self.odata_factory.equalsFilter("armSkuName", arm_sku_name),
                self.odata_factory.equalsFilter("location", region),
            ]
        )
        # if type == "Spot":
        #     filters.append(self.odata_factory.containsFilter("skuName", "Spot"))
        # elif type == "LowPriority":
        #     filters.append(self.odata_factory.containsFilter("skuName", "Low Priority"))

        request_uri = self.odata_factory.buildURI(filters)

        response = self.odata_factory.submitQuery(request_uri)
        # TODO: Check to see if there is any need to paginate. Field to check is response["NextPageLink"]

        items = response["Items"]

        self.vm_price_list = []
        for item in items:
            x = json.dumps(item)
            self.vm_price_list.append(
                json.loads(x, object_hook=lambda d: SimpleNamespace(**d))
            )

    def getSpotPrice(self, os="Linux"):
        os_filtered_list = self.__filterForOs(self.vm_price_list, os)
        spot_price = list(filter(lambda x: "Spot" in x.skuName, os_filtered_list))[0]
        return spot_price
