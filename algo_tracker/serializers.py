from rest_framework import serializers
from .models import Question, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'score')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('name', 'category', 'link', 'notes', 'video_solution', 'completed', 'time_complexity', 'space_complexity', 'time_to_solve', 'optimized', 'date')
        encoder = {
            "user": User(),
        }