import os
import re

class Blog:
    def posts_json(self):
        data={}
        directory='./cards/static/db/blog'
        pattern='[\w-]+?(?=\.)'
        for filename in os.scandir(directory):
            if filename.is_file():
                idPost=re.search(pattern, filename.path)
                id=idPost.group()
                with open(filename.path) as f:
                    contents=f.readlines()
                
                    for content in contents:
                        post_array=content.split(':')
                        print(post_array[0], post_array[1], post_array[2])
                        data[id]={'title': post_array[0], 'subtitle': post_array[1], 'content': post_array[2]}
        return data

class Post:
    def post_json(self, idpost):
        data={}
        directory='./cards/static/db/blog'
        pattern='[\w-]+?(?=\.)'
        for filename in os.scandir(directory):
            if filename.is_file():
                idPost=re.search(pattern, filename.path)
                id=idPost.group()
                if id==idpost:
                    with open(filename.path) as f:
                        contents=f.readlines()
                        for content in contents:
                            post_array=content.split(':')
                            print(post_array[0], post_array[1], post_array[2])
                            data[id]={'title': post_array[0], 'subtitle': post_array[1], 'content': post_array[2]}
                            return data
                else:
                    continue
        return data