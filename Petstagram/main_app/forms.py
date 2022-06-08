import form as form
from django import forms

from Petstagram.main_app.models import Profile, Pet, PetPhoto


class DateInput(forms.DateInput):
    input_type = 'date'


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01',
                }),
        }


class EditPetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter pet name',
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01',
                }),
        }


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'tagged_pets')
        # widgets = {
        #     'photo': forms.ImageField(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'description': forms.Textarea(
        #         attrs={
        #             'class': 'form-control',
        #         }
        #     ),
        #     'tagged_pets': forms.CheckboxInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #     )
        # }


class DeletePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'disabled': True,
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control',
                    'disabled': True,
                }
            ),
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'disabled': True,
                }),
        }


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
            'date_of_birth': DateInput(
                attrs={
                    'class': 'form-control',
                    'min': '1920-01-01',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter e-mail',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write description about you',
                    'rows': 3,
                }
            )
        }
