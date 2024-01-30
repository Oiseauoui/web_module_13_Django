# users/forms.py
from django import forms
from .models import Author, Quote, Tag


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
         )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.all()

    def clean_tags(self):
        return self.cleaned_data['tags']


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

