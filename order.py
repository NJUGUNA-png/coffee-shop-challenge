class Order:
    def __init__(self, customer, coffee, price):
        
        from customer import Customer
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        
        
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        
        
       