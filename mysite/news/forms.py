from django import forms
from .models import Category, News


class NewsForm_old(forms.Form):              #Вариант, где форма не связана с моделью
    title = forms.CharField(max_length=150,
                            label='Заголовок',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label='Контент',
                              required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
                              )
    is_published = forms.BooleanField(label='Опубликовано', initial=True)
    category = forms.ModelChoiceField(empty_label='Выберите категорию',
                                      queryset=Category.objects.all(),
                                      label='Категория',
                                      widget=forms.Select(attrs={"class": "form-control"}))



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
