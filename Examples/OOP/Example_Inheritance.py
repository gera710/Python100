import random

"""
## Overview

This Python script provides a practical demonstration of fundamental Object-Oriented Programming (OOP) concepts, primarily focusing on **Inheritance** and **Polymorphism**. It models a simple banking system with different types of accounts (`Account`, `SavingsAccount`, `CheckingAccount`) to illustrate how classes can be structured hierarchically, share common functionality, and exhibit specialized behaviors.

## File Purpose

The main goal of this example is to showcase:
1.  How to define a base class (`Account`) with common attributes and methods.

2.  How to create derived classes (`SavingsAccount`, `CheckingAccount`) 
that inherit from the base class.

3.  How derived classes can extend the base class with new attributes and 
methods (`interest_rate`, `overdraft_limit`, `apply_interest`).

4.  How derived classes can override base class methods to provide 
specialized implementations (Polymorphism, e.g., `withdraw` in `CheckingAccount`, `__str__` 
in both derived classes).

5.  The use of `super()` to call methods from the parent class.

6.  Basic encapsulation using "protected" attributes (conventionally prefixed with `_`) and 
the `@property` decorators for controlled access.

7.  Defining and using custom exception classes (`InsufficientFundsError`, `InvalidAmountError`) 
for more specific error handling, which also demonstrates inheritance from built-in exception types.

8.  The use of dunder methods like `__init__`, `__str__`, and `__repr__` for object initialization 
and representation.
"""

# --- Custom Exceptions for better error handling ---
class InsufficientFundsError(Exception):
    """Custom exception for when a withdrawal exceeds available funds."""
    pass

class InvalidAmountError(ValueError):
    """Custom exception for invalid deposit/withdrawal amounts."""
    pass

# ==============================================================================
# Base Class: Account
# ==============================================================================
class Account:
    """
    Represents a generic bank account.
    Serves as the base class for specific account types.
    Demonstrates: Classes, Objects, Attributes, Methods, Encapsulation (via _ and properties)
    """
    MINIMUM_OPENING_BALANCE = 10.00 # Class attribute

    def __init__(self, owner_name: str, initial_balance: float):
        """Initializes a new bank account."""
        if initial_balance < Account.MINIMUM_OPENING_BALANCE:
            raise InvalidAmountError(f"Initial balance must be at least {Account.MINIMUM_OPENING_BALANCE:.2f}")

        # Protected attributes (by convention)
        self._account_number = self._generate_account_number()
        self._owner_name = owner_name
        self._balance = float(initial_balance)
        print(f"Account {self._account_number} created for {self._owner_name} with balance ${self._balance:.2f}")

    def _generate_account_number(self) -> str:
        """Helper method to generate a unique account number (simplified)."""
        # In a real system, this would be more robust and ensure uniqueness
        return str(random.randint(1000000000, 9999999999))

    # --- Properties for controlled access to attributes ---
    @property
    def account_number(self) -> str:
        """Read-only property for account number."""
        return self._account_number

    @property
    def owner_name(self) -> str:
        """Read-only property for owner name."""
        return self._owner_name

    @property
    def balance(self) -> float:
        """Read-only property for balance."""
        return self._balance

    # --- Core Methods ---
    def deposit(self, amount: float):
        """Deposits a positive amount into the account."""
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self._balance:.2f}")

    def withdraw(self, amount: float):
        """
        Withdraws a positive amount from the account if funds are sufficient.
        This method will be overridden in subclasses (Polymorphism).
        """
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError(f"Cannot withdraw ${amount:.2f}. Available balance: ${self._balance:.2f}")

        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}")

    # --- Dunder methods for representation ---
    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"Account Holder: {self._owner_name}\nAccount No.: {self._account_number}\nBalance: ${self._balance:.2f}"

    def __repr__(self) -> str:
        """Official string representation for developers."""
        return f"Account(owner_name='{self._owner_name}', initial_balance={self._balance})"

# ==============================================================================
# Derived Class: SavingsAccount
# ==============================================================================
class SavingsAccount(Account):
    """
    A specialized account that earns interest.
    Demonstrates: Inheritance
    """
    def __init__(self, owner_name: str, initial_balance: float, interest_rate: float = 0.01):
        """Initializes a savings account, adding an interest rate."""
        # Call the parent class's __init__ method
        super().__init__(owner_name, initial_balance)
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self._interest_rate = interest_rate
        print(f"Savings Account created with interest rate: {self._interest_rate:.2%}")

    @property
    def interest_rate(self) -> float:
        return self._interest_rate

    def apply_interest(self):
        """Calculates and deposits interest earned."""
        interest_earned = self._balance * self._interest_rate
        print(f"Applying interest ({self._interest_rate:.2%})...")
        self.deposit(interest_earned) # Reuse the deposit method from the base class

    # Override __str__ to include interest rate (Polymorphism)
    def __str__(self) -> str:
        # Call parent's __str__ and add more info
        return f"{super().__str__()}\nType: Savings Account\nInterest Rate: {self._interest_rate:.2%}"

    def __repr__(self) -> str:
        return f"SavingsAccount(owner_name='{self._owner_name}', initial_balance={self._balance}, interest_rate={self._interest_rate})"

# ==============================================================================
# Derived Class: CheckingAccount
# ==============================================================================
class CheckingAccount(Account):
    """
    A specialized account allowing overdraft up to a certain limit.
    Demonstrates: Inheritance, Overriding Methods (Polymorphism)
    """
    def __init__(self, owner_name: str, initial_balance: float, overdraft_limit: float = 100.00):
        """Initializes a checking account, adding an overdraft limit."""
        super().__init__(owner_name, initial_balance)
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self._overdraft_limit = float(overdraft_limit)
        print(f"Checking Account created with overdraft limit: ${self._overdraft_limit:.2f}")

    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit

    # Override the withdraw method (Polymorphism)
    def withdraw(self, amount: float):
        """
        Withdraws amount, allowing for overdraft up to the limit.
        """
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")

        # Check if withdrawal exceeds balance + overdraft limit
        if amount > self._balance + self._overdraft_limit:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount:.2f}. "
                f"Available including overdraft (${self._overdraft_limit:.2f}): ${self._balance + self._overdraft_limit:.2f}"
            )

        self._balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self._balance:.2f}"
              f"{' (Overdraft Active)' if self._balance < 0 else ''}")

    # Override __str__ to include overdraft limit (Polymorphism)
    def __str__(self) -> str:
        return f"{super().__str__()}\nType: Checking Account\nOverdraft Limit: ${self._overdraft_limit:.2f}"

    def __repr__(self) -> str:
        return f"CheckingAccount(owner_name='{self._owner_name}', initial_balance={self._balance}, overdraft_limit={self._overdraft_limit})"


# --- Example Usage ---
print("\n--- OOP Bank Example ---")

try:
    # Create instances (Objects) of different classes
    print("\n1. Creating Accounts:")
    acc1 = SavingsAccount("Alice Smith", 500.00, 0.02) # Savings with 2% interest
    acc2 = CheckingAccount("Bob Johnson", 200.00, 50.00) # Checking with $50 overdraft
    # acc_invalid = Account("Charlie Brown", 5.00) # This would raise InvalidAmountError

    print("\n2. Account Details:")
    print("--- Account 1 ---")
    print(acc1) # Uses SavingsAccount.__str__
    print("\n--- Account 2 ---")
    print(acc2) # Uses CheckingAccount.__str__

    print("\n3. Performing Transactions:")
    print("\n--- Account 1 (Savings) ---")
    acc1.deposit(150.00)
    acc1.withdraw(50.00)
    acc1.apply_interest() # Specific to SavingsAccount
    # Access balance via property
    print(f"Current balance for {acc1.owner_name}: ${acc1.balance:.2f}")

    print("\n--- Account 2 (Checking) ---")
    acc2.deposit(75.00)
    acc2.withdraw(300.00) # This should use the overdraft
    print(f"Current balance for {acc2.owner_name}: ${acc2.balance:.2f}")
    # acc2.apply_interest() # This would cause an AttributeError

    print("\n4. Testing Error Handling:")
    print("\n--- Account 1 (Savings) ---")
    try:
        acc1.withdraw(1000.00) # Insufficient funds
    except InsufficientFundsError as e:
        print(f"Caught expected error: {e}")

    print("\n--- Account 2 (Checking) ---")
    try:
        acc2.withdraw(100.00) # Exceeds balance + overdraft
    except InsufficientFundsError as e:
        print(f"Caught expected error: {e}")

    try:
        acc2.deposit(-50) # Invalid amount
    except InvalidAmountError as e:
        print(f"Caught expected error: {e}")

except (InvalidAmountError, InsufficientFundsError, ValueError) as e:
    print(f"\nAn error occurred during setup or transactions: {e}")


print("\n--- End of OOP Bank Example ---")

"""
Explanation:
## Key Components

1.  **Custom Exceptions:**
    *   `InsufficientFundsError(Exception)`: Raised when a withdrawal attempt exceeds the available funds (including overdraft for checking accounts).
    *   `InvalidAmountError(ValueError)`: Raised for invalid transaction amounts (e.g., non-positive deposits/withdrawals, insufficient initial balance).

2.  **`Account` (Base Class):**
    *   Represents a generic bank account.
    *   **Attributes:** `_owner_name`, `_balance`, `_account_number` (generated randomly), `MINIMUM_OPENING_BALANCE` (class attribute).
    *   **Methods:**
        *   `__init__`: Initializes the account, validates the initial balance, generates an account number.
        *   `_generate_account_number`: Helper method for number generation.
        *   `deposit`: Adds funds, validates the amount.
        *   `withdraw`: Removes funds, validates the amount, checks for sufficient balance (basic check).
        *   `account_number`, `owner_name`, `balance`: Read-only properties using `@property` for accessing protected attributes (encapsulation).
        *   `__str__`, `__repr__`: Provide user-friendly and developer-friendly string representations.

3.  **`SavingsAccount` (Derived Class):**
    *   Inherits from `Account`.
    *   **Adds:** `_interest_rate` attribute.
    *   **Extends:** `__init__` calls `super().__init__` and initializes the interest rate.
    *   **Adds:** `interest_rate` property and `apply_interest` method to calculate and deposit interest (reusing the base `deposit` method).
    *   **Overrides:** `__str__` and `__repr__` to include savings-specific information, calling `super().__str__()` to reuse the base representation.

4.  **`CheckingAccount` (Derived Class):**
    *   Inherits from `Account`.
    *   **Adds:** `_overdraft_limit` attribute.
    *   **Extends:** `__init__` calls `super().__init__` and initializes the overdraft limit.
    *   **Adds:** `overdraft_limit` property.
    *   **Overrides:** `withdraw` method to implement different logic that allows withdrawals up to the balance plus the overdraft limit (Polymorphism).
    *   **Overrides:** `__str__` and `__repr__` to include checking-specific information, calling `super().__str__()`.

## OOP Concepts Illustrated

*   **Inheritance:** `SavingsAccount` and `CheckingAccount` inherit attributes and methods from `Account`.
*   **Polymorphism:** The `withdraw` method behaves differently in `CheckingAccount` compared to `Account`. The `__str__` method provides different output depending on whether the object is an `Account`, `SavingsAccount`, or `CheckingAccount`.
*   **Encapsulation:** Internal state (`_balance`, `_owner_name`, etc.) is kept "protected", and access is primarily managed through methods and properties.
*   **Abstraction:** The `Account` class provides a simplified, abstract view of a bank account, hiding implementation details.
*   **`super()`:** Used effectively in `__init__` and `__str__` of derived classes to leverage parent class implementation.
*   **Class and Instance Attributes:** Demonstrates both (`MINIMUM_OPENING_BALANCE` vs. `_balance`).
*   **Dunder Methods:** Shows common usage of `__init__`, `__str__`, `__repr__`.
*   **Custom Exceptions:** Enhances error handling and demonstrates inheriting from standard exceptions.

## Execution Flow (Example Usage)

The `if __name__ == "__main__":` block demonstrates the practical use of these classes:
1.  Creates instances (objects) of `SavingsAccount` and `CheckingAccount`.
2.  Prints account details using the overridden `__str__` methods, showcasing polymorphism.
3.  Performs transactions (`deposit`, `withdraw`, `apply_interest`) on the objects, showing how methods inherited or specific to the classes are called.
4.  Accesses account balances using the read-only properties.
5.  Uses `try...except` blocks to demonstrate how the custom exceptions (`InsufficientFundsError`, `InvalidAmountError`) are raised and caught during invalid operations (like overdrafting beyond the limit or attempting negative deposits).

"""
