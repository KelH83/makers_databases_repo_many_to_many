from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/repo_many_to_many.sql")

# # Retrieve all studentss
post_repository = PostRepository(connection)
posts = post_repository.all()

# # List them out
for post in posts:
    print(post)