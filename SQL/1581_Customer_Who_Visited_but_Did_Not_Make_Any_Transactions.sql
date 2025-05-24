SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits v
WHERE NOT EXISTS (
    SELECT t.visit_id
    FROM Transactions t
    WHERE t.visit_id = v.visit_id 
)
GROUP BY v.customer_id