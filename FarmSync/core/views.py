from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def landing_page(request):
    # Simulate dynamic data for placeholders
    system_features = [
        {'image_url': 'static/core/system1.jpg', 'title': 'Automate Stock Input', 'description': 'Easily track stock inputs.'},
        {'image_url': 'static/core/system2.jpg', 'title': 'Efficient Sales Logs', 'description': 'Manage sales effortlessly.'},
        {'image_url': 'static/core/system3.jpg', 'title': 'Inventory Monitoring', 'description': 'Stay updated with alerts.'},
    ]
    testimonials = [
        {'name': 'John Doe', 'message': 'This system transformed our cooperative!'},
        {'name': 'Jane Smith', 'message': 'Highly efficient and user-friendly.'},
        {'name': 'Alex Brown', 'message': 'The best tool for managing stock.'},
    ]
    faqs = [
        {'question': 'How accurate is the inventory monitoring?', 'answer': 'Our system provides precise inventory updates.'},
        {'question': 'Can I customize the system?', 'answer': 'Yes, the system is highly customizable to your needs.'},
    ]

    context = {
        'system_features': system_features,
        'testimonials': testimonials,
        'faqs': faqs,
    }
    return render(request, 'core/landing.html', context)
