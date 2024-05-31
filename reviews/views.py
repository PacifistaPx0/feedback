from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        print(username)
        return HttpResponseRedirect("/thankyou")

    return render(request, "reviews/index.html")


def thankyou(request):
    return render(request, "reviews/thankyou.html")
