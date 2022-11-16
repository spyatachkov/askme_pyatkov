from django.contrib import admin
from app.models import Tag
from app.models import Profile
from app.models import Question
from app.models import Answer

# Register your models here.
admin.site.register(Tag)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)

