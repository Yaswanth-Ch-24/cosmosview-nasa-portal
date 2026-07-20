from django.shortcuts import render, redirect
from django.http import JsonResponse

# Simple session-based favorites (no DB needed for demo)
def favorites_list(request):
    favs = request.session.get('favorites', [])
    return render(request, 'favorites/favorites.html', {'favorites': favs})

def add_favorite(request):
    title = request.GET.get('title', 'Untitled')
    url   = request.GET.get('url', '')
    date  = request.GET.get('date', '')
    ftype = request.GET.get('type', 'apod')
    if url:
        favs = request.session.get('favorites', [])
        item = {'title': title, 'url': url, 'date': date, 'type': ftype}
        if item not in favs:
            favs.append(item)
            request.session['favorites'] = favs
    return redirect(request.META.get('HTTP_REFERER', '/'))

def remove_favorite(request, index):
    favs = request.session.get('favorites', [])
    if 0 <= index < len(favs):
        favs.pop(index)
        request.session['favorites'] = favs
    return redirect('/favorites/')
