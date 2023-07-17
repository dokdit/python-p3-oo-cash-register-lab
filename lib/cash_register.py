class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items_list = []
        self.item_dict = dict()

    def add_item(self, title, value, quantity=1):
        self.total += value * quantity
        self.items_list.extend([title] * quantity)
        self.item_dict[title] = [value, quantity]

    def apply_discount(self):
        if self.discount > 0:
            self.total = (100 - self.discount) / 100 * self.total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    @property
    def items(self):
        return self.items_list

    def void_last_transaction(self):
        if self.items_list:
            last_item = self.items_list.pop()
            last_item_info = self.item_dict.pop(last_item)
            last_item_value = last_item_info[0] * last_item_info[1]
            self.total -= last_item_value
        else:
            print("No items to void.")
        return self.total
