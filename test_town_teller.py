# Exercise 1 Terminal testing:

from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.account_add(bob_savings)
zc_bank.inquiry_balance(1001)
# 0
zc_bank.money_deposit(1001, 256.02)
zc_bank.inquiry_balance(1001)
# 256.02
zc_bank.money_withdrawal(1001, 128)
zc_bank.inquiry_balance(1001)
# 128.02

print()

# Exercise 2 Terminal testing:

