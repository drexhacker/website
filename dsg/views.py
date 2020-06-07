from django.shortcuts import render
from shop.forms import ContactForm
from django.core.mail import send_mail
from accounts.models import Profile
from django.contrib.auth.models import User
def index(request):
    return render(request, 'shop/index.html',{})

def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "DSG {}".format(cd['subject'])
            message = "DSG Support request from \nNames:{} {}\nEmail: {}\n\n{}\n DSG Contact Form".format(cd['fname'], cd['lname'], cd['email'], cd['message'])
            send_mail(subject, message, 'noreply@deut818systems.com', ('contact@deut818systems.com',))
            sent = True
    else:
        form = ContactForm()
    return render(request, 'shop/contact.html', {'form':form, 'sent':sent})

def about(request):
    members = User.objects.filter(profile__member=True)
    return render(request, 'about.html', {'members':members})

def privacy(request):
    return render(request, 'shop/privacy.html', {})

def faq(request):
    return render(request, 'faq.html', {})
