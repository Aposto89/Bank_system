CREATE DATABASE new_bank;

USE new_bank;

CREATE TABLE ACCOUNTS (
    Acc_holder VARCHAR(20),
    Acc_number VARCHAR(20),
    DOB VARCHAR(10),
    Address VARCHAR(20),
    Contact INT,
    Openning_Bal INT
);

CREATE TABLE Amount (
    Acc_holder VARCHAR (20),
    Acc_number VARCHAR (20),
    Balance INT
);

SHOW tables;

DESC ACCOUNTS;
DESC Amount;

SELECT * FROM accounts;
SELECT * FROM amount;


