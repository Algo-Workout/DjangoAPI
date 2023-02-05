from django.contrib import admin
from .models import User, Question

admin.site.register(Question)
admin.site.register(User)
