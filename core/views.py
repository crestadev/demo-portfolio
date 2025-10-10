from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse
from weasyprint import HTML
import tempfile
from django.template.loader import render_to_string


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
    return render(request, 'core/resume.html')

def resume_pdf(request):
    """Generate PDF version of the resume page."""
    html_string = render_to_string('core/resume.html')
    html = HTML(string=html_string)
    result = html.write_pdf()
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="resume.pdf"'
    return response