#import from python lib
import re
#import from Django
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

GENDER_CHOICES = (('M', _('Male')), ('F', _('Female')),)

class UserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(username=username, email = UserManager.normalize_email(email),
                          is_staff=False, is_active=True, is_superuser=False,
                          last_login=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(username, email, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    #default profile
    username = models.CharField(_('username'), max_length=30, unique=True, db_index=True,
        help_text=_('Required. 30 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'),
        validators=[
            validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid')
        ])
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    date_of_birth = models.DateField('date of birth', blank=True, null=True)
    gender = models.CharField(_('Gender'),max_length=1, choices=GENDER_CHOICES, blank=True, null=True)

    #user permissions
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return _("%s's profile") % self.username

    def get_absolute_url(self):
        return reverse('user_profile', args=[self.username])

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

