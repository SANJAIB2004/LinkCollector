from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Links
# Create your views here.
 
def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site','')
 
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Links.objects.create(address=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Links.objects.all()
 
 
    return render(request,'myapp/result.html',{'data':data})
 
def clear(request):
    Links.objects.all().delete()
    return render(request,'myapp/result.html')