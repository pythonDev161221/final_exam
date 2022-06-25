from django import forms

from webapp.models import Announce


class AnnounceForm(forms.ModelForm):
    class Meta:
        model = Announce
        exclude = ["status", "published_at", "author"]


class AnnounceModerForm(forms.ModelForm):
    class Meta:
        model = Announce
        fields = ["status"]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")