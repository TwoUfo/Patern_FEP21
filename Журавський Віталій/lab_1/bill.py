class Bill:
    def __init__(self, limit, currDebt):
        self._limit = limit
        self._currDebt = currDebt

    def check(self, amount):
        if amount <= self.limit:
            return True
        else:
            return False

    def changeLimit(self, amount):
        self.limit = amount

    def pay(self, amount):
        if self._currDebt - amount > 0:
            self._currDebt -= amount

    def add(self, amount):
        self._currDebt += amount

    @property
    def limit(self):
        return self._limit

    @property
    def currDebt(self):
        return self._currDebt

    @limit.setter
    def limit(self, newValue):
        self._limit = newValue

    @currDebt.setter
    def currDEbt(self, newValue):
        self._currDebt = newValue
