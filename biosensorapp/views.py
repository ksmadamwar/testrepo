from django.http import HttpResponse,JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from biosensorapp.models import UserInformation,SensorData
import json
import pyrebase
import firebase_admin
from firebase_admin import auth
import os


def index(request):
    return render(request,"build/index.html")


def get_users_data(request):
    '''
        This function would return details of all users from the user info table
        this is a GET api request, so no inputs are needed
        output - list of users present in the db
    '''
    data = list(UserInformation.objects.values())
    return JsonResponse({'data':data})


def get_sensor_data(request):
    '''
        This function would return sensor data for a particular user
        input - userid
        output - sensor data json
    '''    
    body_unicode = request.body.decode('utf-8')     
    body = json.loads(body_unicode)
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
        It will accept id token and data as request params,
        it will validate if id token is valid using firebase admin
        and only then insert the data.

        input required - idtoken, data to be inserted
        output - insertion status, msg


        Prerequisites-
        Create serive key if does not exist already - https://firebase.google.com/docs/admin/setup#windows
        It will first validate the token recieved from api call
        with the firebase db details and if token is validated then only data will be 
        inserted into db.
        to validate from the firebase, below env varible needs to be set (for windows 
        save in PATH env variable https://www.computerhope.com/issues/ch000549.htm)
        after genereating serice account file from firebase project
        $env:GOOGLE_APPLICATION_CREDENTIALS="service-account-file.json"


    '''    
    # to be removed later
    #SensorData.objects.all().delete()



    #reading request param
    body_unicode = request.body.decode('utf-8')     
    body = json.loads(body_unicode)
    status = 'ERROR'
    msg = "Something went wrong"
    if body:
        #check if data is present in the request body
        if 'data' in body:
            #validate the id token with firebase 
            if 'id_token' in body:
                id_token = body['id_token']
                # initializing firebase admin app only if it does not exist already
                try:
                    default_app = firebase_admin.get_app()
                except Exception as e:
                    default_app = firebase_admin.initialize_app();

                decoded_token = auth.verify_id_token(id_token)
                uid = decoded_token['uid']
                insert_count = 0
                #checking of user id is valid
                if uid != "":        
                    data = body['data']
                    for row in data:
                        print(row)
                        try:                            
                            #inserting data into sensor table                    
                            row_val = SensorData(
                                user_id = row['user_id'],
                                biosensor_name = row['biosensor_name'],
                                cholinesterase_name = row['cholinesterase_name'],
                                test_time = row['test_time'],
                                activity = row['activity'],
                                inhibition = row['inhibition'],
                                baseline = row['baseline'],
                                comments = row['comments'],
                                created_by = row['created_by'],
                                updated_by = row['updated_by']
                                )
                            #row_val.save()
                            insert_count += 1
                            
                        except Exception as e:
                            status = 'ERROR'
                            msg  = e
                            print("Error while inserting data in db",e)
                else:
                    status = 'ERROR'
                    msg = 'Token not authorized'

    if insert_count == len(data):
        status = 'OK'
        msg = 'Insertion successful'

    return JsonResponse({"status": status,"msg":msg})


def get_last_test_details(request):
    '''
        This function would return the last test details 
        for selected test type of a particular user,
        these details could be used to indentify
        the data insertion part when there is
        no intenet connection for a while

        input required - user id , biosensortest name
        output - sensor data json
    '''
    data = {}

    # reading request parameters
    body_unicode = request.body.decode('utf-8')     
    body = json.loads(body_unicode)

    if body:
        if 'user_id' in body and 'biosensor_name' in body: 
            user_id = body['user_id']
            biosensor_name = body ['biosensor_name']
            data = list(SensorData.objects.filter(user_id= user_id).order_by('test_time').reverse().values())[0]
            status = 'OK'
            msg = 'Success'
        else:
            msg = "Either of the input missing i.e., biosensor_name, user_id"
            status = "ERROR"
    else:
        status = 'ERROR'
        msg = "Something went wrong"
    return JsonResponse({'data':data, 'status':status,'msg':msg})


def user_login(request):
    '''
        This function would be used to validate user login information
    '''
    data = {}
    # reading request parameters
    body_unicode = request.body.decode('utf-8')     
    body = json.loads(body_unicode)
    useremail = body['user_email']
    password = body['user_pass']  
    status = "ERROR"  
    msg = ""

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
    firebase=pyrebase.initialize_app(config)
    authe = firebase.auth()
    database=firebase.database()
    try:
        user = authe.sign_in_with_email_and_password(useremail,password)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        status = "OK"
        msg = "Login Success"
    except:
        status = "ERROR"
        message="Invalid Credentials!!Please ChecK your Data"

    return JsonResponse({'user_data':user, 'status':status,'msg':msg})


def user_logout(request):
    '''
        This function would log the user out 
        and clear the session variable
    '''
    request.session['uid']=""
    return JsonResponse({'data':{}})

def check_session(request):
    '''
        This function would check if the user's data is stored 
        in the session
    '''
    uid = request.session['uid']
    


''' for firebase '''

