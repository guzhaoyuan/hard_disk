
DROP DATABASE IF EXISTS HardDisk;
CREATE DATABASE IF NOT EXISTS HardDisk
CHARACTER SET utf8
COLLATE utf8_general_ci;
USE HardDisk;

DROP USER admin@localhost;
FLUSH PRIVILEGES;
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON HardDisk.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;