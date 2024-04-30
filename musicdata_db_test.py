import pymysql
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import os

db = SQLAlchemy()
app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)


class Track(db.Model):
    __tablename__ = 'toptracks_final'
    billboard_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    artist = db.Column(db.String)
    featuring = db.Column(db.String)
    album_name = db.Column(db.String)
    release_date = db.Column(db.String)
    streaming_revenue_spotify = db.Column(db.Integer)
    alltime_spotify_streams = db.Column(db.Integer)
    genre = db.Column(db.String(255))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track/<int:billboard_id>')
def track_detail(billboard_id):
    track = Track.query.get_or_404(billboard_id)
    return render_template('track_detail.html', track=track)

@app.route('/genre/<genre_name>')
def genre(genre_name):
    try:
        tracks = db.session.query(Track).filter_by(genre=genre_name).all()  
        return render_template('genre.html', tracks=tracks, genre_name=genre_name)
    except Exception as e:
        return f"Error occurred: {str(e)}"

    
@app.route('/pop')
def pop():
    try:
        tracks = db.session.query(Track).filter_by(genre='Pop').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Pop')
    except Exception as e:
        return f"Error occurred: {str(e)}"


@app.route('/country')
def country():
    try:
        tracks = db.session.query(Track).filter_by(genre='Country').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Country')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    

@app.route('/rnb')
def rnb():
    try:
        tracks = db.session.query(Track).filter_by(genre='RnB').all()  
        return render_template('genre.html', tracks=tracks, genre_name='RnB')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@app.route('/reggaeton')
def reggaeton():
    try:
        tracks = db.session.query(Track).filter_by(genre='Reggaeton').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Reggaeton')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@app.route('/indie')
def indie():
    try:
        tracks = db.session.query(Track).filter_by(genre='Indie').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Indie')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@app.route('/rap')
def rap():
    try:
        tracks = db.session.query(Track).filter_by(genre='Rap').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Rap')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@app.route('/holiday')
def holiday():
    try:
        tracks = db.session.query(Track).filter_by(genre='Holiday').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Holiday')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@app.route('/kpop')
def kpop():
    try:
        tracks = db.session.query(Track).filter_by(genre='K-Pop').all()  
        return render_template('genre.html', tracks=tracks, genre_name='K-Pop')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
@app.route('/afrobeats')
def afrobeats():
    try:
        tracks = db.session.query(Track).filter_by(genre='Afrobeats').all()  
        return render_template('genre.html', tracks=tracks, genre_name='Afrobeats')
    except Exception as e:
        return f"Error occurred: {str(e)}"
    
    
if __name__ == '__main__':
    app.run(debug=True)
