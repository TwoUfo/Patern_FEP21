from __future__ import annotations
class Bill:
  def __init__(self, customerID: int, currentDebt: float = 0, limitingAmount: int = 200) -> None:
    self.limitingAmount = limitingAmount
    self.customerID = customerID
    self.currentDebt = currentDebt
  
  def __str__(self) -> str:
    return f"{self.currentDebt}"

  def check(self):
    if self.currentDebt > self.limitingAmount:
      return False
    else:
      return True
  def add(self, amount: float) -> None:
    temp = self.currentDebt + amount
    if temp < self.limitingAmount:
      self.currentDebt += temp
      print(f"Add {temp} to debt")
    else:
      raise ValueError(f"You reached the limit. Operation is forbidden")
    
  def pay(self, amount: float) -> None:
    temp = self.currentDebt - amount
    if temp < 0:
      self.currentDebt = 0
    else:
      self.currentDebt = temp
    print(f"Customer {self.customerID} paid ${temp}")

  def changeTheLimit(self, amount: float) -> None:
    self.limitingAmount += amount
    print(f"Limit has been risen to {self.limitingAmount}")