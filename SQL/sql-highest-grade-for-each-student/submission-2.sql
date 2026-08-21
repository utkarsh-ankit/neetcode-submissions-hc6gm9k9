-- table:- exam_results

-- highest score with corresponding exam id
-- if same score in multiple exam, return smallest exam id

-- approach:- for each student id, we take out all the exam_id, then we sort it, and give out the highest, and if there are two highrsret, we campare the exam id
-- theb return with order by studetn_id in ascentding order

-- SELECT student_id, exam_id, score
-- From exam_results
-- GROUP BY student_id
-- Having
-- score=score.sort desc(First)
-- CASE WHEN score.frst==socre,second, return sort by exam id ascending
-- return socre and exam id

-- SELECT Distinct ON (student_id)
-- student_id,
-- exam_id,
-- score
-- FROM exam_results
-- ORDER BY student_id, score DESC, exam_id ASC

-- https://www.youtube.com/watch?v=rIcB4zMYMas

SELECT student_id, exam_id, score
FROM (
    SELECT *, ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC, exam_id ASC) as rn
    FROM exam_results
) t
WHERE rn=1
ORDER BY student_id


