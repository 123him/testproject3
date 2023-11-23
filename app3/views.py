from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app3.models import tbl_user


from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes
from rest_framework import *
from django.contrib.auth import authenticate

import json

# Create your views here.
def success_response(response, status_code=None):
        json_obj = {
        "hasError": False,
        "errorCode": -1,
        "message": "Success",
        }
        json_obj["response"] = response
        if status_code is None:
            return Response(json_obj, status=status.HTTP_200_OK)
        return Response(json_obj, status=status_code)

def failure_response(response, status_code=None, error_code=1001, message="Failure"):
    json_obj = {
        "hasError": True,
        "errorCode": error_code,
        "message": message,
    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status_code)

class createaccount(APIView):
     def post(self,request):
            datas={}
            response={}
            try:
                y=tbl_user()
                x=User()
                x.first_name = request.data['fname']
                x.last_name = request.data['lname']
                x.email = request.data['mail']
                x.username = request.data['username']
                password = request.data['pwd']
                x.set_password(password)

                y.name = request.data['fname']
                y.age = request.data['age']
                y.gender = request.data['gender']
                y.username = request.data['username']

                y.save()
                x.save() 
                datas={ "FIRST NAME": x.first_name,
                        "LAST NAME": x.last_name,
                        "EMAIL": x.email,
                        "USERNAME" :  x.username,
                        "PASSWORD" : x.password,
                        "AGE" : y.age,
                        "GENDER" : y.gender,
                        }
               
            except Exception as e:
                response["statusMessage"]='user does not exist'
                return failure_response(response)

            response['isSuccess'] = True
            response["statusMessage"]='successfully done'
            response["DATA"]=datas    
            return success_response(response)
     
class auth_login(APIView):
     def post(self,request):
          data={}
          response={}
          try:
               username=request.data['username']
               password=request.data['password']

               print("helo")
               d=authenticate( username=username,password=password)
               print(d,'test1')
               a=tbl_user.objects.get(username=d)
               if d is not None:
                    data={
                         "USERNAME" : d.username,
                         "FIRST NAME" : d.first_name,
                         "LAST NAME" : d.last_name,
                         "EMAIL" : d.email,
                         "PASSWORD" : d.password,
                         "AGE" : a.age,
                         "GENDER": a.gender,
                    }
               else:
                    response['messege']='user does not exist'
                    return failure_response(response)
          except Exception as e:
                    response["statusMessage"]='user does not exist'
                    return failure_response(response)

          response['isSuccess'] = True
          response["statusMessage"]='successfully done'
          response["DATA"]=data   
          return success_response(response)


