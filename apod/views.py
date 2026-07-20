import requests
from django.shortcuts import render
from django.conf import settings
from datetime import date, timedelta


def fetch_apod(date_str=None):
    params = {'api_key': settings.NASA_API_KEY}
    if date_str:
        params['date'] = date_str
    try:
        r = requests.get('https://api.nasa.gov/planetary/apod', params=params, timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


def home(request):
    selected_date = request.GET.get('date', str(date.today()))
    data = fetch_apod(selected_date)

    # Date range: last 7 days for quick nav
    dates = [(date.today() - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(7)]

    return render(request, 'apod/home.html', {
        'apod': data,
        'selected_date': selected_date,
        'dates': dates,
        'today': str(date.today()),
    })


def apod_date(request, date_str):
    data = fetch_apod(date_str)
    return render(request, 'apod/home.html', {
        'apod': data,
        'selected_date': date_str,
        'today': str(date.today()),
    })
