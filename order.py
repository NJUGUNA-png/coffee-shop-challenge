class Order:
    def __init__(self, customer, coffee, price):
        
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        
        
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        
        
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not (1.0 <= float(price) <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
            
        self._customer = customer
        self._coffee = coffee
        self._price = float(price) 
        
        
        customer._orders.append(self)
        coffee._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price