from django import forms

from Petstagram.main_app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            )
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter URL',
                }
            ),
            'date_of_birth': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter date of birth',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter e-mail',
                }
            ),
            # 'gender': forms.TypedChoiceField(
            #     choices=(('male', 'male'), ('femail', 'femail'), ('Do not show', 'Do not show')),
            #     initial='Do not show',
            #     # attrs={
            #     #     'class': 'form-control',
            #     #     # 'placeholder': 'Enter your gender',
            #     # }
            # ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write description about you',
                    'rows': 3,
                }
            )
        }
