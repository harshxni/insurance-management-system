CREATE TABLE customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    address TEXT,
    password TEXT
);

CREATE TABLE policy(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_name TEXT,
    premium INTEGER
);

CREATE TABLE payment(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    policy_name TEXT,
    amount INTEGER
);

CREATE TABLE claim(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    policy_name TEXT,
    reason TEXT
);