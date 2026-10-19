-- Average rating by genre
SELECT Genre, AVG(Rating) AS AverageRating, COUNT(*) AS MovieCount
FROM movies GROUP BY Genre ORDER BY AverageRating DESC;
