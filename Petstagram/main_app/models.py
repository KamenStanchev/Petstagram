from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.main_app.validator import only_letters_validator, validate_file_max_size


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

''''
Pet's Photo
The user must provide the following information when uploading a pet's photo in their profile:
•	Photo - the maximum size of the photo can be 5MB
•	Tagged pets - the user should tag at least one of their pets. There is no limit in the number of tagged pets
The user may provide the following information when uploading a pet's photo in their profile:
•	Description - a user can write any description about the picture, with no limit of words/chars
Other:
•	Date and time of publication - when a picture is created (only), the date and time of publication are automatically generated.
•	Likes - each picture has 0 likes at the beginning, and no one can change it. The number of likes a picture can collect is unlimited.

'''


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            validate_file_max_size,
        )
    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(
        null=True,
        blank=True
    )
    publication_date = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0
    )

    def __str__(self):
        result = [x.name for x in self.tagged_pets.all()]
        return ' | '.join(result)
