
SELECT COUNT(*)
FROM visitor_tb V
WHERE V.VST_TIME BETWEEN '2017-05-01' AND '2020-01-31';

SELECT V.IP_ADDRESS, COUNT(*)
FROM visitor_tb V
GROUP BY V.IP_ADDRESS
HAVING COUNT(*) >= 2
ORDER BY COUNT(*) DESC;

SELECT DATE_FORMAT(V.VST_TIME,'%Y'), COUNT(*)
FROM visitor_tb V
GROUP BY DATE_FORMAT(V.VST_TIME,'%Y');

SELECT DATE_FORMAT(V.VST_TIME,'%m'), COUNT(*)
FROM visitor_tb V
GROUP BY DATE_FORMAT(V.VST_TIME,'%m')
ORDER BY COUNT(*) DESC;


SELECT DATE_FORMAT(V.VST_TIME, '%Y-%m') 방문월,
CASE
WHEN V.VST_PATH = 1 THEN '검색'
WHEN V.VST_PATH = 2 THEN '부산관광공사'
END AS 방문경로,
COUNT(*) 방문자수 
FROM visitor_tb V
GROUP BY 방문월, V.VST_PATH
ORDER BY 방문월;





















