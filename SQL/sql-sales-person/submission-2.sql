-- Write your query below
-- SELECT DISTINCT seller_name FROM seller WHERE seller_id NOT IN
-- (SELECT DISTINCT s.seller_id FROM seller s
-- LEFT JOIN orders o ON o.seller_id = s.seller_id
-- WHERE o.sale_date > '2019-12-31' AND o.sale_date < '2021-01-01')
-- ORDER BY seller_name;
SELECT DISTINCT sp.name FROM sales_person sp WHERE sp.sales_id NOT IN (SELECT s.sales_id AS salesperson_name
FROM sales_person s
FULL JOIN orders o ON o.sales_id = s.sales_id
FULL JOIN company c ON c.com_id = o.com_id
WHERE c.name = 'CRIMSON' AND s.name IS NOT NULL) ORDER BY sp.name;