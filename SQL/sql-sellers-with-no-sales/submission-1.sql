-- Write your query below
SELECT DISTINCT seller_name FROM seller WHERE seller_id NOT IN
(SELECT DISTINCT s.seller_id FROM seller s
LEFT JOIN orders o ON o.seller_id = s.seller_id
WHERE o.sale_date > '2019-12-31' AND o.sale_date < '2021-01-01')
ORDER BY seller_name;
