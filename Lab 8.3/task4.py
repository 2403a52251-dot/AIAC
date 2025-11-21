class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        """Add an item with the given name and price to the cart.
        If the item already exists, increment its quantity."""
        if name in self.items:
            self.items[name]['quantity'] += 1
        else:
            self.items[name] = {'price': price, 'quantity': 1}

    def remove_item(self, name):
        """Remove one quantity of the item with the given name from the cart.
        If the quantity becomes zero or the item does not exist, remove it completely."""
        if name in self.items:
            if self.items[name]['quantity'] > 1:
                self.items[name]['quantity'] -= 1
            else:
                del self.items[name]

    def total_cost(self):
        """Return the total cost of all items in the cart."""
        return sum(info['price'] * info['quantity'] for info in self.items.values())
