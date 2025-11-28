CREATE TABLE IF NOT EXISTS clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO clients (name, email) VALUES 
('Jean Dupont', 'jean@test.com'),
('Louis Docker', 'louis@test.com');
