
from django import forms

from .models import arecord_users

class PostForm(forms.ModelForm):

    class Meta:
        model = arecord_users
        fields = ('domain_name','redirect_to_url', 'region','permanent','parameter_copy','request_path','domain_type','status','updated_date','ssl_status')
