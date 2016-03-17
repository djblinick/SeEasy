from rest_framework import viewsets, status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rec_app.models import Website, Category, RecQ
from rec_app.serializers import *

class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer

    # @api_view(['GET'])
    # def get_all_web(request):
    #     if request.method == 'GET':
    #         websites = Website.objects.all()
    #         serializer = WebsiteSerializer(websites, many=True)
    #         return Response(serializer.data)
    #
    # @api_view(['POST'])
    # def add_web(request):
    #     if request.method == 'POST':
    #         serializer = WebsiteSerializer(data=request.DATA)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         else:
    #             return Response(
    #                 serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RecViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Rec.objects.all()
    serializer_class = RecSerializer







