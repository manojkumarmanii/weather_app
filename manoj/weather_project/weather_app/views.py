from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'User already exists!'})
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('login')
    return render(request, 'signup.html')

from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

import requests
from .models import CitySearch

def weather_view(request):
    weather_data = None
    if request.method == 'POST':
        city_name = request.POST['city']
        # Save the search
        if request.user.is_authenticated:
            CitySearch.objects.create(user=request.user, city_name=city_name)
        # Fetch weather data from OpenWeatherMap
        api_key = '99e773801015935bef195cc4e2020ac1'  # Replace with your API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={'99e773801015935bef195cc4e2020ac1'}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'condition': data['weather'][0]['description']
            }
    return render(request, 'weather.html', {'weather_data': weather_data})



def signup(request):
    print("Trying to render: weather_app/login.html")
    return render(request, 'weather_app/login.html')

def signup_view(request):
    print("Trying to render: weather_app/signup.html")
    return render(request, 'weather_app/signup.html')


 


