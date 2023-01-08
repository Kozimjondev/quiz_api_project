from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView

# Create your views here.

class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__id=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__id=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)
