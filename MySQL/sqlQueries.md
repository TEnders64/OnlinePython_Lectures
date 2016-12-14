###CREATE

INSERT INTO blogs (title, content, created_at, updated_at) VALUES ("A guide to full CRUD operations", "Here is the syntax: etc etc", NOW(), NOW())

###READ/RETRIEVE

SELECT column1, column2 FROM tablename;

SELECT * FROM users;

SELECT movies.moviename, actors.actor_first, actors.actor_last
FROM movies
	LEFT JOIN actor_movies
		ON movies.id = actor_movies.movie_id
	LEFT JOIN actors
		ON actor_movies.actor_id = actors.id
	JOIN genre
		ON movies.genre = genre.id
WHERE
	actor_first = "Matt"
AND
	actor_last = "Damon"
AND
	movie.published_year > 2000;

###UPDATE
#were-claws

UPDATE users
SET
	first_name = "William",
	last_name = "Of Occam"
WHERE
	id = 8973

###DESTROY/DELETE

DELETE FROM users WHERE id = 8973
