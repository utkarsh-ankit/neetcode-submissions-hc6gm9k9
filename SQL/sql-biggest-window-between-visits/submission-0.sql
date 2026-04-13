-- Write your query below
SELECT user_id, MAX(diff) AS biggest_window
FROM (
    SELECT 
        v1.user_id, 
        (COALESCE(MIN(v2.visit_date), '2021-01-01') - v1.visit_date) AS diff
    FROM user_visits v1
    LEFT JOIN user_visits v2 
        ON v1.user_id = v2.user_id AND v2.visit_date > v1.visit_date
    GROUP BY v1.user_id, v1.visit_date
) AS subquery
GROUP BY user_id
ORDER BY user_id;