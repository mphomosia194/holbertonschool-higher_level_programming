-- Lists all records with a non-null name

-- Display score and name for rows where name exists
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
