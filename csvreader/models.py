from django.db import models
from django.utils import timezone
from decimal import Decimal
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Payment(models.Model):
#     user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        get_latest_by = 'created_at'
    #Add any other fields you want to track for each payment, such as transaction date/time, status, or description.


    def __str__(self):
        return self.phone_number

class Payment1(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('c2b', 'Customer to Business'),
        ('b2c', 'Business to Customer'),
        ('b2b', 'Business to Business'),
    ]

    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return self.phone_number

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
