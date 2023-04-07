CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- users 테이블에서 이름, 나이, 계좌 잔고를 
-- 나이가 어린 순으로, 
-- 같은 나이라면 계좌 잔고가 많은 순으로 정렬
SELECT * FROM users;

SELECT first_name, age, balance FROM users
ORDER BY age ASC, balance DESC;

SELECT first_name, age FROM users
ORDER BY first_name, age DESC;

SELECT first_name, country FROM users
WHERE first_name LIKE '건우' and country LIKE '경기도';