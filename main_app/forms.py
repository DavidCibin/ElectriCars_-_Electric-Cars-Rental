from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

from django.forms import ModelForm
from .models import Booking


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)



class BookingForm(ModelForm):
  class Meta:
    model = Booking
    fields = ['start_date', 'end_date', 'total', 'insurance']

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['phone', 'address1', 'city', 'state', 'zipcode']    