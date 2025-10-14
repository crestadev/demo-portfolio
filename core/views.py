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
    profile = Profile.objects.first()
    return render(request, 'core/about.html', {'profile': profile})


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse

def contact(request):
    form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            contact_message = form.save()
            
            try:
                send_mail(
                    subject=f"New Contact: {contact_message.subject}",
                    message=f"Message from {contact_message.name} <{contact_message.email}>:\n\n{contact_message.message}",
                    from_email=None,  # Uses DEFAULT_FROM_EMAIL from settings
                    recipient_list=['admin@example.com'],
                    fail_silently=False,  # Do not fail silently
                )
                messages.success(request, 'Your message has been sent successfully!')
            except BadHeaderError:
                messages.error(request, 'Invalid header found. Message not sent.')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
            
            return redirect('core:contact')

    return render(request, 'core/contact.html', {'form': form})


def resume(request):
    profile = Profile.objects.first()
    return render(request, 'core/resume.html', {'profile': profile})

def resume_pdf(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    html_string = render_to_string('core/resume_pdf.html', context)
    css_path = os.path.join(settings.BASE_DIR, 'static/resume/pdf_style.css')

    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf(stylesheets=[css_path])

    response = HttpResponse(pdf, content_type='application/pdf')
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