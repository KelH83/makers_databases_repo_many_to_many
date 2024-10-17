DROP TABLE IF EXISTS posts_tags;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS tags;

CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title varchar(250),
  content varchar(250)
);

INSERT INTO posts (title, content) VALUES ('Apple VS Samsung', 'Which phone to get in 2024');
INSERT INTO posts (title, content) VALUES ('My favourite pet', 'My cat Twyla is clearly the best out of all my pets');
INSERT INTO posts (title, content) VALUES ('Rainbow', 'Red, Yellow, Pink, Green, etc etc');


CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  tag_name varchar(250)
);

INSERT INTO tags (tag_name) VALUES ('Mobiles');
INSERT INTO tags (tag_name) VALUES ('Animals');
INSERT INTO tags (tag_name) VALUES ('Nature');

CREATE TABLE posts_tags (
  post_id int,
  tag_id int,
  constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
  constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
  PRIMARY KEY (post_id, tag_id)
);

INSERT INTO posts_tags (post_id, tag_id) VALUES (1,1);
INSERT INTO posts_tags (post_id, tag_id) VALUES (2,2);
INSERT INTO posts_tags (post_id, tag_id) VALUES (3,3);