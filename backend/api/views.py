# from django.shortcuts import render
# Vista capaz de procesar las respuestas.
from django.views import View
from .models import Information
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class InformationView(View):

    # Codigo que se ejecuta cada vez que realizamos/enviamos/despachemos una petición
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        informations = list(Information.objects.values())
        if len(informations)>0:
            datos = {'message': "Success", 'informations': informations}
        else:
            datos = {'message': "Error, Informations not found.", 'informations': []}
        return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        json_data = json.loads(request.body)
        prompt = json_data['question']
        prompt_answer = "answer"

        # Almacenamiento de pregunta y respuesta
        # Information.objects.create(question=json_data['question'], answer=json_data['answer'])
        datos = {'message': "Success", 'answer': prompt_answer}
        return JsonResponse(datos)