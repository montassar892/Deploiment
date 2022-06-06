import email
import json
from operator import contains
from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.http.response import JsonResponse

from app.models import Candidat
from app.serializers import CandidatSerilaizer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view 
import os 
import sys

#sys.path.append('/home/montassar/Desktop/PFE2/')
from app.code import pdf_to_text , convert_pdf_to_image , yolov5 , pytesseractoutput , delrepetition , delete_used_folders , json_create , dict_create , ocroutput
# Create your views here.
#@api_view ['POST']

@csrf_exempt
def CandidatApi(request):
        
        data = {
             'name': request.POST['name'] ,
             "lastname" : request.POST['lastname'] ,
             "email" : request.POST['email'] ,
             "phonenum" : request.POST['phonenum'] ,
             "dateofbirth" : request.POST['dateofbirth'] ,
             "cv" : request.FILES['cv'] 
             
         } 
        """
         
         #candidat_data= JSONParser().parse(request)
         #print(data)
         #candidat_serializer = CandidatSerilaizer(data=data)
         #print(candidat_serializer)
         #return JsonResponse()
"""""
         #file_name = default_storage.save(file.name,file)
         #candidat_data= JSONParser().parse(request)
        #print(data)
        candidat_serializer = CandidatSerilaizer(data=data)
        #print(candidat_serializer)
         
        if candidat_serializer.is_valid():
             file=data["cv"]
             #default_storage.save(file.name,file)
             candidat_serializer.save()
             #return JsonResponse("Added Successfully!" , safe=False)
             input_path='/home/montassar/Desktop/PFE2/backend/webapp/media/'+os.listdir('media')[0]
             print("input path",input_path)
             cv= pdf_to_text(input_path)
             output_path="/home/montassar/Desktop/PFE2/IA/yolo/yolov5/test/img"
             print("----------------convert pdf to image--------------")
             convert_pdf_to_image(input_path,output_path)
             print("-----------------yolov5-------------")
             yolov5()
             print("-----------------OCR-----------------")
             #myCV = pytesseractoutput() 
             myCV = ocroutput()
             myCVf = delrepetition(myCV)
             delete_used_folders()
             print("---------------JSONresponse-----------")
             result=json_create(dict_create(myCVf))
             #print(candidat_serializer.errors)    
            
           

             with open('/home/montassar/Desktop/PFE2/backend/webapp/Result.json') as json_data:
               data_dict = json.load(json_data)
               #print(data_dict["contact"])



        data1 = {
             'name': request.POST['name'] ,
             "lastname" : request.POST['lastname'] ,
             "email" : request.POST['email'] ,
             "phonenum" : request.POST['phonenum'] ,
             "dateofbirth" : request.POST['dateofbirth'] ,
             "cv" : request.FILES['cv'] ,
             "contact": data_dict["contact"],
             "profil": data_dict["profil"],
             "langues": data_dict["langues"],
             "formation": data_dict["formation"],
             "projets": data_dict["projets"],
             "experience": data_dict["experience"],
             "competences": data_dict["competences"],
             "autres": data_dict["autres"]

            } 
        ## Deleting files in media folder 
        dir_list = os.listdir("/home/montassar/Desktop/PFE2/backend/webapp/media")
        for i in dir_list : 
            os.remove("/home/montassar/Desktop/PFE2/backend/webapp/media/"+i)
        ## Deleting images     
        for j  in os.listdir("/home/montassar/Desktop/PFE2/backend/webapp"):
            if '.jpg' in j:
                os.remove("/home/montassar/Desktop/PFE2/backend/webapp/"+j)
                        
        
       
        return JsonResponse({ "name": data1["name"],
                              "lastname":  data1["lastname"],
                              "email" : data1["email"],
                              "phonenum" : data1["phonenum"],
                              "dateofbirth" : data1["dateofbirth"],
                              "contact" : data1["contact"],
                              "profil" : data1["profil"],
                              "langues" : data1["langues"],
                              "profil" : data1["profil"],
                              "formation" : data1["formation"],
                              "projets" : data1["projets"],
                              "experience" : data1["experience"],
                              "competences" : data1["competences"],
                              "autres" : data1["autres"]



        },safe=False)
        



# @csrf_exempt 
# def SaveFile(request):
#      file=request.FILES['myFile']
#      file_name = default_storage.save(file.name,file)
# # 
#      return   JsonResponse(file_name , safe=False)

""" @csrf_exempt
def CandidatApi(request):
    if request.method == "POST":
        data = {
            'name': request.POST["name"],
            'lastname': request.POST["lastname"],
            "email" : request.POST['email'] ,
            "phonenum" : request.POST['phonenum'] ,
            "dateofbirth" : request.POST['dateofbirth'] ,
            "cv" : request.FILES['cv'] ,

        }
        candidat_serializer = CandidatSerilaizer(data=data)
        if candidat_serializer.is_valid():
            candidat_serializer.save()
            return JsonResponse({"name": data["name"] ,"lastname":data["lastname"] , "email" :data["email"] , "phonenum":data["phonenum"] , "dateofbirth":data["dateofbirth"]}, safe=False)
        print(candidat_serializer.errors)    
        return JsonResponse("Failed to Add",safe=False)
 """

