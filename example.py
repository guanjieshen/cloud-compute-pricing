import json
from cloud_price.azure import AzureVMs

standard_l8v2_uswest2 = AzureVMs("US West 2", "Standard_L8s_v2")
standard_l8v2_uswest2_spot = standard_l8v2_uswest2.getSpotPrice()
print(f"SKU Name: {standard_l8v2_uswest2_spot.skuName}")
print(f"Unit Price: {standard_l8v2_uswest2_spot.unitPrice}")
print(f"Price Effective Date: {standard_l8v2_uswest2_spot.effectiveStartDate}")

standard_l8_uswest2 = AzureVMs("US West 2", "Standard_L8s")
standard_l8_uswest2_spot = standard_l8_uswest2.getSpotPrice()
print(f"SKU Name: {standard_l8_uswest2_spot.skuName}")
print(f"Unit Price: {standard_l8_uswest2_spot.unitPrice}")
print(f"Price Effective Date: {standard_l8_uswest2_spot.effectiveStartDate}")
