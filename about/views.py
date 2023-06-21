from django.shortcuts import render, HttpResponse

# Create your views here.
def page(request):
    return HttpResponse("Найдите работу или работника мечты")
