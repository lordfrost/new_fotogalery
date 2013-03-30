import os, sys
sys.path.append('C:/Users/LordFrost/BitNami DjangoStack projects')
sys.path.append('C:/Users/LordFrost/BitNami DjangoStack projects/fotogalery')
os.environ['DJANGO_SETTINGS_MODULE'] = 'fotogalery.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
