"""
Forms and validation code for user profile.
"""
#import custom user model
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User
else:
    User = get_user_model()


from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
import mimetypes, urllib
from profiles.countries import CountryField


class AccountForm(forms.ModelForm):
    """
    Account Settings Form, Composed of
    username, email,is_private, location,latitude,longitude,country
    """
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileForm(forms.ModelForm):
    """
    Profile Form. Composed of
    first_name,last_name,date_of_birth,gender,website,twitter,description
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'gender')