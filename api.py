from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! <h1>HELLO</h1>"

app.route("/<name>")
def user(name):
    return f"Name: {name}"

if (__name__ == "__main__"):
    app.run()


# from flask import Flask, request, render_template,jsonify
# from flask import render_template, url_for, request, redirect
# import scraper

# app = Flask(__name__)


# app.route("/")
# def home():
#     return render_template("home.html")

# # app.route("/login", methods=["POST", "GET"])
# # def login():
# #     if request.method == "POST":
# #         username = request.form["name"]
# #         # password = request.form["password"]
# #         return redirect(f"/profile/{username}")
# #     # else:
# #     #     return render_template("form.html")

# # app.route("/profile/<username>")
# # def profile(username):
# #     return f"<h1>{username}</h1>"

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)

# # # TODO: Get return v=alue from this function
# # def begin_scrape(username,password):
# #    scraper.start_scraping(username, password)

# # def do_something(text1,text2):
# #    text1 = text1.upper()
# #    text2 = text2.upper()
# #    combine = text1 + text2
# #    return combine 

# # def form():
# #     return render_template('form.html')
 
# # @app.route('/verify', methods = ['POST', 'GET'])
# # def verify():
# #     if request.method == 'POST':
# #         name = request.form['name']
# #         return redirect(f"/user/{name}")
 
# # @app.route('/user/<name>')
# # def user(name):
# #     return f"Your name is {name}"

# # @app.route('/join', methods=['GET','POST'])
# # def my_form_post():
# #     text1 = request.form['text1']
# #     word = request.args.get('text1')
# #     text2 = request.form['text2']
# #     combine = do_something(text1,text2)
# #     result = {
# #         "output": combine
# #     }
# #     result = {str(key): value for key, value in result.items()}
# #     return jsonify(result=result)

# # @app.route('/form', methods=['GET','POST'])
# # def form():
# #     if request.method == 'POST':
# #     return render_template('display-test.html', glon=glon)





# # @app.route('/form', methods=['GET','POST'])
# # def form():
# #     if request.method == 'POST':
# #         glon = request.form['username']
# #         return redirect(url_for('return_form',glon=glon))

# #     return render_template('display-test.html', glon=glon)


# # @app.route('/return_form', methods = ['GET', 'POST'])
# # def form():
# #     if request.method == 'POST':
# #         glon = request.form['username']
# #         return render_template('display-test.html', glon=glon)

# # if __name__ == '__main__':
# #     app.run(debug=True, host='0.0.0.0', port=5000)


# #redirect testing - Rohan

