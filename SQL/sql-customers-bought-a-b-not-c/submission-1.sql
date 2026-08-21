SELECT customer_id, customer_name
FROM customers
WHERE customer_id 
IN
(SELECT customer_id FROM orders where product_name='A') and customer_id IN 
(SELECT customer_id FROM orders where product_name='B') and customer_id Not IN
(SELECT customer_id FROM orders where product_name='C')
ORDER BY 
customer_name
