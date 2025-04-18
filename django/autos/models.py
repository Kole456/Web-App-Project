from django.db import models

# assignment stuffs
from django.core.validators import MinLengthValidator

# The Make model represents the car manufacturer.
class Make(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(2)],
        help_text="Enter the name of the car make (minimum 2 characters)"
    )

    def __str__(self):
        return self.name

# The Auto model represents a car and includes a foreign key to the Make model.
class Auto(models.Model):
    nickname = models.CharField(max_length=50, help_text="Enter a nickname for the auto")
    mileage = models.IntegerField(help_text="Enter the mileage for the auto")
    comments = models.CharField(
        max_length=300,
        blank=True,
        help_text="Optional comments about the auto"
    )
    # ForeignKey from Auto to Make ensures that each Auto is linked to a Make.
    make = models.ForeignKey(
        Make,
        on_delete=models.CASCADE,
        help_text="Select the make of the auto"
    )

    def __str__(self):
        return self.nickname
