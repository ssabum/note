-- DDL
-- 테이블 생성
CREATE TABLE classmates (id INTEGER PRIMARY KEY, name TEXT);
-- 테이블 삭제
DROP TABLE classmates;
-- 테이블 변경
ALTER TABLE articles RENAME TO news;
-- 컬럼 추가
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;
-------------------------------------------------------------------------
-- DML
-- 데이터 조회
SELECT * FROM examples;
-- 데이터 추가
INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
-- 모든 COLUMN에 VALUES 추가할 때
INSERT INTO classmates VALUES ('홍길동', 30, '서울');
-- PK를 지정하지 않으면 rowid가 생성
SELECT rowid, * FROM classmates;
-- LIMIT & OFFSET: 3번째 ROW 가져오기
SELECT rowid, name FROM classmates LIMT 1 OFFSET 2;
-- WHERE
SELECT rowid, name FROM classmates WHERE address= '광주';
-- DISTINCT: 중복제거
SELECT DISTINCT address FROM classmates;
-- DELETE
DELETE FROM classmates WHERE rowid=4;
-- UPDATE
UPDATE classmates SET name='홍길동', address='제주' WHERE rowid=4;
-- EXPRESSIONS
SELECT first_name, MAX(balance) FROM users;
-- LIKE
SELECT * FROM users WHERE age LIKE '2_';
-- GROUP BY
SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;