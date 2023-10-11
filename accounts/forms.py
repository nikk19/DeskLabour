from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm

from django.db import transaction
from django.contrib.auth import get_user_model
# from django.forms.models import model_to_dict
from .models import Labour,Engineer

User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ('phone_no','full_name','email')
        
        # exclude =['email']

    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name','phone_no', 'email','password', 'is_active', 'is_superuser',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class EngineerSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password'}))
    name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    country=forms.CharField(max_length=12,required=True,widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    state=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder': 'State'}))
    # address=forms.Textarea



    class Meta:
        model = User
        fields = ('phone_no','full_name','email',)
        # exclude = ['email']
        # model2 = Engineer
        # fields2 = ('name','country','state','address')

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        qs = User.objects.filter(phone_no=phone_no)
        if qs.exists():
            raise forms.ValidationError("This Phone number already exists")
        return phone_no

    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        print(password1)
        print(password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_engineer = True
        user.save()
        engg = Engineer.objects.create(user=user)
        engg.name=self.cleaned_data.get('name')
        engg.country=self.cleaned_data.get('country')
        engg.state=self.cleaned_data.get('state')
        engg.address=self.cleaned_data.get('address')
        engg.save()
        return user


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
class LabourSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    location=forms.CharField(max_length=20)
    gender=forms.ChoiceField(choices=GENDERS)
    about=forms.CharField(widget=forms.Textarea)
    yearsofexp=forms.ChoiceField(choices=YEARS_OF_EXP)
    category = forms.ChoiceField(choices=CATEGORY)
    # address=forms.Textarea



    class Meta:
        model = User
        fields = ('phone_no','full_name','email',)
        # model2 = Engineer
        # fields2 = ('name','country','state','address')

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        qs = User.objects.filter(phone_no=phone_no)
        if qs.exists():
            raise forms.ValidationError("This Phone number already exists")
        return phone_no

    def clean_password2(self):
        data = self.cleaned_data
        password1 = data.get('password1')
        password2 = data.get('password2')
        print(password1)
        print(password2)
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('The passwords you entered are not the same')
        return password1

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_labour = True
        user.save()
        labr = Labour.objects.create(user=user)
        labr.gender=self.cleaned_data.get('gender')
        labr.location=self.cleaned_data.get('location')
        labr.about=self.cleaned_data.get('about')
        labr.years_of_exp=self.cleaned_data.get('yearsofexp')
        labr.category=self.cleaned_data.get('category')
        labr.save()
        return user



#-------------------APJ Method----------------------
class FilterForm(forms.Form):
    Category = forms.ChoiceField(choices = CATEGORY,widget=forms.Select(attrs = {'class':'form-control','style': 'max-width: 300px;'}))
    City = forms.CharField(max_length=100,widget=forms.TextInput(attrs = {'class':'form-control','style': 'max-width: 300px;'}))
    # hat= forms.MultipleChoiceField()

class CheckboxesForm(forms.Form):
    def __init__(self,category,city ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['checkboxes'] = forms.ModelMultipleChoiceField(
            queryset=Labour.objects.filter(category = category, location__icontains = city,is_hired = False), widget=forms.CheckboxSelectMultiple())


#-------------------APJ Method----------------------


class LoginForm(forms.Form):
    phone_no =forms.CharField(max_length=10)
    password =forms.CharField(widget=forms.PasswordInput)


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Labour
        fields =['location','about','category','years_of_exp','is_hired']
        labels = {'location':'City','about':'Tell About Yourself',}

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['full_name','phone_no']
        labels = {'full_name':'Name','phone_no':'Mobile Number',}


class EngProfileform(forms.ModelForm):
    class Meta:
        model = Engineer
        fields = ['country','state','address']
        labels = {'country':'Country','state':'State','address':'Address'}


        



    

# class EngineerForm(forms.ModelForm):
#     date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
#     class Meta:
#         model = Engineer
#         fields = ('name','country','state','address')





    





