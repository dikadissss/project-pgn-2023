from django.shortcuts import render
from applications import sql

from datetime import datetime


# Create your views here.
def dashboard(request):
    dt = datetime.now()

    date = dt.day
    month = dt.month
    year = dt.year

    today = sql.list_event(start_time=f"{year}/{month}/{date}", end_time=f"{year}/{month}/{date + 1}")
    month = sql.list_event(start_time=f"{year}/{month}/01", end_time=f"{year}/{month + 1}/01")
    year = sql.list_event(start_time=f"{year}/01/01", end_time=f"{year + 1}/01/01")

    context = {
        'title': 'Dashboard',
        'today': today,
        'month': month,
        'year': year
    }
    return render(request, 'dashboard/dashboard.html', context)
