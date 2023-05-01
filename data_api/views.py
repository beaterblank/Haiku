from django.http import JsonResponse
from django.shortcuts import render
from .models import Content

# Create your views here.
def get_content_all(request):
    content_all = [{'id':x.content_id,'content':x.body} for x in Content.objects.all()]
    return JsonResponse({'content_all': content_all})
    
