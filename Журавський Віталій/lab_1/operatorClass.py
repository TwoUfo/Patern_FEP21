class Operator:
    def __init__(self, id, talkingCharge, messageCharge, networkCharge, discountCharge, discountMessageRate):
        self.id = id
        self._talkingCharge = talkingCharge
        self._messageCharge = messageCharge
        self._networkCharge = networkCharge
        self._discountRate = discountCharge
        self._discountMessageRate = discountMessageRate

    def calculateTalkingCost(self, minute, currCustomer):
        talkingCharge = self.talkingCharge*minute
        if currCustomer.age < 18 or currCustomer.age > 65:
            talkingCharge -= talkingCharge*self.discountRate

        return round(talkingCharge, 2)

    def calculateMessageCost(self, quantity, currCustomer, otherCustomer):
        messageCharge = self.messageCharge*quantity
        if currCustomer.operator.id == otherCustomer.operator.id:
            messageCharge -= messageCharge*self._discountMessageRate

        return round(messageCharge, 2)

    def calculateNetworkCost(self, amount):

        networkCharge = self._networkCharge
        return amount*networkCharge

    @property
    def talkingCharge(self):
        return self._talkingCharge

    @talkingCharge.setter
    def talkingCharge(self, newValue):
        self._talkingCharge = newValue

    @property
    def messageCharge(self):
        return self._messageCharge

    @messageCharge.setter
    def messageCharge(self, newValue):
        self._messageCharge = newValue

    @property
    def networkCharge(self):
        return self._networkCharge

    @networkCharge.setter
    def networkCharge(self, newValue):
        self._networkCharge = newValue

    @property
    def discountRate(self):
        return self._discountRate

    @discountRate.setter
    def discountRate(self, newValue):
        self._discountRate = newValue
