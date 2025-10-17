from slowapi import Limiter
from slowapi.util import get_remote_address

# Create a Limiter instance using the client's remote address as the key.
# This module is purposely small so both `app.main` and route modules can import
# the same `limiter` instance without causing circular imports.
limiter = Limiter(key_func=get_remote_address)
