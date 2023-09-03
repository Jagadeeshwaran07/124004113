from rest_framework.response import Response
from .models import Company, Train

from django.http import JsonResponse
import requests

def register_company(request):
    registration_data = {
        "companyName": "Jack Trains",
        "rollNumber": "124004113",
        "ownerEmail": "124004113@sastra.ac.in",
        "accessCode": "FKDLIg"
    }

    registration_url = "http://20.244.56.144/train/register"

    response = requests.post(registration_url, json=registration_data)

    if response.status_code == 200:
        registration_response = response.json()
        client_id = registration_response["clientID"]
        client_secret = registration_response["clientSecret"]
        return JsonResponse({
            "message": "Company registered successfully!",
            "clientID": client_id,
            "clientSecret": client_secret
        })
    else:
        return JsonResponse({
            "error": f"Company registration failed with status code: {response.status_code}"
        }, status=400)
    
    

def obtain_auth_token(request):
    auth_data = {
        "ownerEmail": "rahulgabc.edu",
        "rollio": "1",
        "clientSecret": "XOyolORPasKMOAAN"
    }

    auth_url = "http://20.244.56.144/train/auth"

    response = requests.post(auth_url, json=auth_data)

    if response.status_code == 200:
        auth_response = response.json()
        token_type = auth_response["token_type"]
        access_token = auth_response["access_token"]
        expires_in = auth_response["expires_in"]
        return JsonResponse({
            "message": "Authorization successful!",
            "tokenType": token_type,
            "accessToken": access_token,
            "expiresIn": expires_in
        })
    else:
        return JsonResponse({
            "error": f"Authorization failed with status code: {response.status_code}"
        }, status=400)

def get_all_trains(request):
    headers = {
        "Authorization": "FKDLIg"
    }

    train_details_url = "http://20.244.56.144/train/trains"

    response = requests.get(train_details_url, headers=headers)

    if response.status_code == 200:
        train_details = response.json()

        return JsonResponse({
            "message": "Train details retrieved successfully",
            "trainDetails": train_details
        })
    else:
        return JsonResponse({
            "error": f"Failed to retrieve train details with status code: {response.status_code}"
        }, status=400)
    
