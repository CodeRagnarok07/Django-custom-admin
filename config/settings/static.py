import os

from .const import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static/"

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)


MEDIA_ROOT = "/media/"

MEDIA_ROOT = BASE_DIR / "media/"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }