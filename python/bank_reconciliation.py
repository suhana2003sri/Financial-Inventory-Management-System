def reconcile_bank(cash_book_balance, bank_statement_balance):
    difference = cash_book_balance - bank_statement_balance

    print("Cash Book Balance:", cash_book_balance)
    print("Bank Statement Balance:", bank_statement_balance)
    print("Difference:", difference)


reconcile_bank(50000, 48000)
