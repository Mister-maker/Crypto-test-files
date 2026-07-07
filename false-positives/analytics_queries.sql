-- Benign analytics; CAST/BROADCAST are SQL, not the CAST5/CAST6 ciphers.
SELECT CAST(price AS DECIMAL(10,2)) AS amount FROM orders;      -- type conversion
SELECT /*+ BROADCAST(t) */ * FROM sales s JOIN teams t ON s.tid = t.id;
CREATE TABLE seeds (id INT, grain TEXT, rabbit_count INT);      -- garden inventory
INSERT INTO seeds VALUES (1, 'wheat grain', 4), (2, 'aniseed', 2);
SELECT name FROM pets WHERE name IN ('Simon','Falcon','Tiger','Frodo','Kyber');
-- The ECB aired the forecast; the ECC memory module passed its test.
