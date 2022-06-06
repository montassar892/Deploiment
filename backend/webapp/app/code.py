import sys
sys.path.append('/home/montassar/Desktop/PFE2/IA/yolo/yolov5/')
from detect import main,parse_opt
sys.argv=['']
del sys

import timeit 
import json 

import collections
 
try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = dict

import pandas as pd
import pickle 

def yolov5():
    opt = parse_opt()
    main(opt)




#pdf2img importation + function
from pdf2image import convert_from_path
import os
import ntpath

def convert_pdf_to_image(input_path,output_path):
  
  file_name=ntpath.basename(input_path)
  f_name, f_ext = os.path.splitext(file_name)

  output_folder_path=output_path+"/"+f_name
  try:
    os.mkdir (output_folder_path)
  except FileExistsError:
    pass
    

  pages = convert_from_path(input_path,output_folder=output_folder_path,fmt="JPEG")
  for i in range(len(pages)):
    
    pages[i].save(str(f_name)+"_"+str(i)+'.jpg', 'JPEG')
  return(output_folder_path)   
  
# PDF2TEXT
  
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

#from cStringIO import StringIO

def pdf_to_text(path):

    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # Extract text
    fp = open(path, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()

    # Get text from StringIO
    text = sio.getvalue()

    # Cleanup
    device.close()
    sio.close()

    return text


#OCR function
import easyocr
import cv2
from matplotlib import pyplot as plt
import os


def image_to_text(crop_path):
  IMAGE_PATH = crop_path
  reader = easyocr.Reader(['fr'])
  result = reader.readtext(IMAGE_PATH , detail=0)

  ch=''
  for i in result:
    ch =ch+' '+i
  return(ch)  

def ocroutput():
    myCV = []
    for i in os.listdir("/home/montassar/Desktop/PFE2/IA/yolo/yolov5/runs/detect/exp/crops/section") :
        myCV.append(image_to_text('/home/montassar/Desktop/PFE2/IA/yolo/yolov5/runs/detect/exp/crops/section/'+i))
    return(myCV)  


#Pytesseract_OCR
import pytesseract as tess 
from PIL import Image


def pytesseractoutput():
    myCV = []
    for i in os.listdir("/home/montassar/Desktop/PFE2/IA/yolo/yolov5/runs/detect/exp/crops/section") :
        myCV.append(tess.image_to_string('/home/montassar/Desktop/PFE2/IA/yolo/yolov5/runs/detect/exp/crops/section/'+i))
    return(myCV)


    
    
    
    
 
def delrepetition(l):
  
  for i in range(len(l)):
    for j in range(len(l)):
      if (l[i].find(l[j])!=-1 ) and (i!=j):
        l[j]=''
  for elt in list(l):
    if (elt == ''):
      l.remove(elt)

  return(l)

#delete folders
import shutil

def delete_used_folders():
  path1 = '/home/montassar/Desktop/PFE2/IA/yolo/yolov5/runs/detect/exp'
  path2 = '/home/montassar/Desktop/PFE2/IA/yolo/yolov5/test/img/1'
  shutil.rmtree(path1)
  shutil.rmtree(path2)

# NER
#### Spacy has been replaced from (3.3.0) to 
import spacy

def get_entities (resume):
  from joblib import load
  #Load the model

  with open('/home/montassar/Desktop/PFE2/IA//nlp_model_diplome.pkl', 'rb') as f:
    nlp_model_diplome = pickle.load(f)

  # with open('/home/montassar/Desktop/PFE2/nlp_model_societe.pkl', 'rb') as f:
  #  nlp_model_societe = pickle.load(f)

  # with open('/home/montassar/Desktop/PFE2/nlp_model_nom_prenom.pkl', 'rb') as f:
  #  nlp_model_nom_prenom = pickle.load(f)
  
  # with open('/home/montassar/Desktop/PFE2/nlp_model_titre.pkl', 'rb') as f:
  #  nlp_model_titre = pickle.load(f)

  # with open('home/montassar/Desktop/PFE2/nlp_model_adresse.pkl', 'rb') as f:
  #  nlp_model_adresse = pickle.load(f)

   #with open('nlp_model_email.pickle', 'rb') as f:
    #nlp_model_email = pickle.load(f)

   #with open('nlp_model_skills.pickle', 'rb') as f:
    #nlp_model_skills = pickle.load(f)
  
  # education=nlp_model_diplome(resume)
  # societe=nlp_model_societe(resume)
  # nom_prenom=nlp_model_nom_prenom(resume)
  # adresse=nlp_model_adresse(resume)
  # titre=nlp_model_titre(resume)

  #email=nlp_model_email(resume)
  #skills=nlp_model_skills(resume)



  # entities={}

  # entities['nom_prenom']=[] 
  # entities['adresse']=[] 
  # entities['titre']=[] 
  # entities['education']=[] 
  # entities['experience']=[]

  #entities['skills']=[] 
  #entities['email']=[] 


  # for ent in education.ents:
  #     entities['education'].append(ent.text)    #get entities label
  
  # for ent in societe.ents:
  #     entities['experience'].append(ent.text)    #get entities label

  # for ent in nom_prenom.ents:
  #     entities['nom_prenom'].append(ent.text)
  
  # '''for ent in skills.ents:
  #     entities['skills'].append(ent.text)
  # for ent in email.ents:
  #     entities['email'].append(ent.text)    #get entities label'''

  # for ent in adresse.ents:
  #     entities['adresse'].append(ent.text)
  
  # for ent in titre.ents:
  #     entities['titre'].append(ent.text)
 
    
    
  # return(entities)




## Create the dictionnary 
def dict_create(cv):
  model = pickle.load(open('/home/montassar/Desktop/PFE2/IA/models/svm_model_final_pickle.pkl','rb'))
  cv_dict = OrderedDict({
      "nom_prenom":"",
      "email":"",
      "phone_number":"",  
      "contact": "",
      "profil" : "",
      "langues" : "",
      "formation" : "",
      "projets" : "",
      "experience" : "",
      "competences": "",
      "autres": ""
   })
  predicted_label=""
  for i in cv:
     liste=[]
     liste.append(i)
     predicted_label = str(model.predict(pd.Series(liste))[0])
     i=i.replace("'","")
     cv_dict[predicted_label] += str.lower(i)
  return(cv_dict)

## Convert Dictionnary to json object :


def json_create(dic):
  json_cv = json.dumps(dic, indent = 4) 
  out_file = open("Result.json","w")
  json.dump(dic,out_file,   indent=4)
  out_file.close()
  #return(json_cv)

if __name__ == "__main__":
    tic = timeit.default_timer()
    input_path='/home/montassar/Desktop/PFE2/IA/yolo/yolov5/test/pdf/1.pdf'
    cv= pdf_to_text(input_path)
    #entities=get_entities(cv)
    #print(entities)

    output_path="/home/montassar/Desktop/PFE2/IA/yolo/yolov5/test/img"
    print("----------------convert pdf to image--------------")
    convert_pdf_to_image(input_path,output_path)
    print("-----------------yolov5-------------")
    yolov5()
    '''
    tiic = timeit.default_timer()
    print(tiic - tic)
    #import time 
    #time.sleep(20)
    '''
    #print("-----------------OCR-----------------")
    #myCV = ocroutput()
    myCV = pytesseractoutput() 
    myCVf = delrepetition(myCV)
    delete_used_folders()
    for i in range(len(myCVf)):
        print("**************************section***************************")
        print(myCVf[i])
    ## check processing time       
    #toc = timeit.default_timer()
    # print(toc - tiic)
   

    # Create the Json response :

    print("**************************JSONRESPONSE************************")
    print(json_create(dict_create(myCVf)))

    #toc = timeit.default_timer()
    #print(toc - tic)





