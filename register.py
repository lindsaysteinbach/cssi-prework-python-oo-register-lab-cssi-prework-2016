class CashRegister:
  def __init__(self, discount = 0):
    self.total = 0
    self.items = []
    self.discount = discount
    self.transaction = 0
    self.value = 0

  def add_item(self, title, price, quantity=1):

    self.transaction = quantity
    self.value = price * quantity

    for x in range (0, quantity):
      self.items.append(title)

    self.total += (price * quantity)



  def apply_discount(self):
    if self.discount == 0:
      return "There is no discount to apply."
    else:
      self.total = self.total - (self.total * (self.discount *.01))
      return "After the discount, the total comes to ${:.2f}.".format(self.total)

  def void_last_transaction(self):

    self.total = self.total - self.value

    self.items = self.items[0:len(self.items)-self.transaction]







