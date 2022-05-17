import json

from django.shortcuts import render
from django.views import View


# Create your views here.
class KnowledgeBase(View):

    @staticmethod
    def get(request):
        context = {}

        return render(request, "knowledge_base/info.html", context)


class Strategies(View):

    @staticmethod
    def get(request):
        return render(request, "knowledge_base/strategies.html")


class About(View):

    @staticmethod
    def get(request):
        return render(request, "knowledge_base/about.html")


class Contacts(View):

    @staticmethod
    def get(request):
        return render(request, "knowledge_base/contacts.html")