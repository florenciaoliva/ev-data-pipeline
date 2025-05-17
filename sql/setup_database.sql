-- Create the user
CREATE USER ev_data_user WITH PASSWORD 'ev_password';

-- Create the database with the user as owner
CREATE DATABASE ev_data WITH OWNER ev_data_user;