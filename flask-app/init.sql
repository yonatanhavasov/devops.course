 CREATE DATABASE IF NOT EXISTS gif_db;

  USE gif_db;                                     
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
('https://media.tenor.com/YcZbpukPl34AAAAM/honey-badger-dance.gif'),
('https://media1.tenor.com/m/uy06yNc_aXQAAAAd/honey-badger-woah.gif'),
('https://media1.tenor.com/m/kAvWsWS8vZgAAAAd/putois-carmaux.gif'),
('https://media1.tenor.com/m/TAf_lYi62gsAAAAd/dont-care-honey-badger.gif'),
('https://media1.tenor.com/m/U4_Uag4pZLsAAAAC/thug-life-honey-badger.gif');

CREATE TABLE IF NOT EXISTS visitor_counter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    count INT NOT NULL DEFAULT 0
);

-- Initialize the counter with a starting value of 0, for more rows add (0), (value of another row).
INSERT INTO visitor_counter (count) VALUES (0); 