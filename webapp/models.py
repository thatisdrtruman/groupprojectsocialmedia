from flask_login import UserMixin
from webapp import db
from werkzeug.security import generate_password_hash, check_password_hash


class PersistentStorage(db.Model):
	"""
	Database table for storing random values needed in the backend

	Attributes
		- self.id : str - (16 chars)
			database id string
		- self.content: str - (long text)
			data associated with the id
	"""
	#
	id = db.Column(db.String(32), primary_key=True)
	content = db.Column(db.Text)

	def __repr__(self):
		return f"PersistentStorage('{self.id}','{self.content}')"


class User(UserMixin, db.Model):
	"""
	Database table for storing login user information

	Attributes
		- self.id : str - (16 chars)
			user id string
		- self.username : str - (16 chars)
		- self.email : str - (255 chars)
		- self.password_hash : str - (255 chars)
		- self.password : str - (255 chars)
		- self.role : str - (16 chars)

	Methods
		- verify_password : compares the hash of the input password to the stored password hash
	"""
	id = db.Column(db.String(16), primary_key=True)
	username = db.Column(db.String(16), unique=True, nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	password_hash = db.Column(db.String(255), nullable=False)
	password = db.Column(db.String(255), nullable=False)
	role = db.Column(db.String(16))

	def __repr__(self):
		return f"User('{self.id}','{self.username}', '{self.email}', '{self.role}'"

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
