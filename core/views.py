from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from .models import Profile,Testimonial
from django.conf import settings
import os



def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            
            send_mail(
                subject=f"New Contact: {contact_message.subject}",
                message=f"Message from {contact_message.name} <{contact_message.email}>:\n\n{contact_message.message}",
                from_email=None,
                recipient_list=['admin@example.com'],
                fail_silently=True,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('core:contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})

def resume(request):
    profile = Profile.objects.first()
    return render(request, 'core/resume.html', {'profile': profile})

def resume_pdf(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    html_string = render_to_string('core/resume.html', context)

    css_path = os.path.join(settings.BASE_DIR, 'static/resume/style.css')

    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    result = html.write_pdf(stylesheets=[css_path])

    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    return response


def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'core/testimonials.html', {'testimonials': testimonials})


def home(request):
    profile = Profile.objects.first()
    testimonials = Testimonial.objects.all()[:3] 
    return render(request, 'core/home.html', {
        'profile': profile,
        'testimonials': testimonials,
    })