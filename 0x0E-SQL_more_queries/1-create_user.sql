-- A script to create a user if its doesn't exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT SELECT ON *.* TO 'user_0d_1'@'localhost';
