from celery import shared_task
import requests
from .models import Endpoint

@shared_task
def verifica_endpointuri():
    for endpoint in Endpoint.objects.all():
        try:
            response = requests.get(endpoint.url, timeout=5)

            if response.status_code >= 200 and response.status_code <= 302:
                endpoint.stare = 'Stable'
            else:
                endpoint.stare = 'Unstable'
                
        except requests.exceptions.RequestException:
            endpoint.stare = 'Down'
        
        endpoint.save()