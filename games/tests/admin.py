from django.contrib import admin
# from .models import Choice, Question
from .models import Game, Profile, OnlineGameStore

# admin.site.register(Question)
# admin.site.register(Choice)

admin.site.register(Game)
admin.site.register(Profile)
admin.site.register(OnlineGameStore)
