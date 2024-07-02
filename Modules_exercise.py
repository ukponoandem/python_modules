import requests
def my_post():
 
 post = requests.get("https://jsonplaceholder.typicode.com/posts")
 return post.text




    # ("https://jsonplaceholder.typicode.com/posts")