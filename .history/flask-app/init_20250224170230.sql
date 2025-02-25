-- Create the 'images' table
CREATE TABLE IF NOT EXISTS images (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL
);

-- Insert sample image URLs
INSERT INTO images (url) VALUES
('https://media.tenor.com/zZ1i8J3C2RUAAAAM/hello-robert-e-fuller.gif'),
('https://media.tenor.com/1y8rq5FE6OEAAAAM/yawning-robert-e-fuller.gif'),
('https://media.tenor.com/KYE8V6nrzzYAAAAM/itchy-robert-e-fuller.gif'),
('https://media.tenor.com/YcZbpukPl34AAAAM/honey-badger-dance.gif');
