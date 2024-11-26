from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Geolocation
from .models import Cooperative
from .models import User
from .models import Stock_management
from .models import System
from .models import Notification
from .models import Fail_type
def Hello(request):
    return render(request, "landing.html")

def dashboard(request, id):
    system = get_list_or_404(System, cooperative_id=id)
    mngt = get_list_or_404(Stock_management, cooperative_id=2)
    cooperative = get_object_or_404(Cooperative, pk=id)
    dash_info = {
        "name": cooperative.user.full_name,
        "coop_info": cooperative,
        "system_info": system[:5],
        "management":  mngt[:5],
    }
    return render(request, 'dashboard.html', {"dashboard": dash_info})

def home(request):
    geolocation = Geolocation.objects.all()
    return render(request, 'home.html', {'locationCoop': geolocation})

def signup(request):
    return render(request, 'signup.html')

def overview(request, id):
    coop = get_object_or_404(Cooperative,pk=id)
    return render(request, 'overview.html', {'cooperative_info': coop})

def notification(request, id):
    coop = get_object_or_404(Cooperative, pk=id)
    mngt = get_list_or_404(Stock_management, cooperative_id=id)
    return render(request, 'notification.html')

def complete_account(request):
    return render(request, 'complete_account.html')

def stock_mngt(request, id):
    stock = get_list_or_404(Stock_management, cooperative_id=id)
    return render(request, 'stock_mngt.html', {'stocks': stock})

def login(request):
    return render(request, 'login.html')

def add_mngt(request):
    return render(request,"add_mngt.html")
