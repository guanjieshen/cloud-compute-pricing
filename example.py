from cloud_price.azure import AzureVMs

azure_pricing = AzureVMs()
azure_pricing.getVMPrices("US West 2", "Standard_L8s_v2")
