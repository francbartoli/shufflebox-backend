from django.contrib import admin
from .models import Profile, BrownBag, SecretSanta, Hangout

# Register your models here.
admin.site.register(Profile)
admin.site.register(BrownBag)
admin.site.register(Hangout)
admin.site.register(SecretSanta)
