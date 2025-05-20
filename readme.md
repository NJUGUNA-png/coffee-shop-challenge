# Coffee Shop Domain Model

This is a simple Python project that models a coffee shop using object-oriented programming. It's designed for beginners to understand how classes and relationships work in Python.

## What This Project Does

This project creates a model for a coffee shop with three main components:
- **Customers** who visit the shop
- Different types of **Coffees** sold at the shop
- **Orders** that connect customers with the coffees they purchase

## Files in the Project

```
coffee-shop-challenge/
├── customer.py - Contains the Customer class
├── coffee.py - Contains the Coffee class
├── order.py - Contains the Order class
└── tests/ - Contains test files for each class
```

## Understanding the Classes

### Customer Class (`customer.py`)

A Customer represents someone who visits the coffee shop.

Features:
- Has a name (must be 1-15 characters long)
- Can place orders for different coffees
- Can view their order history
- Can see all the different coffees they've ordered


### Coffee Class (`coffee.py`)

A Coffee represents a type of coffee sold at the shop.

Features:
- Has a name (must be at least 3 characters)
- Once created, the name can't be changed
- Keeps track of all orders for this coffee
- Can tell you which customers have ordered it
- Can calculate how many times it's been ordered
- Can calculate the average price it's sold for


### Order Class (`order.py`)

An Order connects a Customer with a Coffee they've purchased.

Features:
- Links a specific customer to a specific coffee
- Includes the price (must be between $1.00 and $10.00)
- Once created, the price can't be changed
- Automatically updates both the customer and coffee records


## How Everything Connects

- A Customer can place many Orders for different Coffees
- A Coffee can be in many Orders from different Customers
- An Order always connects exactly one Customer to one Coffee
- This creates a "many-to-many" relationship between Customers and Coffees

## Learning from This Code

This project demonstrates:

1. **Class Design**: How to organize data and methods into classes
2. **Properties**: Using getters and setters to control access to data
3. **Data Validation**: Checking inputs to ensure they meet requirements
4. **Relationships**: Managing connections between different objects
5. **Type Checking**: Ensuring objects are of the correct class
6. **Immutability**: Making certain values unchangeable after creation
