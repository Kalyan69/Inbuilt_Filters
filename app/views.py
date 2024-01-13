from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'Django is frame worl','dt':dt,'c':1}

    return render(request,'filters.html',d)