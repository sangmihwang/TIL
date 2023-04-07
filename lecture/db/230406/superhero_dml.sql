-- 1. 전체 조회
-- 2. 특정 필드 조회
-- 3. 정렬하기
-- 3.1 여러 필드 정렬하기
-- 4. 중복 제거하기
-- 5. 조건문 써보기
-- 6. 특정 개수만 가져오기
-- 7. OFFSET 활용하기

-- 전체 조회
SELECT * FROM superhero;

-- rowid 는 암시적으로 들어있음
SELECT * FROM superhero WHERE rowid = 1;
SELECT rowid FROM superhero;

-- 이름과 직업 조회하기
SELECT 이름, 직업 FROM superhero;

-- 나이가 어린순으로 조회하기
SELECT * FROM superhero ORDER BY 나이;

-- 나이가 많은 순으로 조회하기
SELECT * FROM superhero ORDER BY 나이 DESC;

-- 소속회사 별로 나이가 많은순으로 조회하기
SELECT 이름, 나이, 소속회사 FROM superhero ORDER BY 소속회사, 나이 DESC;

-- 중복 제거하기
-- 모두 중복되는 값을 제거해준다.
SELECT DISTINCT 소속회사 FROM superhero;

SELECT DISTINCT 직업, 소속회사 FROM superhero;

-- 이름, 나이, 소속회사가 겹치지 않는 사람들 중 소속회사, 나이 순으로 정렬
SELECT DISTINCT 나이, 소속회사 FROM superhero
ORDER BY 소속회사, 나이;

-- 영웅인 사람들만 조회하기
SELECT * FROM superhero WHERE 직업 = '영웅';

-- 가입날짜 조회
-- 비교할 때는 필드에 맞춰서 하기
SELECT 이름, 가입날짜 FROM superhero WHERE 가입날짜 < '2000-01-01';

-- 마블 소속의 영웅인 사람들만 조회하기
SELECT * FROM superhero WHERE 소속회사 = '마블' AND 직업 = '영웅';

-- 이름의 끝에 '맨' 이 들어가는 모든 사람 조회하기
SELECT * FROM superhero WHERE 이름 LIKE '맨%';

-- 나이가 50 살이 넘는 사람 조회하기
SELECT * FROM superhero WHERE 나이 >= 50;

-- 나이가 10~100살 사이의 사람 조회하기
-- 언더바: 특정 글자 하나를 의미
SELECT * FROM superhero WHERE 나이 LIKE '__';

-- 능력이 술과 관련된 사람들 조회하기
SELECT * FROM superhero WHERE 능력 LIKE '%술%';

-- 마블, DC 소속의 사람들 조회
SELECT * FROM superhero WHERE 소속회사 IN ('마블', 'DC');

-- 마블, DC 소속의 사람들 중 악당만 조회
SELECT * FROM superhero 
WHERE 소속회사 IN ('마블', 'DC')
    AND 직업 = '악당';


-- 나이가 100~500살 사이의 사람들
-- 이상, 이하 입니다.
SELECT * FROM superhero WHERE 나이 BETWEEN 100 AND 500;

-- 하나의 열만 뽑아내기
-- LIMIT: 쿼리에서 반환되는 행 수를 제한
SELECT * FROM superhero LIMIT 1;

-- 나이가 가장 적은 사람
SELECT * FROM superhero ORDER BY 나이 LIMIT 1;

-- 나이가 많은 10명
SELECT * FROM superhero ORDER BY 나이 DESC LIMIT 10;

-- 나이가 10번 째로 많은 사람
-- OFFSET: N 번째 데이터 부터 조회하기
SELECT * FROM superhero ORDER BY 나이 DESC LIMIT 1 OFFSET 10;

SELECT 소속회사, AVG(나이) AS 영웅평균나이
FROM superhero
GROUP BY 소속회사;

SELECT * FROM superhero
GROUP BY 소속회사;



-- 평균 나이가 40살 이상인 소속회사를 구하여라
-- 평균 나이: GROUP BY + AVG 의 결과

-- 소속회사 별로 그룹 (뒤에서부터 읽어오기)
-- 40살 이상인 데이터만 조회해서
-- 평균 계산
SELECT 소속회사, AVG(나이) AS 평균나이
FROM superhero
WHERE 나이 >= 40
GROUP BY 소속회사;

-- 그룹화 후에 조건 주기 (HAVING : 그룹화한것 중에)
-- 평균 나이가 40살 이상인 소속회사를 구하여라
SELECT 소속회사, AVG(나이) AS 평균나이
FROM superhero
GROUP BY 소속회사
HAVING AVG(나이)>= 40;


-- 그룹화 이전에 조건문 필요-> WHERE
-- 그룹화 이후에 조건문 -> HAVING
