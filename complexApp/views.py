from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import PassengerForm
from .models import PassengerBaseModel
# Create your views here.
def home(request):
    return render(request, 'home.html')

def passengerRegister(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('passengerList')
        else:
            form = PassengerForm()
    else:
        form = PassengerForm()
    return render(request, 'register_pasenger.html', {'form':form})

def update(request, id):
    passenger = PassengerBaseModel.objects.get(pk=id)
    form = PassengerForm(instance=passenger)
    if request.method == 'POST':
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('passengerList')
        else:
            form = PassengerForm()

    context = {
        'form':form
    }
    return render(request, 'register_pasenger.html', context)

def delete(request, id):
    queryset = PassengerBaseModel.objects.get(pk=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('passengerList')
    context  = {
        'queryset':queryset
    }
    return render(request, 'register_pasenger.html', context)

def passengerList(request):
    form = PassengerBaseModel.objects.all()
    return render(request, 'passenger_list.html', {'form':form})
