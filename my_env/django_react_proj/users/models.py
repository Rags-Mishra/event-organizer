from django.db import models

# User model
class User(models.Model):
    name = models.CharField("Name", max_length=240, blank=True)
    email = models.EmailField()
    password = models.CharField("Password", max_length=240)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name

# Event model
class Events(models.Model):
    event_name = models.CharField("EventName", max_length=240)
    date = models.DateField("Registration Date", auto_now_add=False)
    time = models.TimeField(
        "Time",
    )
    location = models.CharField("Location", max_length=300)
    image = models.CharField("image", max_length=200)
    is_liked = models.BooleanField("is_liked", default=False)
