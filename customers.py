
# ISM 2411 - Lab 11
# Name: Ashwin

# REFLECTION 1:
# I would use .get() when a dictionary key might not exist, because it
# allows me to provide a default value without causing an error.
# I would use bracket notation when I know the key exists and need its value.

# REFLECTION 2:
# This pattern reminds me of using SUMIF in Excel, where we add values
# based on a matching category. Python is more useful for large datasets
# because loops can process many records automatically and flexibly.


# ==========================================
# EXERCISE 1 - One customer
# ==========================================

customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 2500
}

print("EXERCISE 1")

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)


# ==========================================
# EXERCISE 2 - Update and add
# ==========================================

print("\nEXERCISE 2")

# Add phone field
customer["phone"] = "813-555-1234"
print(customer)

# Update tier
customer["tier"] = "platinum"
print(customer)

# Delete email field
del customer["email"]
print(customer)


# ==========================================
# EXERCISE 3 - Safe lookup
# ==========================================

print("\nEXERCISE 3")

# Use get() to look up the deleted email
email = customer.get("email", "no email on file")
print(email)

# Use bracket notation to look up the deleted email
# This raises a KeyError because the email key no longer exists.
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist in the dictionary")


# ==========================================
# EXERCISE 4 - Iterate
# ==========================================

print("\nEXERCISE 4")

# .items() gives us both the key and the value.
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the keys.
for key in customer:
    print(key)


# ==========================================
# EXERCISE 5 - Lookup table
# ==========================================

print("\nEXERCISE 5")

tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

tier = customer["tier"]

# Get the discount for the customer's tier.
discount = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print("Tier:", tier)
print("Discount rate:", discount * 100, "%")
print("Final price: $", round(final_price, 2))


# ==========================================
# EXERCISE 6 - List of dictionaries
# ==========================================

print("\nEXERCISE 6")

dict1 = {
    "name": "Alice",
    "tier": "platinum"
}

dict2 = {
    "name": "Bob",
    "tier": "gold"
}

dict3 = {
    "name": "Charlie",
    "tier": "silver"
}

customers = [dict1, dict2, dict3]

for person in customers:
    name = person["name"]
    tier = person["tier"]

    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{name}: {tier} - Discount: ${discount_amount:.2f}")


# ==========================================
# EXERCISE 7 - Nested catalog
# ==========================================

print("\nEXERCISE 7")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left")


# ==========================================
# EXERCISE 8 - Sales by region
# ==========================================

print("\nEXERCISE 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    # Add the amount to the region's existing total.
    sales_summary[region] = sales_summary.get(region, 0) + amount

# Print the summary sorted alphabetically by region.
for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
