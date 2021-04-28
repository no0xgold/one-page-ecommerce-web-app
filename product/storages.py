from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.files.storage import FileSystemStorage
PROTECTED_MEDIA = getattr(settings, 'PROTECTED_MEDIA', None)
if  PROTECTED_MEDIA==None:
    raise ImproperlyConfigured(f'PROTECTED_MEDIA is not set yet.')


class ProtectedStorage(FileSystemStorage):
    location =PROTECTED_MEDIA #to MEDIA_ROOT