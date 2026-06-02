-- Lists all records with a score greater than or equal to 10

-- Display score and name for records with score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
