from cloudprice.azure.azure_helpers import ValidationFactory
import pytest

from cloudprice.constants.azure import AZURE_VM_RESERVATION_TERMS


class TestAzureHelpers(object):
    def setup(self):
        self.azure_validation_factory = ValidationFactory()

    def test_invalid_reservation_terms(self):
        print(AZURE_VM_RESERVATION_TERMS.values())
        print(AZURE_VM_RESERVATION_TERMS.ONE_YEAR)
        # with pytest.raises(ValueError) as error_message:
        #     self.azure_validation_factory.validateReservationTerm("one_year")

        # assert error_message.value == "error"
