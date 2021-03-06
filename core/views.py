
from django.shortcuts import render
from django.conf import settings
import requests
from github import Github, GithubException
from .forms import DictionaryForm, SynonymsForm, CityForm, RobohashForm
from .models import City
from django.http import HttpResponse

def robohash(request):
    user_text = {}
    form = RobohashForm(request.GET)
    if form.is_valid():
            user_text = form.hashit()
    else:
        form = RobohashForm()
    return render(request, 'core/robohash.html', { 'form': form, 'user_text': user_text})

def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'core/oxford.html', {'form': form, 'search_result': search_result})





def crime(request):

    url = 'http://NflArrest.com/api/v1/crime'
    r = requests.get(url).json()

    print(r)
    crime_data = {
    'DUI' : r[0]['Category'],
    'DUIARRESTS' : r[0]['arrest_count'],
    'HANDICAP' : r[69]['Category'],
    'HANDIARRESTS' : r[69]['arrest_count'],
    'CHILDSUPP' : r[34]['Category'],
    'CHILDSUPPARRESTS' : r[34]['arrest_count'],
    'DOMESTIC' : r[3]['Category'],
    'DOMESTICPARRESTS' : r[3]['arrest_count']

    }

    context = {'crime_data' : crime_data}
    print(crime_data)
    return render(request, 'core/crime.html', context)


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=098732b5261acdda6e9a574b9f4360b5'
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, "core/weather.html", context)


def trivia(request):

    url = 'https://opentdb.com/api.php?amount=1&type=boolean'
    r = requests.get(url).json()

    trivia_data = {
        'category' : r["results"][0]['category'],
        'question' : r["results"][0]['question'],
        'correct_answer' : r["results"][0]['correct_answer']
        }
    context = { 'trivia_data' : trivia_data}
    print(trivia_data)
    return render(request, 'core/trivia.html', context)

def chuck(request):

    reply= requests.get('https://api.chucknorris.io/jokes/random')
    request.session['cwords'] = reply.json()

    return render(request, 'core/chuck.html', {
        'value': reply.json()['value']
        })




def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    return render(request, 'core/github.html', {'user': user})

def github_client(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        client = Github()

        try:
            user = client.get_user(username)
            search_result['name'] = user.name
            search_result['login'] = user.login
            search_result['public_repos'] = user.public_repos
            search_result['avatar_url'] = user.avatar_url
            search_result['success'] = True
        except GithubException as ge:
            search_result['message'] = ge.data['message']
            search_result['success'] = False

        rate_limit = client.get_rate_limit()
        search_result['rate'] = {
            'limit': rate_limit.rate.limit,
            'remaining': rate_limit.rate.remaining,
        }
    return render(request, 'core/github.html', {'search_result': search_result})

def home(request):
    is_cached = ('geodata' in request.session)
    ip_address = '74.130.182.40'
    if not is_cached:
        ip_address = '74.130.182.40'
        print(ip_address)
        payload = {'access_key': 'd62c327120643214856d11c1d7533c18', }
        url = "http://api.ipstack.com/%s" % ip_address
        response = requests.get(url, params=payload)
        r = response.json()
        print(r)
        location_data = {
                'ip' : r['ip'],
                'city' : r['city'],
                'region_name' : r['region_name'],
                'longitude' : r['longitude'],
                'latitude' : r['latitude'],
                'api_key': settings.GOOGLE_MAPS_API_KEY,
                }
        print(location_data)
        context = { 'location_data' : location_data}
        return render(request, 'core/home.html', context)



def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'core/oxford.html', {'form': form, 'search_result': search_result})

def synonyms(request):
    search_result = {}
    if 'word' in request.GET:
        form = SynonymsForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = SynonymsForm()
    return render(request, 'core/synonyms.html', {'form': form, 'search_result': search_result})

def antonyms(request):
    search_result = {}
    if 'word' in request.GET:
        form = SynonymsForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = SynonymsForm()
    return render(request, 'core/synonyms.html', {'form': form, 'search_result': search_result})
