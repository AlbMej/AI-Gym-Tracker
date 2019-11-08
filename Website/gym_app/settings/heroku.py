from .settings import * #Import base settings

DEBUG = False
ADMINS = [('Alberto Mejia', 'albertomejia295@gmail.com')]


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage' #This alias has now been removed as per the 4.0 update.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
#AIPSA_USER = config('AIPSA_USER')
#AIPSA_PASS = config('AIPSA_PASS')
ALLOWED_HOSTS = ['rcos-gym-tracker.herokuapp.com', '127.0.0.1']
