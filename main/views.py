from django.shortcuts import render, redirect
from .models import Menu
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    return render(request, 'book.html', {'form': form})

def menu(request):
    menu_data = Menu.objects.all()
    context = {'menu': menu_data}
    return render(request, 'menu.html', context)

def display_menu_items(request, pk):
    if pk:
        menu_item = Menu.objects.get(id=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {'menu_item': menu_item})
