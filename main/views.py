from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.mail import send_mail



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



@require_POST
def get_quote(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message_customer = request.POST.get('message')
    subject = 'Get a Free Quote'
    from_email = 'flaskapptest@outlook.com'
    message  = f'''
            Hello Doctor,
            
            You received the following request from the following contact :

            Name: {name}
            Email: {email}
            Phone: {phone}
            Message: {message_customer}

            Regards
            '''
    send_mail(subject, message, from_email, ['flaskapptest@outlook.com'])
    return redirect('index')




def contact(request):
    return render(request, 'main/contact.html')

def test(request):
    return render(request, 'main/test.html')