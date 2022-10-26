from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import m_link, r_link

# Create your views here.

def links_srt(request):
    
    ini_ = request.headers["link"]
    srt = m_link(ini_)
    return JsonResponse({"success": True, "link": srt})

def redirect_srt(request, link):
    l = r_link(link)
    if l:
        if l[0:8] == 'https://':
            return redirect(l)
        elif l[0:7] == 'http://':
            return redirect(l)
        else:
            return redirect(f'https://google.com/?q={l}')
    else:
        return HttpResponse('Sorry but the link is invalid. Generate a link >>> <a href="http://localhost:8000" style=color:"red";>Here</a>')

def home_srt(request):
    return render(request, "main/index.html")
