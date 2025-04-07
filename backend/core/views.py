from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
import os
from .models import Habit, DailyLog, BuilderManifesto, SMSMessage, MessageTone
from .serializers import (
    HabitSerializer,
    DailyLogSerializer,
    BuilderManifestoSerializer,
    SMSMessageSerializer
)
from openai import OpenAI
import os

import dotenv
dotenv.load_dotenv()

# === ViewSets ===

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class DailyLogViewSet(viewsets.ModelViewSet):
    queryset = DailyLog.objects.all()
    serializer_class = DailyLogSerializer

class BuilderManifestoViewSet(viewsets.ModelViewSet):
    queryset = BuilderManifesto.objects.all()
    serializer_class = BuilderManifestoSerializer

class SMSMessageViewSet(viewsets.ModelViewSet):
    queryset = SMSMessage.objects.all()
    serializer_class = SMSMessageSerializer

# === GPT Message Generator ===

@api_view(['POST'])
def generate_gpt_message(request):
    time_of_day = request.data.get("time_of_day")  # morning, midday, night
    tone = request.data.get("tone")  # honest, hype, etc.

    if not time_of_day or not tone:
        return Response({"error": "Missing time_of_day or tone"}, status=400)

    prompt = f"Write a motivational, focused, and {tone} message for a {time_of_day} check-in. Make it 1-2 sentences. Speak to someone who is building a legendary future and needs to stay aligned with their purpose."

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        message_text = response.choices[0].message.content.strip()

        message = SMSMessage.objects.create(
            time_of_day=time_of_day,
            tone=tone,
            content=message_text,
            sent=False
        )

        return Response({"message": message_text})

    except Exception as e:
        return Response({"error": str(e)}, status=500)
    

@api_view(["POST"])
def verify_password(request):
    input_password = request.data.get("password")
    if input_password == os.getenv("DASHBOARD_PASSWORD"):
        return Response({"success": True})
    return Response({"success": False}, status=status.HTTP_401_UNAUTHORIZED)