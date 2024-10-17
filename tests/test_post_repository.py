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

# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/repo_many_to_many.sql")
#     repository = PostRepository(db_connection)

#     post = repository.find("Kelly Howes")
#     assert post == Post("Kelly Howes", "Sept 2024 foundations ra")

# def test_create_record(db_connection):
#     db_connection.seed("seeds/repo_many_to_many.sql")
#     repository = PostRepository(db_connection)

#     repository.create(Post("Kiyomi Dogue", "Barker"))

#     result = repository.all()
#     assert result == [
#         Post("Kelly Howes", "Sept 2024 foundations ra"),
#         Post("Kimiko Dogue", "Walkies"),
#         Post("Twyla Kitty", "Purrfect"),
#         Post("Yuki Snake", "Cornucopia"),
#         Post("Kiyomi Dogue", "Barker")
#     ]

