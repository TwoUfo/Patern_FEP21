def GoldenCreditCard(cls):
    class GoldenCreditCardDecorator(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.golden_benefits = True

        def apply_golden_discount(self):
            pass

    return GoldenCreditCardDecorator


def VIPCustomer(cls):
    class VIPCustomerDecorator(cls):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.vip_status = True

        def access_vip_lounge(self):
            pass

    return VIPCustomerDecorator
