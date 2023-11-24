from .serializer import *
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .forms import *
from .models import *
from datetime import date,datetime,timedelta

@api_view(["GET"])
def getUserData(request):
    user = UserSerializer(request.user).data
    return JsonResponse({'user':user})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def getBescData(request):
    besc_data = BesicData.objects.first()
    return JsonResponse({'data':BescDataSirializer(besc_data).data})

@api_view(['POST'])
def Setting(request):
    basc_data = BesicData.objects.first()
    # print(basc_data)
    if basc_data:
        form = BesicDataForm(request.data or None,instance=basc_data)
    else:
        form = BesicDataForm(request.data or None)
    
    if form.is_valid():
        basc_data = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    
    return JsonResponse({'status':True,'data':BescDataSirializer(basc_data).data})

@api_view(['POST'])
def create_organizers(request):
    form = OrganizersForm(request.data,request.FILES)
    
    if form.is_valid():
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':OrganizersSerializer(organizers).data})

@api_view(['POST'])
def update_organizers(request,id):
    organizers = Organizers.objects.get(pk=id)
    
    form = OrganizersForm(request.data,request.FILES,instance=organizers)
    
    if form.is_valid():
        new_organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':OrganizersSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_organizers(request):
    besc_data = Organizers.objects.all()
    return JsonResponse({'data':OrganizersSerializer(besc_data,many=True).data})


@api_view(['GET'])
def get_organizer(request,id):
    besc_data = Organizers.objects.get(pk=id)
    return JsonResponse({'data':OrganizersSerializer(besc_data).data})

@api_view(['DELETE'])
def delete_organizer(request,id):
    besc_data = Organizers.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})

# ======================================= #

@api_view(['POST'])
def create_shepherds(request):
    form = ShepherdsForm(request.data,request.FILES)
    
    if form.is_valid():
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ShepherdsSerializer(organizers).data})

@api_view(['POST'])
def update_shepherds(request,id):
    organizers = Shepherds.objects.get(pk=id)
    
    form = ShepherdsForm(request.data,request.FILES,instance=organizers)
    
    if form.is_valid():
        new_organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ShepherdsSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_shepherds(request):
    besc_data = Shepherds.objects.all()
    return JsonResponse({'data':ShepherdsSerializer(besc_data,many=True).data})


@api_view(['GET'])
def get_shepherd(request,id):
    besc_data = Shepherds.objects.get(pk=id)
    return JsonResponse({'data':ShepherdsSerializer(besc_data).data})

@api_view(['DELETE'])
def delete_shepherds(request,id):
    besc_data = Shepherds.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})

# ====================== Schedule ========================== #

@api_view(['POST'])
def create_schedule(request):
    form = ScheduleForm(request.data,request.FILES)
    
    if form.is_valid():
        schedule = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':ScheduleSirializer(schedule).data})

# @api_view(['POST'])
# def update_schedule(request,id):
#     organizers = Schedule.objects.get(pk=id)
    
#     form = ShepherdsForm(request.data,request.FILES,instance=organizers)
    
#     if form.is_valid():
#         new_organizers = form.save()
#     else:
#         return JsonResponse({'status':False,'error':form.errors})
#     return JsonResponse({'status':True,'data':ShepherdsSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_schedule(request):
    besc_data = Schedule.objects.all()
    settings = BesicData.objects.first()
    d1 = settings.from_date
    d2 = settings.to_date
    
    result1 = abs(d2-d1).days + 1
    print(result1)
    array_of_dates = []
    
    for i in range(0,result1):
        array_of_dates.append(d1+timedelta(days=i))
    
    return JsonResponse({'data':ScheduleSirializer(besc_data,many=True).data,'days':array_of_dates})

@api_view(['DELETE'])
def delete_schedule(request,id):
    besc_data = Schedule.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})


# ======================================= #

@api_view(['POST'])
def create_Speakers(request):
    form = SpeakersForm(request.data,request.FILES)
    
    if form.is_valid():
        organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':SpeakersSerializer(organizers).data})

@api_view(['POST'])
def update_Speakers(request,id):
    organizers = Speakers.objects.get(pk=id)
    
    form = SpeakersForm(request.data,request.FILES,instance=organizers)
    
    if form.is_valid():
        new_organizers = form.save()
    else:
        return JsonResponse({'status':False,'error':form.errors})
    return JsonResponse({'status':True,'data':SpeakersSerializer(new_organizers).data})


@api_view(['GET'])
@permission_classes([])
@authentication_classes([])
def get_Speakers(request):
    besc_data = Speakers.objects.all()
    return JsonResponse({'data':SpeakersSerializer(besc_data,many=True).data})


@api_view(['GET'])
def get_shepherd(request,id):
    besc_data = Speakers.objects.get(pk=id)
    return JsonResponse({'data':SpeakersSerializer(besc_data).data})

@api_view(['DELETE'])
def delete_Speakers(request,id):
    besc_data = Speakers.objects.get(pk=id)
    besc_data.delete()
    return JsonResponse({'status':True})
