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
    

    def find_by_tag(self, tag):
        rows = self._connection.execute(
            'SELECT posts.id, posts.title, posts.content FROM tags JOIN posts_tags ON posts_tags.tag_id = tags.id JOIN posts ON posts_tags.post_id = posts.id WHERE tags.tag_name = %s',[tag])
        row = rows[0]
        return Post(row["id"],row["title"], row["content"])
