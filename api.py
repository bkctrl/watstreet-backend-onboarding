from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) 
api = Api(app)

class TravelWishlist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  attractions = db.Column(db.String(255), nullable=False)
  best_time_to_visit = db.Column(db.String(50), nullable=False)
  visited = db.Column(db.Boolean, default=False)

  def __repr__(self):
    return f"<Place(name={self.name}, visited={self.visited})>"

place_args = reqparse.RequestParser()
place_args.add_argument('name', type=str, required=True, help="Place name is required")
place_args.add_argument('attractions', type=str, required=True, help="Attractions are required")
place_args.add_argument('best_time_to_visit', type=str, required=True, help="Best time to visit is required")
place_args.add_argument('visited', type=bool, required=False, help="Visited status")

placeFields = {
  'id': fields.Integer,
  'name': fields.String,
  'attractions': fields.String,
  'best_time_to_visit': fields.String,
  'visited': fields.Boolean,
}

class Wishlist(Resource):
  @marshal_with(placeFields)
  def get(self):
    places = TravelWishlist.query.all() 
    return places

  @marshal_with(placeFields)
  def post(self):
    args = place_args.parse_args()
    place = TravelWishlist(
      name=args['name'],
      attractions=args['attractions'],
      best_time_to_visit=args['best_time_to_visit'],
      visited=args.get('visited', False),
    )
    db.session.add(place)
    db.session.commit()
    return place, 201

class WishlistItem(Resource):
  @marshal_with(placeFields)
  def get(self, id):
    place = TravelWishlist.query.filter_by(id=id).first()
    if not place:
      abort(404, message="Place not found")
    return place

  @marshal_with(placeFields)
  def put(self, id):
    args = place_args.parse_args()
    place = TravelWishlist.query.filter_by(id=id).first()
    if not place:
      abort(404, message="Place not found")
    place.name = args['name']
    place.attractions = args['attractions']
    place.best_time_to_visit = args['best_time_to_visit']
    place.visited = args.get('visited', place.visited)
    db.session.commit()
    return place

  @marshal_with(placeFields)
  def delete(self, id):
    place = TravelWishlist.query.filter_by(id=id).first()
    if not place:
      abort(404, message="Place not found")
    db.session.delete(place)
    db.session.commit()
    return TravelWishlist.query.all()

api.add_resource(Wishlist, '/api/wishlist/')
api.add_resource(WishlistItem, '/api/wishlist/<int:id>')

@app.route('/')
def home():
  return '<h1>Welcome to the Travel Wishlist API</h1>'

if __name__ == '__main__':
  app.run(debug=True)
