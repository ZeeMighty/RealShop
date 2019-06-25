from django import forms
from .models import Good_Get, Good
from HiPage import views

class GoodGet(forms.ModelForm):
    class Meta:
        model = Good_Get
        Size = forms.ModelChoiceField(queryset = Good.objects.all())
        fields = '__all__'

        widgets = {
            'Name': forms.TextInput(attrs = {'type': 'hidden'}),
            'Photo': forms.ClearableFileInput(attrs = {'type': 'hidden'}),
            'Price': forms.TextInput(attrs = {'type': 'hidden'}),
        }

    def __init__(self, *args, good_id1=None, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        if good_id1 is not None:
            obj = Good.objects.filter(id = good_id1)
            img = Good.objects.get(id=good_id1)
#            self.fields['Name'].initial = Good.objects.get(id=good_id1)
            self.fields['Photo'].initial = img.Photo.url
#            self.fields['Price'].initial = Good.objects.get(id=good_id1)
            for good in obj:
                good_sizes = good.Size.all()
            self.fields['Size'].queryset = good_sizes
