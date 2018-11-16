from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Sujet']
            from_email = form.cleaned_data['Votre_email']
            message = form.cleaned_data['Votre_message']
            try:
                send_mail(subject, message, from_email, ['fatimazahrakechida@gmail.com'])
            except BadHeaderError:
                messages.error(request, 'Une erreur s\'est produite veuillez réessayer ultérieurement!')
            messages.success(request, 'Votre email a été envoyé avec succès!')
    return render(request, "contact.html", {'form': form})

def contact_success_view(request):
    return HttpResponse('Success! Thank you for your message.')