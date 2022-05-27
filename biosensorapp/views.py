from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from biosensorapp.models import UserInformation,SensorData
import json
import pyrebase
import firebase_admin
from firebase_admin import auth


def index(request):
    return render(request,"build/index.html")


def get_users_data(request):
    '''
        This function would return details of all users from the user info table
    '''
    data = list(UserInformation.objects.values()) 


    # user=authe.sign_in_with_email_and_password("test@test.com","***")
    # print(user)


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



def insert_data_from_mobile(request):
    '''
        This function would be used to store data from mobile app into 
        database.
        It will first validate the token recieved from api call
        with the firebase db details and if token is validated then only data will be 
        inserted into db.
        to validate from the firebase, below env varible needs to be set
        after genereating serice account file from firebase project
        $env:GOOGLE_APPLICATION_CREDENTIALS="service-account-file.json"
    '''

    #reading request param
    body_unicode = request.body.decode('utf-8')     
    body = json.loads(body_unicode)
    print("body from mobile app", body) 
    id_token = body['id_token']

    default_app = firebase_admin.initialize_app();
    decoded_token = auth.verify_id_token(id_token)
    print("decoded_token", decoded_token)
    uid = decoded_token['uid']



''' for firebase '''

config={
      'apiKey': "AIzaSyCegFLQg5tlXi6ixQCa6JE7vq0opJXYySo",
      'authDomain': "shoppingcartapp-8d98b.firebaseapp.com",
      'projectId': "shoppingcartapp-8d98b",
      'storageBucket': "shoppingcartapp-8d98b.appspot.com",
      'messagingSenderId': "970381875676",
      'appId': "1:970381875676:web:9b82491ba1929f22875719",
      'measurementId': "G-PGF48WDT3P",
      'databaseURL' : ""
}

# # Initialising database,auth and firebase for further use
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()



