from decimal import Decimal
from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

from django.utils import timezone


class AccessToken(models.Model):
    token = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return self.token
    
    from django.db import models
from django.utils import timezone

class Game(models.Model):
    GAME_TYPES = [
        ('normal', 'Normal Game'),
        ('grandJackpot', 'Grand Jackpot'),
        ('correct_score', 'Correct Score'),
         ('megaJackpot', 'Mega jakpot'),
         ('ft/cs','FT/CS'),
         ('over/under1.5','Over/Under 1.5'),
         ('ht/cs', 'HT/CS'),
         ('supermultibet', 'Super Multibet')
    ]
    
    # HOME = 'H'
    # AWAY = 'A'
    # DRAW = 'D'
    # WIN_CHOICES = [
    #     (HOME, 'Home'),
    #     (AWAY, 'Away'),
    #     (DRAW, 'Draw')
    # ]
    
    game_type = models.CharField(max_length=15, choices=GAME_TYPES)
    Teams = models.TextField(max_length=300, default='manU')
    time = models.TimeField()
    created = models.DateTimeField(default=timezone.now)
    # prediction = models.CharField(max_length=1, choices=WIN_CHOICES, null=True, blank=True)
    amount = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.game_type} - {self.Teams}"

        
    def is_expired(self):
        """Return True if the game is older than 24 hours, else False."""
        return timezone.now() - self.created > timezone.timedelta(hours=24)
    
    def delete_if_expired(self):
        """Delete the game if it is older than 24 hours."""
        if self.is_expired():
            self.delete()


class Earning(models.Model):
   amount = models.CharField(max_length=15)

class RunningTotal(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def add_amount(self, amount):
        
        self.total_amount += Decimal(str(amount))

        self.save()

    def __str__(self):
        return f"Running total: {self.total_amount}"

    def is_expired(self):
        """Return True if the game is older than 24 hours, else False."""
        return timezone.now() - self.created > timezone.timedelta(hours=24)
    
    def delete_if_expired(self):
        """Delete the game if it is older than 24 hours."""
        if self.is_expired():
            self.delete()
