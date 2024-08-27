from django import forms
from .models import KRI, Portfolio, PerformanceMetric


class KRIForm(forms.ModelForm):
    class Meta:
        model = KRI
        fields = ['name', 'value', 'threshold', 'date_reported']


class PerformanceMetricForm(forms.ModelForm):
    class Meta:
        model = PerformanceMetric
        fields = ['name', 'metric_value', 'target_value', 'date_measured']


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'description', 'total_value', 'risk_level']
