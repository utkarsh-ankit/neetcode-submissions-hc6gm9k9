-- SELECT customer_id, customer_name
-- FROM customers
-- WHERE customer_id 
-- IN
-- (SELECT customer_id FROM orders where product_name='A') and customer_id IN 
-- (SELECT customer_id FROM orders where product_name='B') and customer_id Not IN
-- (SELECT customer_id FROM orders where product_name='C')
-- ORDER BY 
-- customer_name

SELECT c.customer_id, c.customer_name
FROM customers c
JOIN orders o ON c.customer_id=o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING
SUM(CASE WHEN o.product_name='A' THEN 1 ELSE 0 END)>0 AND
SUM(CASE WHEN o.product_name='B' THEN 1 ELSE 0 END)>0 AND
SUM(CASE WHEN o.product_name='C' THEN 1 ELSE 0 END)=0
ORDER BY c.customer_name





