from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.urls import reverse




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
    return redirect(reverse('contact') + f'?name={name}')




def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')

def blog_single(request):
    return render(request, 'main/blog-single.html')

def blog(request):
    return render(request, 'main/blog.html')

def doctors(request):
    return render(request, 'main/doctors.html')

def services(request):
    return render(request, 'main/services.html')

def test(request):
    return render(request, 'main/test.html')