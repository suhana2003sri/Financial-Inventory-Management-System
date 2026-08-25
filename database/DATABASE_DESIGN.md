# Database Design

## Main Tables

1. Users
- user_id
- name
- email
- password

2. Customers
- customer_id
- name
- contact
- email

3. Suppliers
- supplier_id
- name
- contact
- email

4. Products
- product_id
- product_name
- category
- quantity
- unit_price

5. Sales
- sale_id
- customer_id
- product_id
- quantity
- sale_date
- total_amount

6. Purchases
- purchase_id
- supplier_id
- product_id
- quantity
- purchase_date
- total_amount

7. Expenses
- expense_id
- expense_type
- amount
- expense_date

8. Receivables
- receivable_id
- customer_id
- amount
- due_date
- status

9. Payables
- payable_id
- supplier_id
- amount
- due_date
- status
