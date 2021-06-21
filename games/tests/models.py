from django.db import models
from django.contrib.auth.models import User

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Game(models.Model):
    game_des = models.TextField(max_length=1000, blank=True)
    game_name = models.CharField(max_length=200)
    dev_company = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    rel_date = models.DateField('Date Released')

    GENRE_CHOICES = (
        ('ts', 'Tactical Shooter'),
        ('rpg', 'RPG'),
        ('mb', 'MOBA'),
    )

    game_genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    game_platform = models.CharField(max_length=200)
    game_price = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='game_post', blank=True)

    def total_likes(self):
        return self.likes.count()


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    mobilephone = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)


class OnlineGameStore(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200)
    store_link = models.CharField(max_length=200)
