from django.shortcuts import render


def index(request):
    return render(request, "capstone/index.html")

def todolist(request):
    return render(request, "capstone/todolist.html")