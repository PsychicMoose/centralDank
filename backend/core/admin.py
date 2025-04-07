from django.contrib import admin
from .models import Habit, DailyLog, BuilderManifesto, SMSMessage

admin.site.register(Habit)
admin.site.register(DailyLog)
admin.site.register(BuilderManifesto)
admin.site.register(SMSMessage)
