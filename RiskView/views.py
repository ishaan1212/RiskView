from django.shortcuts import render, redirect

from .forms import KRIForm, PerformanceMetricForm, PortfolioForm
from .models import KRI, PerformanceMetric, Portfolio

def index(request):
    return render(request, template_name='RiskView/base.html')
def dashboard(request):
    kris = KRI.objects.all()  # Fetch all KRIs
    metrics = PerformanceMetric.objects.all()  # Fetch all Performance Metrics
    portfolios = Portfolio.objects.all()  # Fetch all Portfolios
    return render(request, 'RiskView/dashboard.html', {
        'kris': kris,
        'metrics': metrics,
        'portfolios': portfolios,
    })


def add_kri(request):
    if request.method == 'POST':
        form = KRIForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RiskView:dashboard')  # Redirect to the dashboard or main page after saving
    else:
        form = KRIForm()  # Create an empty form for GET request

    # Render the form in both cases, either after a GET request or after an invalid POST request
    return render(request, 'RiskView/add_kri.html', {'form': form})


def add_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RiskView:dashboard')  # Redirect to the dashboard after saving
    else:
        form = PortfolioForm()  # Create an empty form for GET request

    # Render the form for both GET requests and failed POST requests
    return render(request, 'RiskView/add_portfolio.html', {'form': form})


def add_metric(request):
    if request.method == 'POST':
        form = PerformanceMetricForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RiskView:dashboard')  # Redirect to the dashboard after saving
    else:
        form = PerformanceMetricForm()  # Create an empty form for GET request

    # Render the form for both GET requests and failed POST requests
    return render(request, 'RiskView/add_metric.html', {'form': form})
