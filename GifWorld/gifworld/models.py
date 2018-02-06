from django.db import models

class Gif(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    upload_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class CsgoGif(Gif):
    image = models.ImageField(max_length=255)
    WEAPONS = (
        ('PI', 'Pistol'),
        ('RI', 'Rifle'),
        ('SR', 'Sniper'),
        ('GR', 'Grenade'),
        ('OT', 'Other'),
    )
    weapon_used = models.CharField(
        max_length=2,
        choices=WEAPONS,
        default='PI',       
    )
    

class OWGif(Gif):
    image = models.ImageField(max_length=255)
    HEROES = (
        ('OF', 'Offense'),
        ('DE', 'Defense'),
        ('TA', 'Tank'),
        ('SU', 'Support'),
    )
    hero_class = models.CharField(
        max_length=2,
        choices=HEROES,
        default='OF',
    )
    
