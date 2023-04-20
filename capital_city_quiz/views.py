from django.shortcuts import render
from django.views import View
from django.contrib import messages
import requests
import random

class Home(View):

    def get(self,request):
        context = {}
        response = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
        data= response.json()
        countries = data.get('data', [])
        index = random.randint(0,len(countries)-1)
        if countries:
                context["country"] = countries[index].get('name', '')

        return render(request , 'home.html',context)

    def post(self,request):
        
        context = {}
        answer = request.POST['answer']
        country = request.POST['country']
        context["country"] = country
        response = requests.post('https://countriesnow.space/api/v0.1/countries/capital' , data={"country":country})
        data= response.json()
        country = data.get('data', [])
        capital = country['capital']

        if answer.lower() == capital.lower():
            messages.success(request , "Correct Answer")
            return render(request , 'home.html',context)
        else:
            messages.error(request , f"Wrong Answer! The correct answer is {capital}.")
            return render(request , 'home.html',context)
