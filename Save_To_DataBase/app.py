import menu
from database import Database
from models.blog import Blog
from models.post import Post

Database.initialize()

# post = Post(blog_id = "123",
#             title = "Another Great Post",
#             content = "Example content",
#             author = "Bikash"
#             )
#
# post.save_to_mongo()


#print(Post.from_mongo('478662af349149cb9532cad3712b62c7'))

# posts = Post.from_blog("123")
#
# for post in posts:
#     print(post)

# blog = Blog(author="Bikash",
#             title="Sample Title",
#             description="Sample Description")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.get_from_mongo(blog.id)
#
# print(blog.get_posts())

menu = menu.Menu()
menu.run_menu()