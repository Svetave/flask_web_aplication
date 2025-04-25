DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    organization TEXT NOT NULL,
    analit TEXT NOT NULL,
    genome TEXT NOT NULL,
    samples TEXT NOT NULL,
    mode TEXT NOT NULL,
    genes TEXT NOT NULL,
    comment TEXT NOT NULL
);