from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
import random


def create_phone():
    all_phones = []
    users = Profile.objects.all()
    
    for user in users:
        all_phones.append(user.phone)
        
    new_phone = '+7'+ str(random.randint(700000000, 999999999))
    
    if new_phone not in all_phones:
        return new_phone 
    else:
        return create_phone()   
    
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance, 
            phone=create_phone(),
            balance = 0)
        Profile.user
        
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
        
    
    

