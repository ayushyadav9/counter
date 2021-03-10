from django import forms
from .models import WordsModel,ChangeModel,FindModel

class WordsForm(forms.ModelForm):
    class Meta:
        model = WordsModel
        fields = ("method","text","result")

class ChangeForm(forms.ModelForm):
    class Meta:
        model=ChangeModel
        fields=("method2","input","output")

class FindForm(forms.ModelForm):
    class Meta:
        model=FindModel
        fields=("method3","word_to_find","paragraph","occurances")
