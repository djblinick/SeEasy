from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from similarweb import ContentClient
from django.http import HttpResponse
from csc import similar
import unirest

@api_view(['GET'])
def qsimweb(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        similar.similar("jpost.com")



