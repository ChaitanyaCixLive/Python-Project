from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter your name: ")
        self.user_blog = None

        if(self._user_has_account()):
            print("Welcome Back {}".format(self.user))
        else:
            self._promt_user_for_account()


    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author':self.user})

        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            return  False

    def _promt_user_for_account(self):
        title = input("Enter the blog title: ")
        description = input("Enter the description for the blog: ")

        blog = Blog(self.user,title, description)
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Do you want to read or write bolgs: (R/W) ")
        if read_or_write == 'R':
            pass

        elif read_or_write =='W':
            self.user_blog.new_post()

        else:
            print("Thansk for Blogging")


