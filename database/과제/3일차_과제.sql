USE testdatabase;

-- # employees 테이블 생성
--  CREATE TABLE employees (
--      employees_id INT PRIMARY KEY AUTO_INCREMENT,
--      name VARCHAR(100),
--      position VARCHAR(100),
--      salary DECIMAL(10,2)
--  );

-- # 직원 데이터 추가
-- INSERT INTO employees (name, position, salary)
-- VALUES 
-- ('혜린', 'PM', 90000),
-- ('은우', 'Frontend', 80000),
-- ('가을', 'Backend', 92000),
-- ('지수', 'Frontend', 78000),
-- ('민혁', 'Frontend', 96000),
-- ('하온', 'Backend', 130000);

# 모든 직원 조회
-- SELECT name, salary FROM employees;

#Frontend 연봉 90000이하 조회
-- SELECT name, salary 
-- FROM employees 
-- WHERE position = 'Frontend' AND salary <= 90000;

# PM직책 연봉 인상 후 결과 확인
-- SET SQL_SAFE_UPDATES = 0;
-- UPDATE employees 
-- SET salary = salary * 1.10 
-- WHERE position = 'PM';
-- SELECT * FROM employees WHERE position = 'Quality Assurance';

# Backend 연봉 인상
-- UPDATE employees 
-- SET salary = salary * 1.05 
-- WHERE position = 'Backend';

# 민혁 데이터 삭제
-- DELETE FROM employees 
-- WHERE name = '민혁';

# position별 평균 급여
-- SELECT position, AVG(salary) AS average_salary
-- FROM employees
-- GROUP BY position;

# employees 테이블 삭제
-- DROP TABLE employees;