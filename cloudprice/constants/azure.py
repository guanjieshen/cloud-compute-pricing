from .constants_helper import Enum


AZURE_PRICE_URL = "https://prices.azure.com/api/retail/prices"

AZURE_REGIONS = ["US West 2", "US West"]

AZURE_VM_PRICING_TYPES = ["Consumption", "DevTestConsumption", "Reservation"]

AZURE_VM_TYPES = ["Standard", "Spot", "LowPriority"]

AZURE_VM_OS = ["Windows", "Linux"]

# AZURE_VM_RESERVATION_TERMS = ["1YR", "3YR"]

AZURE_VM_RESERVATION_TERMS = Enum(ONE_YEAR="1 Year", THREE_YEAR="3 Years")
