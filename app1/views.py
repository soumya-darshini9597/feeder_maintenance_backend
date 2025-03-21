from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Feeder
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404



@api_view(['POST','PATCH'])
@csrf_exempt
def create_feeder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(data)
            stepCount = data.get('stepCount')
            print(stepCount)
            feeder = Feeder.objects.create(stepCount=stepCount)
            print(feeder)

            # datas ={'stepCount': feeder.stepCount,
            #     "id":feeder.id}
            

            return JsonResponse({
                # 'mesuredHeight': feeder.mesuredHeight,
                'stepCount': feeder.stepCount,
                "id":feeder.id
            }, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
    elif request.method == 'PATCH':
        data = json.loads(request.body)
        id = data.get("id")
        feeder = get_object_or_404(Feeder,id=id)
        try:
            if 'mesuredHeight' in data:
                feeder.mesuredHeight = data['mesuredHeight'] 

                feeder.save()

            return JsonResponse({
                # 'mesuredHeight': feeder.mesuredHeight,
                'stepCount': feeder.stepCount,
                "id":feeder.id
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    else:
        return JsonResponse({'error': 'POST method only'}, status=405)

    

# @csrf_exempt
# def get_feeders(request,id=None):
#     if request.method == 'GET':
#         feeders = Feeder.objects.all()
#         data=[]
#         for i in feeders:
#             datas = {
#                 "id":i.id,
#                 "mesuredHeight":i.mesuredHeight,
#                 "stepCount":i.stepCount
#             }

#             data.append(datas)
            
#         return JsonResponse(data, safe=False)
#     else:
#         return JsonResponse({'error': 'GET method only'}, status=405) 
    

@csrf_exempt
def get_feeders(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                feeder = Feeder.objects.get(id=id)
                data = {
                    "id": feeder.id,
                    "mesuredHeight": feeder.mesuredHeight,
                    "stepCount": feeder.stepCount
                }
                return JsonResponse(data)
            except Feeder.DoesNotExist:
                return JsonResponse({'error': 'Feeder not found'}, status=404)
        else:
            feeders = Feeder.objects.all()
            data = []
            for feeder in feeders:
                data.append({
                    "id": feeder.id,
                    "mesuredHeight": feeder.mesuredHeight,
                    "stepCount": feeder.stepCount
                })
            return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'GET method only'}, status=405)


    
@csrf_exempt
def create_feeder_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            mesured_height_value = data.get('targetHeight')
            print(mesured_height_value)

            if not mesured_height_value:
                return JsonResponse({'error': 'targetheight is required'}, status=400)

            # Check if mesuredHeight exists in the database
            datas = Feeder.objects.filter(mesuredHeight=mesured_height_value).first()
            print(datas,"999999999999999")

            if datas:
                # # Optional: update stepCount to 5000 or keep as is
                # data.stepCount = 5000
                # data.save()
                print("8888888888")
                return JsonResponse({"message":"targetheight present in database"
                    # 'feeder_id': data.id,
                    # 'targetHeight': data.mesuredHeight,
                    # 'stepCount': data.stepCount
                }, status=200)
            
            return JsonResponse({'message': 'targetheight not found in database'},status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def get_targetHeight(request, id=None):
    if request.method == 'GET':
        feeders = Feeder.objects.all()
        data = []
        for feeder in feeders:
            data.append({
                "mesuredHeight": feeder.mesuredHeight,
                "stepCount": feeder.stepCount
            })
        return JsonResponse(data, safe=False, status=200)
    else:
        return JsonResponse({'error': 'GET method only'}, status=405)