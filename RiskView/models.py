from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=100)  # Name of the portfolio
    description = models.TextField(blank=True)  # Optional description
    total_value = models.FloatField()
    risk_level = models.CharField(max_length=50, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ])  # Risk level of the portfolio
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when created

    def __str__(self):
        return self.name


class KRI(models.Model):
    name = models.CharField(max_length=100)
    value = models.FloatField()
    threshold = models.FloatField()
    date_reported = models.DateField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PerformanceMetric(models.Model):
    name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    target_value = models.FloatField()
    date_measured = models.DateField()

    def __str__(self):
        return self.name
