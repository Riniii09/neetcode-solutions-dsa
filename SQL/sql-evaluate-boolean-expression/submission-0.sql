-- Write your query below
SELECT left_operand, 
       operator, 
       right_operand, 
       CASE WHEN operator = '<' AND vari.value < varii.value
            THEN 'true'
            WHEN operator = '>' AND vari.value > varii.value
            THEN 'true'
            WHEN operator = '=' AND vari.value = varii.value
            THEN 'true'
            ELSE 'false'
       END AS value
FROM expressions AS expr
CROSS JOIN variables AS vari 
CROSS JOIN variables AS varii
WHERE vari.name = left_operand
AND varii.name = right_operand