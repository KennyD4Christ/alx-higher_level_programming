-- Script to create database hbtn_0d_2 and user user_0d_2 with SELECT privilege

-- Create the database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if not exists and grant SELECT privilege in the database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
