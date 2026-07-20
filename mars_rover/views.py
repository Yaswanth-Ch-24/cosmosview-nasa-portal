import requests
from django.shortcuts import render
from django.conf import settings

ROVERS = ['curiosity', 'opportunity', 'spirit']
CAMERAS = {
    'curiosity': ['FHAZ','RHAZ','MAST','CHEMCAM','MAHLI','MARDI','NAVCAM'],
    'opportunity': ['FHAZ','RHAZ','NAVCAM','PANCAM','MINITES'],
    'spirit': ['FHAZ','RHAZ','NAVCAM','PANCAM','MINITES'],
}

def mars_home(request):
    rover    = request.GET.get('rover', 'curiosity')
    earth_date = request.GET.get('date', '2023-06-01')
    camera   = request.GET.get('camera', '')
    page     = request.GET.get('page', 1)

    params = {
        'api_key': settings.NASA_API_KEY,
        'earth_date': earth_date,
        'page': page,
    }
    if camera:
        params['camera'] = camera

    photos = []
    error  = None
    try:
        url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos'
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            photos = r.json().get('photos', [])
        else:
            error = f"API error {r.status_code}"
    except Exception as e:
        error = str(e)

    return render(request, 'mars_rover/mars.html', {
        'photos': photos,
        'rover': rover,
        'rovers': ROVERS,
        'cameras': CAMERAS.get(rover, []),
        'selected_camera': camera,
        'selected_date': earth_date,
        'page': int(page),
        'error': error,
    })
