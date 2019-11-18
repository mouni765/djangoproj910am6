from django.shortcuts import render
from .forms import  NameForm
from django.http import HttpResponse
from .models import Name
# Create your views here.
def get_name(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            n1=Name(First_name=form.cleaned_data["First_name"],Last_name=form.cleaned_data["Last_name"])
            n1.save()
            return HttpResponse('data inserted successfully')
    else:
        form=NameForm()
        return render(request,'name.html',{"form":form})
