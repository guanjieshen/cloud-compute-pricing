import json
from typing import List
from cloud_price.azure_helpers import ODataFactory, ValidationFactory
from cloud_price.prices import AzurePrice


class AzureVM:
    def __init__(self, region: str, arm_sku_name: str):
        self.vm_price_list: List[AzurePrice] = []
        self.odata_factory = ODataFactory()
        self.defaultFilters = [
            self.odata_factory.equalsFilter("serviceName", "Virtual Machines")
        ]
        self.getVMPrices(region, arm_sku_name)

    def __filterForOs(self, list_of_prices: List[AzurePrice], os: str) -> List[object]:
        ValidationFactory.validateOsType(os)

        if os == "Linux":
            return filter(lambda x: "Windows" not in x.product_name, list_of_prices)
        else:
            return filter(lambda x: "Windows" in x.product_name, list_of_prices)

    def getVMPrices(self, region: str, arm_sku_name: str):
        ValidationFactory.validateRegion(region)

        filters = self.defaultFilters
        filters.extend(
            [
                self.odata_factory.equalsFilter("armSkuName", arm_sku_name),
                self.odata_factory.equalsFilter("location", region),
            ]
        )

        request_uri = self.odata_factory.buildURI(filters)

        response = self.odata_factory.submitQuery(request_uri)
        # TODO: Check to see if there is any need to paginate. Field to check is response["NextPageLink"]

        response_items = response["Items"]

        self.vm_price_list = []
        for item in response_items:
            x = json.dumps(item)
            price_dict = json.loads(x)
            price_object = AzurePrice(**price_dict)
            self.vm_price_list.append(price_object)

    def getSpotPrice(self, os="Linux"):
        os_filtered_list: List[AzurePrice] = self.__filterForOs(self.vm_price_list, os)
        spot_price: AzurePrice = list(
            filter(lambda x: "Spot" in x.sku_name, os_filtered_list)
        )[0]
        return spot_price
