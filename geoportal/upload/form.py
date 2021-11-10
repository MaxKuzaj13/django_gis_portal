from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from .models import UploadFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('type', 'link_to_file')
        # labels = {'my label'}
        # help_texts = {'test help'}

        link_to_file = forms.FileField(
            label="Upload a file",
            help_text="Select the file to upload.",
            error_messages={
                "required": "Choose the file you exported"
            },
        )

        # def __init__(self, *args, **kwargs):
        #     super(UploadForm, self).__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout("file", Submit("submit", "Submit"))
