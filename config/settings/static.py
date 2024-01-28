import os

from .const import BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static/"
# COMPRESS_ROOT = STATIC_ROOT
COMPRESS_ENABLED = True
STATICFILES_FINDERS = ("compressor.finders.CompressorFinder",)
# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
