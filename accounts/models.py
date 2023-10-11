
# Create your models here.
from datetime import timedelta
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# from django.template.defaultfilters import slugify
        
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    full_name       = models.CharField(_('full name'), max_length=30)
    email           = models.EmailField(_('email address'), unique=True,blank=True)
    phone_no        = models.CharField(_("Phone no"),max_length=10,unique=True)
    is_staff        = models.BooleanField(_('staff status'), default=False)
    is_active       = models.BooleanField(_('active'), default=True)
    date_joined     = models.DateTimeField(_('date joined'),default=timezone.now)
    is_engineer    = models.BooleanField(_('engineer'), default=False)
    is_labour     = models.BooleanField(_('labour'), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_no'
    REQUIRED_FIELDS = ['full_name',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self): 
        return self.phone_no

    def __str__(self): 
        return self.full_name

    # def clean(self):
    #     super().clean()
    #     self.phone_no = self.__class__.phone_no


YEARS_OF_EXP = (
    ('entry', 'Entry Level'),
    ('1-2', '1-2 years'),
    ('3-5', '3-5 years'),
    ('6-10', '6-10 years'),
    ('above 10', 'Above 10 years')
)

GENDERS = (
    ('male', 'Male'),
    ('female', 'Female')
)

CATEGORY = (
    ('Flooring ','FLOORING'),
    ('Plumbing','PLUMBING'),
    ('Fitting','FITTING'),
    ('Other','OTHER'),
)

CERTIFICATES = (
    ('', 'Entry Level'),
    ('1-2', '1-2 years'),
    ('3-5', '3-5 years'),
    ('6-10', '6-10 years'),
    ('above 10', 'Above 10 years')
)

class Labour(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    # interest        = models.ForeignKey(Industry, on_delete=models.SET_NULL, blank=True, null=True)
    # date_of_birth   = models.DateField(null=True, blank=True)
    location        = models.CharField(_('Where do you Reside now'), max_length=20, null=True, blank=True)
    gender          = models.CharField(max_length=10, choices=GENDERS, null=True, blank=True)
    about           = models.CharField(max_length=40,blank=True, null=True)
    category        = models.CharField('Select your work type :',max_length=20,choices=CATEGORY,null=True, blank=True)
    years_of_exp    = models.CharField('Years of Experience', max_length=20, choices=YEARS_OF_EXP, null=True, blank=True)
    is_hired = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.full_name

class Engineer(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    name        = models.CharField(_('NAME'), max_length=50, null=True, blank=True)
    # description = models.TextField(_(''), null=True, blank=True)
    # website     = models.URLField(_('company webite'), null=True, blank=True)
    country     = models.CharField(max_length=40, null=True, blank=True)
    state       = models.CharField(max_length=40, null=True, blank=True)
    address     = models.CharField(_('company address'), max_length=120, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Engineer'
    
    def __str__(self):
        return self.name


class Hired(models.Model):
    eng_id=models.ForeignKey(Engineer,on_delete=models.CASCADE)
    labr_id=models.ForeignKey(Labour,on_delete=models.CASCADE)
    

# class HiringLabour(models.Model):
#     category = models.ForeignKey(Labour,on_delete=models.CASCADE)
#     state = models.CharField('State',max_length=20,blank=True)
#     city = models.CharField('State',max_length=20,blank=True)

# # Get the  list of all available labours
#     def get_listoflabours():
#         return Labour.objects.all()

# # Get the  list of all available labours under selected category

#     def get_list_by_ctg(ctgry):
#         if ctgry:
#             return Labour.objects.filter(category=ctgry)
#         else:
#             return HiringLabour.get_listoflabours()

