-- Lists the number of records with the same score

-- Display score and count of records for each score
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
