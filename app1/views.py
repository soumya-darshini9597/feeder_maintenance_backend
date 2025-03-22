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
        print(id)
        feeder = get_object_or_404(Feeder,id=id)
        print(feeder)
        try:
            if 'mesuredHeight' in data:
                feeder.mesuredHeight = data['mesuredHeight']
                feeder.save()
            if 'confirmationHeight' in data:
                feeder.confirmationHeight = data['confirmationHeight']
                feeder.save()

            return JsonResponse({
                # 'mesuredHeight': feeder.mesuredHeight,
                'stepCount': feeder.stepCount,
                "id":feeder.id,
                "confirmationHeight": feeder.confirmationHeight
            }, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    else:
        return JsonResponse({'error': 'POST method only'}, status=405)


    

@csrf_exempt
def get_feeders(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                feeder = Feeder.objects.get(id=id)
                data = {
                    "id": feeder.id,
                    "confirmationHeight": feeder.confirmationHeight,
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
                    "confirmationHeight": feeder.confirmationHeight,
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
            print("Received targetHeight:", mesured_height_value)

            if not mesured_height_value:
                return JsonResponse({'error': 'targetHeight is required'}, status=400)

            # Check if mesuredHeight exists in the database
            feeder = Feeder.objects.filter(mesuredHeight=mesured_height_value).first()
            print("Feeder found:", feeder)
            data =[]
            if feeder:
                # Update stepCount to 5000
                feeder.stepCount = 5000
                feeder.save()
                abcd = ({
                    "feeder_id": feeder.id,
                    "targetHeight": int(feeder.mesuredHeight),
                    "confirmationHeight":feeder.confirmationHeight,
                    "stepCount": feeder.stepCount
                })
                print("Updated feeder stepCount to 5000")
          
                data.append(abcd)
                return JsonResponse({
                    'message': 'targetHeight present in database',
                    'data': data
                }, status=200)
            
            return JsonResponse({'message': 'targetHeight not found in database'}, status=404)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


# @csrf_exempt
# def get_targetHeight(request, id=None):
#     if request.method == 'GET':
#         feeders = Feeder.objects.all()
#         data = []
#         for feeder in feeders:
#             data.append({
#                 "mesuredHeight": feeder.mesuredHeight,
#                 "stepCount": feeder.stepCount
#             })
#         return JsonResponse(data, safe=False, status=200)
#     else:
#         return JsonResponse({'error': 'GET method only'}, status=405)