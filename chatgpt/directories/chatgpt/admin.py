from django.contrib import admin
from .models import *
from .models import Feedback

# Register your models here.


admin.site.register(QuestionAnswer)
admin.site.register(Rate)
admin.site.register(Feedback)
