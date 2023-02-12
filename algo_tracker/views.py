from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import User, Question  
from .serializers import UserSerializer, QuestionSerializer

# Create your views here.
def questionApi(request, id=0):
    if request.method == 'GET':
        questions = Question.objects.all()
        questions_serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(questions_serializer.data, safe=False)
    elif request.method == 'POST':
        question_data=JSONParser.parser(request).question_serializer = QuestionSerializer(data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        question_data = JSONParser.parser(request)
        question = Question.objects.get(QuestionId=question_data['QuestionId'])
        question_serializer = QuestionSerializer(question, data=question_data)
        if question_serializer.is_valid():
            question_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        question = Question.objects.get(QuestionId=id)
        question.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

def userApi(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data=JSONParser.parser(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser.parser(request)
        user = User.objects.get(UserId=user_data['UserId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
    elif request.method == 'DELETE':
        user = User.objects.get(UserId=id)
        user.delete()
        return JsonResponse("Deleted Successfully!", safe=False)