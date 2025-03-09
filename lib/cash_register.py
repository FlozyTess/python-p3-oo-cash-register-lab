#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """Initialize a cash register with an optional discount."""
        self.total = 0
        self.discount = discount
        self.items = []  # List to track all items
        self.last_transaction_amount = 0  # Track last transaction amount

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item to the cash register.
        Arguments:
            - item_name: Name of the item
            - price: Price per unit
            - quantity: Number of units (default is 1)
        """
        self.total += price * quantity
        self.items.extend([item_name] * quantity)  # Store item names for tracking
        self.last_transaction_amount = price * quantity  # Save for voiding

    def apply_discount(self):
        """Applies a discount to the total price."""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            self.total = round(self.total, 2)  # Ensure rounding to 2 decimal places

            # Format total properly to match test expectations
            total_display = f"${int(self.total)}" if self.total.is_integer() else f"${self.total:.2f}"
            print(f"After the discount, the total comes to {total_display}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Removes the last transaction from the total."""
        self.total -= self.last_transaction_amount
        if self.total < 0:
            self.total = 0  # Ensure total doesn't go negative
        self.last_transaction_amount = 0  # Reset after voiding

    def show_items(self):
        """Returns a list of all items added."""
        return self.items

    def get_total(self):
        """Returns the total amount."""
        return self.total
