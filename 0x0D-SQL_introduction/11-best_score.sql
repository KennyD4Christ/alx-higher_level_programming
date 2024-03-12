-- List all records with score >= 10 in the table second_table, displaying score and name, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
