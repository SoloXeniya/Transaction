from django.db import models
from django.contrib.auth.models import User
from .utils import validate_phone_number
from django.forms import ValidationError


class Profile(models.Model):
    #username first_name last_name email password
    image = models.ImageField(upload_to='profile_image/', blank=True, null=True, verbose_name='Фотография профиля', help_text="Картинка должна быть х на х")
    
    phone = models.CharField(max_length=20, verbose_name='Телефон',
            help_text="Укажите действующий номер телефона", unique = True, validators = [validate_phone_number])
    
    balance = models.PositiveBigIntegerField(default=0, verbose_name='Баланс', help_text="Баланс")
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text = "Связанный пользователь для данного профиля")
    
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата создания")
    
    def __str__(self):
        return f"профиль пользователя: {self.user.username}"
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['-created_at']
        
class Transaction(models.Model):
    sender_phone = models.CharField(max_length=20,  verbose_name="Номер телефона отправителя", validators=[validate_phone_number])
    recipient_phone = models.CharField(max_length=20, verbose_name="Номер телефона получателя", validators=[validate_phone_number])
    amount = models.PositiveBigIntegerField(verbose_name="Сумма перевода")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата создания")
    
    
    # до сохранения данных  проверятся корректность данных
    def save(self, *args, **kwargs):
        try:
            sender_profile = Profile.objects.get(phone=self.sender_phone)
        except Profile.DoesNotExist:
            return ValidationError("Профиль отправителя не найден")
        try:
            recipient_profile = Profile.objects.get(phone=self.recipient_phone)
        except Profile.DoesNotExist:
            return ValidationError("Профиль получателя не найден")
        
        if self.sender_phone == self.recipient_phone:
            return ValidationError("Нельзя переводить самому себе")
        
        if sender_profile.balance < self.amount:
            return ValidationError("Недостаточно средств на балансе")
        if self.amount < 100:
            return ValidationError("Минимальная сумма перевода - 100")
        
        sender_profile.balance -= self.amount
        recipient_profile.balance += self.amount
        
        sender_profile.save()
        recipient_profile.save()  
            
        return super().save(*args, **kwargs)
    
    def _str_(self):
        
        return f"перевод от {self.sender_phone} для {self.recipient_phone} равен сумме {self.amount}"
    
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
        ordering = ['-created_at']


class AddBalance(models.Model):
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", validators=[validate_phone_number])
    amount = models.PositiveBigIntegerField(verbose_name="Сумма")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Дата создания")
    
    def save(self, *args, **kwargs):
        try:
            profile = Profile.objects.get(phone=self.phone)
        except Profile.DoesNotExist:
            return ValidationError("Профиль не найден")
               
        if self.amount < 100:
            return ValidationError("Минимальная сумма добавления - 100")
        
        profile.balance += self.amount
        profile.save()
        
        return super().save(*args, **kwargs)
    
    def _str_(self):
        return f"Добавление суммы {self.amount} для {self.phone}"
    
    class Meta:
        verbose_name = 'Пополнение баланса'
        verbose_name_plural = 'Пополнения баланса'
        ordering = ['-created_at']
    
    
    
    
    
    
        
        