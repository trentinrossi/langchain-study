data = [
    {
        "customer": "customer1",
        "product": "product1",
        "quantity": 1,
        "price": 1.0,
    },
    {
        "customer": "customer2",
        "product": "product2",
        "quantity": 1,
        "price": 5.0,
    },
]

# Loop over all of the customers
for customer in data:
    # If the customer is customer1, then print "Customer 1 is the first customer":
    if customer["customer"] == "customer1":
        print("Customer 1 is the first customer")

