
from decouple import config

EMAIL_BACKEND = config('EMAIL_BACKEND', cast=str)
EMAIL_HOST = config('EMAIL_HOST', cast=str)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', cast=str)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
SERVER_EMAIL = config('SERVER_EMAIL', cast=str)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', cast=str)