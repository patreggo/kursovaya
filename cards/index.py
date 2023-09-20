from flask import Flask, render_template, request, redirect
from api import Blog, Post

app=Flask(__name__)
posts=Blog()
post=Post()
login='artem'
password='123'
isAdmin=False


@app.route('/api/blog')
def api_blog():
    return posts.posts_json()

@app.route('/api/blog/<postid>/')
def api_blog_post(postid):
    return post.post_json(postid)








@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<postid>/')
def blog_post(postid):
    return render_template('post.html')
    



@app.route('/admin', methods=['POST', 'GET'])
def log_in():
    return render_template('adminlogin.html')

@app.route('/admin/login', methods=['POST', 'GET'])
def adminLogin():
    if request.method=='POST':
        loginrequest=request.form['login']
        passwordrequest=request.form['password']
        if loginrequest==login and passwordrequest==password:
            print('success')
            global isAdmin
            isAdmin=True
            return redirect('/adminka')
        else:
            return ('Неверный логин или пароль')
        
@app.route('/adminka', methods=['POST', 'GET'])
def adminka():
    
    if isAdmin==True:
        return render_template('admin.html')
    else:
        return 'Ты больше не армянин'

@app.route('/adminka/post/add',methods=['POST', 'GET'])
def addpost():
    if request.method=='POST':
        title=request.form['title']
        subtitle=request.form['subtitle']
        content=request.form['content']
        add_post=open(f'./cards/static/db/blog/{title}.txt','w+')
        add_post.write(f'{title}:{subtitle}:{content}')
        add_post.close()
        return redirect(f'/blog/{title}')
    

if __name__ == '__main__':
    app.run(port=8000, debug = True)