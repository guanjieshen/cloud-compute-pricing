from cloudprice.azure import AzureVM
from cloudprice.constants.azure import AZURE_VM_RESERVATION_TERMS

# Get Azure VM Pricing
example_vm = AzureVM("US West", "Standard_E8_v3")

# Get Azure VM Pricing for On Demand Instance
example_vm_standard = example_vm.getLatestPrice()
print(
    f"""
Product Name: {example_vm_standard.product_name}
Meter Name: {example_vm_standard.meter_name}
Location: {example_vm_standard.location}
Effective Date: {example_vm_standard.effective_start_date}
Unit Price: {example_vm_standard.unit_price}
"""
)

# Get Azure VM Pricing for D13 v2 Linux Spot Instance
example_vm_spot = example_vm.getLatestPrice(vm_type="Spot")
print(
    f"""
Product Name: {example_vm_spot.product_name}
Meter Name: {example_vm_spot.meter_name}
Location: {example_vm_spot.location}
Effective Date: {example_vm_spot.effective_start_date}
Unit Price: {example_vm_spot.unit_price}
"""
)

# Get Azure VM Pricing for D13 v2 Windows Instance
example_vm_windows_spot = example_vm.getLatestPrice(os="Windows")
print(
    f"""
Product Name: {example_vm_windows_spot.product_name}
Meter Name: {example_vm_windows_spot.meter_name}
Location: {example_vm_windows_spot.location}
Effective Date: {example_vm_windows_spot.effective_start_date}
Unit Price: {example_vm_windows_spot.unit_price}
"""
)

# Get Azure VM Pricing for 1 year reservation
example_vm_res_1yr = example_vm.getLatestPrice(vm_pricing_type="Reservation")
print(
    f"""
Product Name: {example_vm_res_1yr.product_name}
Reservation Term: {example_vm_res_1yr.reservation_term}
Location: {example_vm_res_1yr.location}
Effective Date: {example_vm_res_1yr.effective_start_date}
Unit Price: {example_vm_res_1yr.unit_price}
Retail Price: {example_vm_res_1yr.retail_price}
"""
)

# Get Azure VM Pricing for 3 year reservation
example_vm_res_3yr = example_vm.getLatestPrice(
    vm_pricing_type="Reservation",
    reservation_term=AZURE_VM_RESERVATION_TERMS.THREE_YEAR,
)
print(
    f"""
Product Name: {example_vm_res_3yr.product_name}
Reservation Term: {example_vm_res_3yr.reservation_term}
Location: {example_vm_res_3yr.location}
Effective Date: {example_vm_res_3yr.effective_start_date}
Unit Price: {example_vm_res_3yr.unit_price}
Retail Price: {example_vm_res_3yr.retail_price}
"""
)

# # # Get Azure VM Pricing for something that doesn't exist
try:
    example_vm_error = example_vm.getLatestPrice(vm_pricing_type="DevTestConsumption")
    print(example_vm_error)
except ValueError as e:
    print(e)
