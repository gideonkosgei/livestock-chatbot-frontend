from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat(request):
    return render(request, 'chat.html')


