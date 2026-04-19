-- Write your query below
SELECT s.seller_name
FROM seller s
LEFT JOIN orders o ON s.seller_id=o.seller_id AND LEFT(o.sale_date::text, 4) = '2020'
WHERE o.seller_id IS NULL
ORDER BY s.seller_name