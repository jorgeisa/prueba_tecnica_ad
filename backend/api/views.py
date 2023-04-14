# from django.shortcuts import render
# Vista capaz de procesar las respuestas.
from django.views import View
from django.http.response import JsonResponse
from .models import Information


from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

import json
import openai 
from .secret_key import API_KEY
openai.api_key = API_KEY

# Create your views here.
class InformationView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        try:
            informations = list(Information.objects.values())
            if len(informations)>0:
                datos = {'message': "Success", 'informations': informations}
            else:
                datos = {'message': "Informations not found.", 'informations': []}
        except:
            datos = {'message': "Unexpected Error", 'informations': []}
        return JsonResponse(datos)

    def post(self, request):
        try:
            json_data = json.loads(request.body)
            prompt = str(json_data['question'])

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            prompt_answer = str(response.choices[0].message['content'])
            
            # Almacenamiento de pregunta y respuesta
            Information.objects.create(question=prompt, answer=prompt_answer)
            datos = {'message': "Success", 'answer': prompt_answer}
        except:
            datos = {'message': "Unexpected Error", 'answer': "Error"}
        
        return JsonResponse(datos)