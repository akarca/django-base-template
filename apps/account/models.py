# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone




class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')
        email = CustomUserManager.normalize_email(email)
        user = self.model(email=email,
                          is_staff=False,
                          is_active=True,
                          is_superuser=False,
                          last_login=now,
                          **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u





class CustomUser(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (('f', u"Kadın"), ('m', u"Erkek"))

    email = models.EmailField(verbose_name=u'Email Adresi',
                              unique=True,
                              db_index=True,
                              help_text= """Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>.""")

    first_name = models.CharField(verbose_name=u'Ad',
                                  max_length=30,
                                  blank=True)

    last_name = models.CharField(verbose_name=u'Soyad',
                                 max_length=30,
                                 blank=True)

    date_of_birth = models.DateField(verbose_name=u"Doğum Tarihi",
                                     blank=True,
                                     null=True)

    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              verbose_name=u"Cinsiyet",
                              null=True,
                              blank=True)

    is_staff = models.BooleanField(verbose_name=u'Çalışan mı?',
                                   default=False)

    is_active = models.BooleanField(verbose_name=u'Aktif mi?',
                                    default=True)

    date_joined = models.DateTimeField(verbose_name=u'Üyelik Tarihi',
                                       default=timezone.now)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    class Meta:
        verbose_name = u"Kullanıcı"
        verbose_name_plural = u"Kullanıcılar"

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        warnings.warn("The use of AUTH_PROFILE_MODULE to define user profiles has been deprecated.",
            DeprecationWarning, stacklevel=2)
        if not hasattr(self, '_profile_cache'):
            from django.conf import settings
            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                                   self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    def welcome(self):
        return "Send welcome email"

