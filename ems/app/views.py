from django.core.mail import send_mail
from django.shortcuts import render
from django.views import View
from .models import ContactMessage, SlideModel, Review, Gallery


# Create your views here.
class Home(View):
    def get(self, request):
        slides = SlideModel.objects.all()
        reviews = Review.objects.all()
        Galleries = Gallery.objects.all()
        return render(request, 'base.html', {'slides': slides, 'reviews': reviews, 'Galleries': Galleries})

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_message = ContactMessage(name=name, email=email, number=number, subject=subject,
                                         message=message)
        contact_message.save()
        print(name)
        print(email)
        print(number)
        print(subject)
        print(message)
        subject = 'New Contact Form Submission'
        message = f'Name: {name}\nEmail: {email}\nNumber: {number}\nSubject: {subject}\nMessage: {message}'
        from_email = 'reset9546@gmail.com'
        recipient_list = ['lokeshjain2806@gmail.com']
        send_mail(subject, message, from_email, recipient_list)
        return render(request, 'base.html')
