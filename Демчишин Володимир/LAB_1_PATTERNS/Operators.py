class Operator:
    def __init__(self, id: int, talkingCharge: float, messageCharge: float,
                 networkCharge: float, discountCharge: float, discountMessageRate: float) -> None:
        self.id = id
        self.talkingCharge = talkingCharge
        self.messageCharge = messageCharge
        self.networkCharge = networkCharge
        self.discountRate = discountCharge
        self.discountMessageRate = discountMessageRate

    def calculateTalkingCost(self, minute: float, first_customer) -> float:
        # TODO: Calculate talk cost
        talkingCharge = self.talkingCharge*minute
        if first_customer.age < 18 or first_customer.age > 65:
            talkingCharge -= talkingCharge*self.discountRate

        return round(talkingCharge, 2)

    def calculateMessageCost(self, quantity: float, first_customer, second_customer) -> float:
        # TODO: Calculate massage cost
        messageCharge = self.messageCharge*quantity
        if first_customer.operator.id == second_customer.operator.id:
            messageCharge -= messageCharge*self.discountMessageRate
        return round(messageCharge, 2)

    def calculateNetworkCost(self, amount: float) -> float:
        # TODO: Calculate network cost
        networkCharge = self.networkCharge
        return amount*networkCharge

