import json
from cloud_price.azure import AzurePrice, AzureVM

standard_l8v2_uswest2 = AzureVM("US West 2", "Standard_L8s_v2")

standard_l8v2_uswest2_spot = standard_l8v2_uswest2.getSpotPrice()
print(f"SKU Name: {standard_l8v2_uswest2_spot.sku_name}")
print(f"Unit Price: {standard_l8v2_uswest2_spot.unit_price}")
print(f"Price Effective Date: {standard_l8v2_uswest2_spot.effective_start_date}")

standard_l8_uswest2 = AzureVM("US West 2", "Standard_L8s")
standard_l8_uswest2_spot = standard_l8_uswest2.getSpotPrice()
print(f"SKU Name: {standard_l8_uswest2_spot.sku_name}")
print(f"Unit Price: {standard_l8_uswest2_spot.unit_price}")
print(f"Price Effective Date: {standard_l8_uswest2_spot.effective_start_date}")
