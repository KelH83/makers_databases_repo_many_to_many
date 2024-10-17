from lib.post_repository import PostRepository
from lib.post import Post


def test_get_all_records(db_connection): 
    db_connection.seed("seeds/repo_many_to_many.sql") 
    repository = PostRepository(db_connection)

    posts = repository.all() 

    assert posts == [
        Post(1,'Apple VS Samsung', 'Which phone to get in 2024'),
        Post(2,'My favourite pet', 'My cat Twyla is clearly the best out of all my pets'),
        Post(3,'Rainbow', 'Red, Yellow, Pink, Green, etc etc')
    ]

def test_find_by_tag(db_connection):
    db_connection.seed("seeds/repo_many_to_many.sql")
    repository = PostRepository(db_connection)

    post = repository.find_by_tag("Mobiles")
    assert post == Post(1, "Apple VS Samsung", "Which phone to get in 2024")

