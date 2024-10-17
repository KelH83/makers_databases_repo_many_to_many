from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/repo_many_to_many.sql")

post_repository = PostRepository(connection)
posts = post_repository.all()

for post in posts:
    print(post)