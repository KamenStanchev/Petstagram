from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.main_app.validator import only_letters_validator

""""Profile
The user must provide the following information in their profile:
•	The first name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
•	The last name - it should have at least 2 chars, max - 30 chars, and should consist only of letters.
•	Profile picture - the user can link their picture using a URL.

The user may provide the following information in their profile:
•	Date of birth: day, month, and year of birth.
•	Description - a user can write any description about themselves, no limit of words/chars.
•	Email - a user can only write a valid email address.
•	Gender - the user can choose one of the following: "Male", "Female", and "Do not show".
"""


class Profile(models.Model):

    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
            only_letters_validator,
        )
    )

    picture = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=30,
        choices=(('male', 'male'), ('femail', 'femail'), ('Do not show', 'Do not show')),
        null=True,
        blank=True
    )



