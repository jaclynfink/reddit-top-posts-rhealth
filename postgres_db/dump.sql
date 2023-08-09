CREATE TABLE IF NOT EXISTS top_posts(
    id SERIAL PRIMARY KEY,
    date_time timestamp,
    word CHARACTER VARYING(100),
    `url` CHARACTER VARYING(100),
    `definition` text
);