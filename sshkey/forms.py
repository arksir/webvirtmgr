import re

from django import forms
from django.utils.translation import ugettext_lazy as _

# from sshkey.models import SSHKey


class SSHKeyUpdateForm(forms.Form):
    value = forms.CharField(error_messages={'required': _('No SSH Key has been entered')},
                            max_length=5000)

    # def clean_value(self):
    #     value = self.cleaned_data['value']
    #     try:
    #         SSHKey.objects.get(name="id_ras")
    #     except SSHKey.DoesNotExist:
    #         return value
    #     raise forms.ValidationError(_('This SSH Key is already connected'))
