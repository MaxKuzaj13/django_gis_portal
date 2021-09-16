from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from .models import UploadFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('file', 'layer', 'type', 'link_to_file')
        # labels = {'my label'}
        # help_texts = {'test help'}

        link_to_file = forms.FileField(
            label="Upload a file",
            help_text="Select the CSV file to upload.",
            error_messages={
                "required": "Choose the CSV file you exported from the spreadsheet"
            },
        )

        def __init__(self, *args, **kwargs):
            super(UploadForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.layout = Layout("file", Submit("submit", "Submit"))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Save file'))

        # def __init__(self, *args, **kwargs):
        #     super(UploadForm, self).__init__(*args, **kwargs)
        #     self.helper = FormHelper()
        #     self.helper.layout = Layout("file", Submit("submit", "Submit"))