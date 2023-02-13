from django import forms
from .models import Profile
from .models import Comment


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))

    class Meta:
        model = Profile
        fields = ['avatar', 'about']
        
        
class AddComment(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ваш коментар тут...', 
                                                    'class': 'form-control'}))
    
    class Meta:
        model = Comment
        fields = ['content']