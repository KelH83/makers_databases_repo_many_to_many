from lib.post import Post

def test_post_constructs():
    post = Post(1,"Day 1", "Started Makers bootcamp")
    assert post.id == 1
    assert post.title == "Day 1"
    assert post.content == "Started Makers bootcamp"

def test_posts_format_nicely():
    post = Post(1,"Day 1", "Started Makers bootcamp")
    assert str(post) == "Title:Day 1,Content:Started Makers bootcamp,Post ID:1"