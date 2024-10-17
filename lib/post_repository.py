from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    # CREATE

    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content) VALUES (%s, %s)', [
                                post.title, post.content])
        return None
    
    # READ
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"],row["title"], row["content"])
            posts.append(item)
        return posts
    

    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE post_id = %s', [post_id])
        row = rows[0]
        return Post(row["title"], row["content"], row["post_id"])
