from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from praticando.errors.exceptions import AcessoNegado

def role_required(role):
	def decorator(fn):
		
		@wraps(fn)

		def wrapper (*args, **kwargs):

			verify_jwt_in_request()

			claims = get_jwt()

			if claims['role'] != role:
				raise AcessoNegado()
			return fn (*args, **kwargs)

		return wrapper

	return decorator