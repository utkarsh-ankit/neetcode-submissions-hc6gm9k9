SELECT s.seller_name 
FROM seller s
LEFT JOIN orders o
ON s.seller_id=o.seller_id AND o.sale_date BETWEEN '2020-01-01' AND '2020-12-31'
WHERE order_id IS Null
ORDER BY seller_name