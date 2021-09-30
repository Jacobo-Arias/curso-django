"""Platzigram Views"""

# Django
from django.http import HttpResponse, JsonResponse

# utilities
from datetime import datetime


def hello_world(request):
    """Return a greeting"""
    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse(f"Hi, current time is {str(now)}")


def sorted_numbers(request):
    """Return a JSON"""
    numbers = [int(i) for i in request.GET["numbers"].split(",")]
    numbers.sort()
    data = {"status": "ok", "numbers": numbers, "message": "Integers sorted correctly"}
    return JsonResponse(data)


def hi(request, name, age):
    if age <= 12:
        message = f"Sorry {name}, you're not allowed here"
    else:
        message = f"Hello {name}, welcome to platzigram"

    return HttpResponse(message)
