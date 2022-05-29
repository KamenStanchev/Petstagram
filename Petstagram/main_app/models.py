from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.main_app.validator import only_letters_validator


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

    picture = models.URLField(
        null=True,
        blank=True
    )
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
    def __str__(self):
        return self.first_name


# Pet
# The user must provide the following information when adding a pet in their profile:
# •	Name - it should consist of maximum 30 characters. All pets' names should be unique for that user.
# •	Type - the user can choose one of the following: "Cat", "Dog", "Bunny", "Parrot", "Fish", or "Other".
# The user may provide the following information when adding a pet to their profile:
# •	Date of birth - pet's day, month, and year of birth.


class Pet(models.Model):
    TYPES = [(x, x) for x in ("Cat", "Dog", "Bunny", "Parrot", "Fish", "Other")]
    name = models.CharField(max_length=30)
    type = models.CharField(
        max_length=max(len(x) for (x, y) in TYPES),
        choices=TYPES
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return self.name
