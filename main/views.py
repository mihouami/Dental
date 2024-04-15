from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')
        print('Name: ', name, type(name))
        print('Email: ', email, type(email))
        print('Date: ', date, type(date))
        print('Time: ', time, type(time))
        print('Message: ', message, type(message))
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')

def test(request):
    return render(request, 'main/test.html')