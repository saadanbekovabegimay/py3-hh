from django.shortcuts import render, HttpResponse

# Create your views here.
def newpage(request):
    response = "Phone: +996777123456<br>Email: office@handhunter.kg"
    return HttpResponse(response)
