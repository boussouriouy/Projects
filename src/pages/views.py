from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def about_view(request, *args, **kwargs):
    my_player = {
        'my_txt': 'Insha Allah you will be fine',
        'my_num': 'My number is: 123, 345,3452',
        'my_list': [123, 456, 678, 'MBD'],
        'my_html': '<h1>Bishmillah</h1>'
    }
    return render(request, 'about.html', my_player)

def contact_view(request, *args, **kwargs):
    return render(request, 'cont.html', {})

def info_view(request, *args, **kwargs):
    return render(request, 'info.html', {})