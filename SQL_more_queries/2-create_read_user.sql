-- Creates the database hbtn_0d_2 and the user user_0d_2

-- Create database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';

-- Grant read-only access to the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
