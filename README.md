# Personal Portfolio Website ( D E M O )

A modern, responsive personal portfolio website built with Django. The website showcases projects, blogs, skills, experience, education, and allows visitors to contact you through a built-in form.

## Features

- **Home Page**
  - Hero section with profile photo, name, tagline, and social links
  - Skills section with animated progress bars
  - Featured projects with hover effects
  - Testimonials with interactive cards
  - Smooth animations and floating shapes

- **Blog**
  - List of blog posts with summaries
  - Detailed blog pages with markdown content support
  - Read more links for full posts

- **About Page**
  - Profile overview
  - Skills, experience, and education sections
  - Modals for detailed experience and education information

- **Projects**
  - List of projects with images and summaries
  - Detailed project pages

- **Contact**
  - Contact form with email backend
  - Option to configure demo or real email sending

- **Performance & Optimization**
  - WhiteNoise for static file handling and caching
  - Compressed and versioned static files
  - Responsive design across all devices
  - AOS animations and interactive elements

## Technology Stack

- **Backend:** Django 5.x  
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript  
- **Database:** SQLite (default, can switch to PostgreSQL)  
- **Other Libraries:** WhiteNoise, AOS, Particles.js  

## Project Structure

portfolio/
   - ├── core/           # Main app for homepage, contact, profile
   - ├── blog/           # Blog app
   - ├── projects/       # Projects app
   - ├── templates/      # Base and shared templates
   - ├── static/         # Static CSS, JS, images
   - ├── media/          # Uploaded media files
   - ├── portfolio_site/ # Django project settings
   - └── manage.py
   - └── requirements.txt


