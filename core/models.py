from django.contrib.auth.models import User
from django.db import models
from datetime import date

# Create your models here.

# Create your models here.

EVENT_CATEGORY = (
   ("CRICKET", 'Cricket'),
   ("FOOTBALL", 'Football'),
   ("FOOSBALL", 'Foosball'),
   ("CARROM", 'Carrom'),
)

class Player (models.Model):
   image_link = models.CharField(max_length=1000, default = "")
   name = models.CharField(max_length=30)
   rating = models.IntegerField(default = 0)

   def __unicode__(self):
      return self.name

class Event(models.Model):
   name = models.CharField(max_length=40)
   event_date = models.DateTimeField()
   organizer = models.ForeignKey(User)
   start_date = models.DateTimeField()
   end_date = models.DateTimeField()
   description = models.CharField(max_length=100)
   max_bet = models.IntegerField(default = 0)
   min_bet = models.IntegerField(default = 0)
   limit = models.IntegerField(default = 0)
   category = models.CharField(max_length=20, choices=EVENT_CATEGORY, blank=True, null=True)
   winner = models.ForeignKey(Player)
   total_bet_amount = models.IntegerField(default=0)
   def __unicode__(self):
      return self.name

class Player_event (models.Model):
   event = models.ForeignKey(Event)
   player = models.ForeignKey(Player)
   rate_of_return = models.DecimalField(max_digits=5,decimal_places=2)

   def __unicode__(self):
      return self.player.name + self.event.name


class Bet(models.Model):
   event = models.ForeignKey(Event)
   player = models.OneToOneField(Player)
   amount = models.IntegerField(default = 0)
   rate_of_return = models.DecimalField(max_digits=10, decimal_places=2)
   user = models.OneToOneField(User)
   final_amount = models.IntegerField(default = 0)

   def __unicode__(self):
      return str(self.user) + str(self.player)

class User_profile(models.Model):
   user = models.OneToOneField(User)
   points = models.IntegerField(default = 0)

   def __unicode__(self):
      return self.user.username

class Player_rating(models.Model):
	player = models.ForeignKey(Player)
	rating = models.DecimalField(max_digits=10, decimal_places = 2, default = 0.0)
	category = models.CharField(max_length = 30, default = "")