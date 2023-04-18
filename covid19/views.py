from datetime import datetime
import requests
from django.shortcuts import render

def index_view(request, source='PL'):
    
    #Statistics
    url = ('https://api.covid19api.com/summary')
    response = requests.get(url)
    data = response.json()

    for record in data['Countries']:
        if record['CountryCode'] == source:
            completeCountry = record
    
    completeGlobal = data['Global']
    
    #chetny
    updatedTimeGlobal = datetime.strptime(completeGlobal["Date"], "%Y-%m-%dT%H:%M:%S.%fZ")
    updatedTimeCountry = datetime.strptime(completeCountry["Date"], "%Y-%m-%dT%H:%M:%S.%fZ")


    countries = {
    'PL': 'Poland', 
    'DE': 'Germany',
    'US': 'USA',
    'GB': 'Great Britain',
    'FR': 'France',
    'ES': 'Spain',
    'RU': 'Russia',
    }


    context = {
        'statistics': completeCountry,
        'statisticsGlobal': completeGlobal,
        'Countries': countries,
        'activeSource': source,        
        'updatedTimeGlobal': updatedTimeGlobal,
        'updatedTimeCountry': updatedTimeCountry,
    }
    return render(request, 'covid19/index.html', context)
