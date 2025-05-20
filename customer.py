class Customer:
    def _init_(self, name):
    
        self.name = name  
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return self._orders

    def coffees(self):
        
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees

    def create_order(self, coffee, price):
        
        from order import Order
        new_order = Order(self, coffee, price)
        return new_order