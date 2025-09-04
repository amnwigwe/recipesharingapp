-- init.sql: Initialize MySQL database for recipe app

CREATE DATABASE IF NOT EXISTS recipe_db;

USE recipe_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    ingredients TEXT,
    instructions TEXT
);

-- Sample users
INSERT INTO users (username, email, password) VALUES
('Alice', 'alice@example.com', 'password123'),
('Bob', 'bob@example.com', 'mypassword');

-- Sample recipes
INSERT INTO recipes (title, ingredients, instructions) VALUES
('Spaghetti Carbonara', 'Spaghetti, Eggs, Bacon, Parmesan', 'Boil pasta. Cook bacon. Mix with eggs and cheese.'),
('Tomato Soup', 'Tomatoes, Onion, Garlic, Cream', 'Cook ingredients. Blend. Serve hot.');
