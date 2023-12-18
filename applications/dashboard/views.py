from django.shortcuts import render
from applications import sql
from django.http import JsonResponse
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

    query_set = sql.group_event(start_time="2020-01-01 00:00:00", end_time="2024-01-01 00:00:00")

    context = {
        'title': 'Dashboard',
        'today': today,
        'month': month,
        'year': year,
        'query_set': query_set
    }
    return render(request, 'dashboard/dashboard.html', context)


# def chart(request):
#     query_set = sql.group_event(start_time="2020-01-01 00:00:00", end_time="2024-01-01 00:00:00")
#
#     data = []
#     labels = []
#     for qs in query_set:
#         data.append(qs['count'])
#         labels.append(qs['year'])
#
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data
#     })
