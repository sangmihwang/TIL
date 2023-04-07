-- JOIN 을 테스트 하기 위해 랜덤으로 NULL 값을 넣음
UPDATE hero SET 가입날짜 = NULL WHERE id = 10;
UPDATE hero SET 가입날짜 = NULL WHERE id = 20;
UPDATE hero SET 가입날짜 = NULL WHERE id = 25;
UPDATE hero SET job_id = NULL WHERE id = 30;
UPDATE hero SET job_id = NULL WHERE id = 40;
UPDATE hero SET job_id = NULL WHERE id = 50;
UPDATE hero SET company_id = NULL WHERE id = 64;
UPDATE hero SET company_id = NULL WHERE id = 75;
UPDATE hero SET company_id = NULL WHERE id = 88;
UPDATE hero SET country_id = NULL WHERE id = 16;
UPDATE hero SET country_id = NULL WHERE id = 46;
UPDATE hero SET country_id = NULL WHERE id = 57;

-- JOIN: 여러 테이블을 합쳐서 원하는 데이터를 조회하는 기법

-- CROSS JOIN
-- 두 테이블 간 가능한 모든 조합을 선택
SELECT * FROM hero, job;

-- INNER JOIN
-- 두 테이블 에서 일치하는 값을 가진 행들만 선택
-- SELECT <필드> FROM 테이블1
-- INNER JOIN 테이블2
-- ON 조건
-- 전체 사람들의 id, 이름, 직업을 조회하여라
SELECT hero.id, hero.이름, job.job
FROM hero
INNER JOIN job
ON hero.job_id = job.id;


-- LEFT JOIN
-- 왼쪽 테이블의 모든 행과 오른쪽 테이블에서 일치하는 값을 가진 행을 선택
-- 일치하는 겂이 없는 경우에는 NULL 값을 가짐
SELECT hero.id, hero.이름, job.job
FROM hero
LEFT JOIN job
ON hero.job_id = job.id;

-- 똑같은 코드 다른 표현 방식
-- 필드명이 겹치지 않는 부분은 명시하지 않을 수 있다
SELECT hero.id, 이름, job
FROM hero AS A
LEFT JOIN job AS B
ON hero.job_id = job.id;

-- 똑같은 코드 다른 표현 방식2
-- 각 테이블에 별칭을 주어 표현
SELECT A.id, A.이름, B.job
FROM hero AS A
LEFT JOIN job AS B
ON hero.job_id = job.id;


-- 영웅들의 id, 이름, 능력을 조회하여라
SELECT hero.id, hero.이름, power.능력
FROM hero
LEFT JOIN power
ON hero.id = power.hero_id;


-- 영웅들의 id, 이름, 직업, 소속회사를 조회하여라
SELECT hero.id, hero.이름, job.job, company.company
FROM hero
    LEFT JOIN job
    ON hero.job_id = job.id
    LEFT JOIN company
    ON hero.company_id = company.id;


