DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title varchar(250),
  content varchar(250)
);

INSERT INTO posts (title, content) VALUES ('Apple VS Samsung', 'Which phone to get in 2024');
INSERT INTO posts (title, content) VALUES ('My favourite pet', 'My cat Twyla is clearly the best out of all my pets');
INSERT INTO posts (title, content) VALUES ('Rainbow', 'Red, Yellow, Pink, Green, etc etc');
