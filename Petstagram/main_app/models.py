import datetime

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
        default='Do not show',
        null=True,
        blank=True
    )
    def __str__(self):
        return self.first_name


class Pet(models.Model):
    TYPES = [(x, x) for x in ("Cat", "Dog", "Bunny", "Parrot", "Fish", "Other")]
    name = models.CharField('Pet name', max_length=30)
    type = models.CharField(
        max_length=max(len(x) for (x, y) in TYPES),
        choices=TYPES
    )
    date_of_birth = models.DateField(
        'Day of birth',
        null=True,
        blank=True
    )
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return self.name


class PetPhoto(models.Model):
    photo = models.ImageField(
        'Pet image',
        upload_to='images/',

    )
    tagged_pets = models.ManyToManyField(Pet)
    description = models.TextField(
        null=True,
        blank=True,
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
