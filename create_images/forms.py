from django import forms
from create_images.models import Images

class Upload_image_form(forms.ModelForm):
    class Meta:
		model=Images
