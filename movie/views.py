from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

#web scrapping the popular imdb.com

def home(request):
    base_url = 'https://www.imdb.com/'
    url = "https://www.imdb.com/chart/moviemeter/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find('table',  {'class': 'chart full-width'})
    rows = table.find_all('tr')
    movies = []
    for row in rows:
        image = row.find('img')
        link = row.find('a')
        if image and link:
            new_link = base_url + link['href']
            movies.append((image['alt'], image['src'], new_link))
            #print(new_link)
            page = request.GET.get('page', 1)
            
            paginator = Paginator(movies, 12)
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                users = paginator.page(1)
            except EmptyPage:
                users = paginator.page(paginator.num_pages)

    
   
    return render(request, "index.html", {'users': users})

