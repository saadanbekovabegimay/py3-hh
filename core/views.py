from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("hi")
def address(request):
    return HttpResponse('''
    <ul>
        <li>г.Бишкек, 7 м-н, 26/1</li>
        <li>г.Ош, Черемушкина 156</li>
    </ul>    
''')