from django import forms
from .models import Follower, ContCreator


class FollowerForm(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ('f_name', 'city', 'state', 'zipcode', 'email', 'phone_number')

class CreatorForm(forms.ModelForm):
    class Meta:
        model = ContCreator
        fields = ('cc_name', 'city', 'state', 'zipcode', 'email', 'phone_number')
