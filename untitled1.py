from flask import Flask, render_template

app = Flask(__name__)
class Movie:
    def __init__(self,title,img):
        self.title=title
        self.img=img
movie1 = Movie("angry bird","https://i.ytimg.com/vi/oenxgUiNOYA/maxresdefault.jpg")
movie2 = Movie("The secrets life of pet","http://share.thesecretlifeofpets.com/site-content/uploads/2016/04/SurprisedThumb_600x324-1-600x324.jpg")
movies = [
            Movie("angry bird", "https://i.ytimg.com/vi/oenxgUiNOYA/maxresdefault.jpg"),
            Movie("The secrets life of pet",
                  "http://share.thesecretlifeofpets.com/site-content/uploads/2016/04/SurprisedThumb_600x324-1-600x324.jpg")]

@app.route('/')
def hello_world():
    return 'Hello Linh!'

@app.route('/c4e')
def hello_C4E():
    return 'Hello C4E!'

@app.route('/c4e/1')
def hello_team1():
    return 'Hello Hoang+Hoang'
@app.route('/<name>')
#<name> argument: mở các post khác nhau
def hello(name):
    return ('Hello' +name)
@app.route('/movie')
def get_movie():
    return render_template('movie.html')
@app.route('/movie2')
def get_movie2():
    return render_template('movie_2.html',
                           title='civil war',
                           img="http://media.comicbook.com/2016/04/civil-war-cap-tony-179110.jpg")
@app.route('/movies')
def get_movies():
    return render_template('movies.html',
                           movie_list=movies,
                           )

if __name__ == '__main__':
    app.run()
