-- Write your query below
/*WITH ranked AS ( 
SELECT student_id, exam_id, score,
ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY exam_id desc, score desc) AS rnk
FROM exam_results e)
SELECT student_id, exam_id, score, rnk
FROM ranked
WHERE rnk = 1
ORDER BY student_id asc*/
WITH ranked AS ( 
SELECT student_id, exam_id, score,
ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY score DESC, exam_id ASC) AS rnk
FROM exam_results e)
SELECT student_id, exam_id, score--, rnk
FROM ranked
WHERE rnk = 1
ORDER BY student_id asc
