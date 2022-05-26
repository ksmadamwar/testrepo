from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from biosensorapp.models import UserInformation,SensorData
import json
import pyrebase


def index(request):
    return render(request,"build/index.html")


def get_users_data(request):
    '''
        This function would return details of all users from the user info table
    '''
    data = list(UserInformation.objects.values())    
    return JsonResponse({'data':data})


def get_sensor_data(request):
    '''
        This function would return sensor data for a particular user
    '''    
    body_unicode = request.body.decode('utf-8')     
    body = json.loads(body_unicode)
    print(body) 
    data=[]
    user_id = body['uid']
    if user_id:
        data = list(SensorData.objects.filter(user_id = user_id).values())
        print(type(data))
        return JsonResponse({'sensor-data':data})



''' for firebase '''

config={
      'apiKey': "AIzaSyCegFLQg5tlXi6ixQCa6JE7vq0opJXYySo",
      'authDomain': "shoppingcartapp-8d98b.firebaseapp.com",
      'projectId': "shoppingcartapp-8d98b",
      'storageBucket': "shoppingcartapp-8d98b.appspot.com",
      'messagingSenderId': "970381875676",
      'appId': "1:970381875676:web:9b82491ba1929f22875719",
      'measurementId': "G-PGF48WDT3P"
}

# # Initialising database,auth and firebase for further use
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()