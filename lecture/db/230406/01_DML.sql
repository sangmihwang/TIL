-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;

SELECT AVG(balance) FROM users;


CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates
VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최치수', 12, '충청'),
    ('김나다', 25, '경상');


UPDATE classmates
SET name='김철수한무두루미',
    address='제주'
WHERE rowid=2;

DELETE FROM classmates
WHERE rowid=5;

-- 이름에 '영' 들어간 데이터 삭제
DELETE FROM classmates 
WHERE name LIKE '%영%';

-- 데이터 모두 삭제
DELETE FROM classmates;