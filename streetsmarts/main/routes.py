from flask import render_template, request, Blueprint
from streetsmarts import  db #added
from streetsmarts.models import Post, User, RecordsMetadata, PidstoreRecid
import json


#FOR CONTROLLERS 😁
from sqlalchemy import select #, create_engine
from sqlalchemy.sql.expression import func, literal

#import folium


main = Blueprint('main', __name__)



@main.route('/')  #decorator
def index():
    return render_template('index.html')


@main.route('/home')
def home():
    return render_template('index.html')


@main.route('/map')
def map():
    #start_coords = (14.6091, 121.0223)
    #folium_map = folium.Map(location=start_coords, zoom_start=14)
    #return folium_map._repr_html_()
    return render_template('map.html')

@main.route('/map_grocery')
def map_grocery():
    return render_template('map_grocery.html')

@main.route('/map_educ')
def map_educ():
    return render_template('map_educ.html')

@main.route('/map_security')
def map_security():
    return render_template('map_security.html')

@main.route('/map_finance')
def map_finance():
    return render_template('map_finance.html')

@main.route('/map_transpo')
def map_transpo():
    return render_template('map_transpo.html')

# @main.route('/map_health')
# def map_health():
#     return render_template('map_health.html')

@main.route('/map_health')
def map_health():
    #start_coords = (14.6091, 121.0223)
    #folium_map = folium.Map(location=start_coords, zoom_start=14)
    #return folium_map._repr_html_()
    return render_template('map_health.html')


@main.route('/map_single')
def map_single():
    #start_coords = (14.6091, 121.0223)
    #folium_map = folium.Map(location=start_coords, zoom_start=14)
    #return folium_map._repr_html_()
    return render_template('map_single.html')

@main.route('/posts')
def posts():

    page = request.args.get('page', 1, type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)

    return render_template('posts.html', posts=post)