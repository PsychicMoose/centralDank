from django.db import models


class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

class DailyLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

class BuilderManifesto(models.Model):
    content = models.TextField()

class MessageTone(models.TextChoices):
    HONEST = 'honest', 'Honest'
    HYPE = 'hype', 'Hype'
    PHILOSOPHER = 'philosopher', 'Philosopher'
    MYTHIC = 'mythic', 'Mythic'

class SMSMessage(models.Model):
    time_of_day = models.CharField(max_length=10)  # 'morning', 'midday', 'night'
    tone = models.CharField(max_length=20, choices=MessageTone.choices)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
