from django import forms
from django_quill.forms import QuillFormField
from django_summernote.widgets import SummernoteWidget

from shopconfigapp.models import Post, ShopItem


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {'content': SummernoteWidget(), }


class EditorForm(forms.Form):
    it_explain = forms.CharField(widget=SummernoteWidget())
    it_sub_explain = forms.CharField(widget=SummernoteWidget())


class QuillFieldForm(forms.Form):
    content = QuillFormField()

# class EditorForm(forms.ModelForm):
#     class Meta:
#         model = ShopItem
#         fields = ['it_explain', 'it_sub_explain', 'it_id', 'it_name']
#         widgets = {'it_explain': SummernoteWidget(), 'it_sub_explain': SummernoteWidget()}


# class EditorFormSub(forms.ModelForm):
#     class Meta:
#         model = ShopItem
#         fields = ['it_sub_explain']
#         widgets = {'it_sub_explain': SummernoteWidget(), }
