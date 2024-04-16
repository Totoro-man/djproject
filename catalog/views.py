from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        return right_way(request)
    return render(request, 'catalog/contacts.html')


def right_way(request):
    data = {}
    if request.method == 'POST':
        data.update({'name': request.POST.get('name')})
        data.update({'email': request.POST.get('email')})
    return render(request, 'catalog/your_way.html', data)
