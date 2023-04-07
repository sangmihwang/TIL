-- 테이블 삭제하기
DROP TABLE superhero3;

-- 새로운 테이블 생성하기
-- 이름, 직업, 능력, 국적, 팀을 필드로 가진 테이블
CREATE TABLE superhero (
  -- rowid 컬럼의 별칭으로 id 를 사용하겠다
  id INTEGER PRIMARY KEY,
  이름 TEXT NOT NULL,
  직업 TEXT,
  능력 TEXT,
  국적 TEXT,
  팀 TEXT,
  나이 INTEGER
);


-- 테이블명 변경하기
ALTER TABLE superheroes RENAME TO superhero;

-- 컬럼명 변경하기
ALTER TABLE superhero RENAME COLUMN 팀 TO 소속회사;

-- 새로운 컬럼 추가하기
-- UNIQUE 속성을 가진 컬럼은 추가 할 수 없다.(SQLITE 가 지원하지 않음)
ALTER TABLE superhero ADD COLUMN 가입날짜 DATE;

-- DROP COLUMN 은 안됨.
-- 2022년 말~ 2023 초에 등록된 새로운 기능
-- extension 은 2022년 6월 기준 sqlite3 를 사용
-- ALTER TABLE superhero ADD COLUMN 임시 TEXT;
-- ALTER TABLE superhero DROP COLUMN 임시;


-- 데이터 넣어보기
-- .mode 및 .import 사용하기
