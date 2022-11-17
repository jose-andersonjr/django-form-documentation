from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from core.forms import NameForm, ContactForm
from django.core.mail import send_mail


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['c_myself']
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()  

    context = {
        'form':form
    }  
    return render(request, 'home.html', context=context)