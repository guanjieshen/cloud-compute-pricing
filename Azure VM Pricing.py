# Databricks notebook source
list_of_regions = ["US West 2", "US West"]
list_of_vm_types = []

# COMMAND ----------

class AzureVMs:
  def __init__(self):
    self.base_url = "https://prices.azure.com/api/retail/prices"
    self.odata_url = self.base_url + "?$filter="
    
  def getAllVMPricing(self, region: str, arm_sku_name: str):
    spot_pricing_query = "(serviceName eq 'Virtual Machines' and armSkuName eq '{}' and location eq '{}')".format(arm_sku_name, region)
    
    request_url = self.odata_url + spot_pricing_query
    r =requests.get(self.odata_url + spot_pricing_query)
    return r.json()["Items"]
    


# COMMAND ----------

azure = AzureVMs()
from pyspark.sql.functions import *
vm_price  = azure.getAllVMPricing("US West 2", "Standard_L8s_v2")

df = spark.createDataFrame(vm_price)
display(df.withColumn("effectiveStartDate",to_timestamp("effectiveStartDate")))
  

# COMMAND ----------

import requests
r =requests.get("https://prices.azure.com/api/retail/prices?$filter=(serviceName eq 'Virtual Machines' and contains(skuName, 'L4s') and location eq 'US West 2' and  contains(skuName, 'Spot'))")
r.json()

# COMMAND ----------

# MAGIC %pip install azure-identity

# COMMAND ----------

from azure.identity import DeviceCodeCredential

def prompt(url, user_code, _):
    print("opening a browser to '{}', enter device code {}".format(url, user_code))
    
credential = DeviceCodeCredential(prompt_callback=prompt, timeout=40)
credential.get_token()

# COMMAND ----------

from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
print(credential)

# COMMAND ----------

https://prices.azure.com/api/retail/prices?$filter=(serviceName eq 'Virtual Machines' and skuName eq 'E2ads v5 Low Priority')
