from rest_framework import serializers
from .models import Habit, DailyLog, BuilderManifesto, SMSMessage

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

class BuilderManifestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuilderManifesto
        fields = '__all__'

class SMSMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSMessage
        fields = '__all__'
