-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT tv_shows.title FROM tv_shows WHERE tv_shows.id NOT IN (SELECT tv_show_genres.show_id FROM tv_show_genres
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'Comedy') ORDER BY tv_shows.title;
