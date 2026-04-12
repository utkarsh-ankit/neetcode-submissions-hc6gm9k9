-- Write your query below
SELECT o.sale_date, a.sold_num-o.sold_num as diff
FROM sales o
JOIN sales a ON o.sale_date=a.sale_date
WHERE o.fruit='oranges'
AND a.fruit='apples'
