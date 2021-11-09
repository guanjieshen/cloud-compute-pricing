from cloud_price.azure_helpers import ODataFactory, validateRegion, validateVMType


class AzureVMs:
    def __init__(self):
        self.odata_factory = ODataFactory()
        self.defaultFilters = [
            self.odata_factory.equalsFilter("serviceName", "Virtual Machines")
        ]

    def urlBuilder(self, filters):
        return self.base_url + "?$filter=" + filters

    def getVMPrices(
        self, region: str, arm_sku_name: str, type="Consumption", is_spot=False
    ):
        validateRegion(region)
        validateVMType(type)
        filters = self.defaultFilters
        filters.extend(
            [
                self.odata_factory.equalsFilter("armSkuName", arm_sku_name),
                self.odata_factory.equalsFilter("location", region),
                self.odata_factory.equalsFilter("priceType", type),
            ]
        )
        request_uri = self.odata_factory.buildURI(filters)
        print(request_uri)
        response = self.odata_factory.submitQuery(request_uri)
        return response
