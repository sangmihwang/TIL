--  DATABASE DAY1
-- CREATE TABLE statement

CREATE TABLE contacts(
name TEXT NOT NULL,
age INTEGER NOT NULL,
email TEXT NOT NULL UNIQUE
);

ALTER TABLE contacts RENAME TO new_contacts;