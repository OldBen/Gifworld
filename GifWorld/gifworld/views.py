from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.http import HttpResponse

from .models import CsgoGif, OWGif
from .forms import *


def index(request):
    return render(request, 'gifworld/index.html')
    
def csgo(request):
    title = request.GET.get('title', request.POST.get('title', ''))
    weapon = request.GET.get('weapon', request.POST.get('weapon', ''))
    page_no = int(request.GET.get('page', 1))
    paginator = Paginator(CsgoGif.objects.filter(title__contains=title).filter(weapon_used__contains=weapon).order_by('-upload_date'), 6)
    gifs = paginator.get_page(page_no)
    context = {
        "game": "csgo",
        "gifs": gifs,
        "page_no": page_no,
    }
    return render(request, 'gifworld/list.html', context)

def ow(request):
    title = request.GET.get('title', request.POST.get('title', ''))
    hero = request.GET.get('hero', request.POST.get('hero', ''))
    page_no = int(request.GET.get('page', 1))
    paginator = Paginator(OWGif.objects.filter(title__contains=title).filter(hero_class__contains=hero).order_by('-upload_date'), 6)
    gifs = paginator.get_page(page_no)
    context = {
        "game": "ow",
        "gifs": gifs,
        "page_no": page_no,
    }
    return render(request, 'gifworld/list.html', context)
    
def csgo_detail(request, id):
    gif = get_object_or_404(CsgoGif, pk=id)
    context = {
        "game": "csgo",
        "gif" : gif,
        
    }
    return render(request, 'gifworld/details.html', context)

def ow_detail(request, id):
    gif = get_object_or_404(OWGif, pk=id)
    context = {
        "game": "ow",
        "gif" : gif,
    }
    return render(request, 'gifworld/details.html', context)
    
def csgo_create(request):
    if request.method == 'POST':
        form = CsgoGifForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('csgo')
    else:
        form = CsgoGifForm()
    return render(request, 'gifworld/create.html', {
        'form': form,
        "game": "csgo",
        "game_name": "Counter-Strike",

    })

def ow_create(request):
    if request.method == 'POST':
        form = OWGifForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ow')
    else:
        form = OWGifForm()
    return render(request, 'gifworld/create.html', {
        'form': form,
        "game": "ow",
        "game_name": "Overwatch",
    })

def csgo_filter(request):
    if request.method == 'POST':
        return redirect('csgo', request)
    else:
        return render(request, 'gifworld/filter.html', {
            'form': CsgoGifFilter(),
            "game": "csgo",
            "game_name": "Counter-Strike",
    })

def ow_filter(request):
    if request.method == 'POST':        
        return redirect('ow', request)
    else:
        return render(request, 'gifworld/filter.html', {
            'form': OWGifFilter(),
            "game": "ow",
            "game_name": "Overwatch",
    })