
-- 5

SELECT E.first_name, E.salary,
CASE 
WHEN E.commission_pct IS NULL THEN 0
ELSE E.commission_pct
END,
CASE
WHEN E.commission_pct IS NULL THEN E.salary
ELSE E.salary+E.commission_pct
END
FROM employees E;


-- 6

SELECT E.first_name
FROM employees E
WHERE E.commission_pct IS NULL;



-- 7

SELECT E.first_name, E.department_id
FROM employees E
WHERE E.first_name LIKE 'S%'
ORDER BY E.department_id DESC;


-- 8

SELECT E.department_id, AVG(E.salary)
FROM employees E, departments D
WHERE E.employee_id=D.department_id
GROUP BY E.department_id
HAVING AVG(E.salary)>=2000;


-- 10

SELECT E.first_name, E.department_id, D.department_name, L.city
FROM employees E, jobs J, departments D,locations L
WHERE E.department_id=D.department_id
AND D.location_id=L.location_id
AND E.job_id=J.job_id
AND J.job_title='Stock Clerk';









