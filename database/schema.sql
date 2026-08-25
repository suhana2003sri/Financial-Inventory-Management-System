-- Financial and Inventory Management System
-- Database Schema

CREATE DATABASE financial_inventory_management;

USE financial_inventory_management;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    quantity INT DEFAULT 0,
    unit_price DECIMAL(10,2)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE purchases (
    purchase_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id INT,
    product_id INT,
    quantity INT NOT NULL,
    purchase_date DATE NOT NULL,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE expenses (
    expense_id INT PRIMARY KEY AUTO_INCREMENT,
    expense_type VARCHAR(100) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    expense_date DATE NOT NULL,
    description VARCHAR(255)
);

CREATE TABLE receivables (
    receivable_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    amount DECIMAL(10,2) NOT NULL,
    due_date DATE,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE payables (
    payable_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id INT,
    amount DECIMAL(10,2) NOT NULL,
    due_date DATE,
    status VARCHAR(50) DEFAULT 'Pending',
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);
