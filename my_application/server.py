from flask import Flask
from flask import redirect
app = Flask(__name__)
@app.route("/users")
def users():
   return redirect("http://jsonplaceholder.typicode.com/users")
@app.route("/posts")
def posts():
   return redirect("http://jsonplaceholder.typicode.com/posts")
@app.route("/albums")
def albums():
   return redirect("http://jsonplaceholder.typicode.com/albums")
@app.route("/comments")
def comments():
   return redirect("http://jsonplaceholder.typicode.com/comments")
@app.route("/photos")
def photos():
   return redirect("http://jsonplaceholder.typicode.com/photos")
@app.route("/todos")
def todos():
   return redirect("http://jsonplaceholder.typicode.com/todos")
if __name__ == "__main__":
   app.run(host="0.0.0.0")
