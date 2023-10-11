from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from haberler.models import Makale
from haberler.api.serializer import MakaleSerializer


@api_view(["GET"])
def Get(req):
    if req.method == "GET":
        makaleler = Makale.objects.filter(aktif=True)
        serializer = MakaleSerializer(makaleler, many=True)
        return Response(serializer.data)


@api_view(["POST"])
def Post(req):
    if req.method == "POST":
        serializer = MakaleSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def GetDetail(req,pk):
   if req.method == "GET":
        try:
         makale_instancec = Makale.objects.get(pk=pk)
         serializer = MakaleSerializer(makale_instancec)
         return Response(serializer.data)
        except Makale.DoesNotExist:
            return Response({
                'ERROR':{
                    'CODE' : 404,
                    'MESSAGE':f'{pk} böyle bir ID Numarasi Yok.'
                }
            },status=status.HTTP_404_NOT_FOUND)
        
@api_view(['GET'])
def Delete(req,pk):
        Makale.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['PUT'])
def Update(req,pk):
    makale = Makale.objects.get(pk =pk)
    serializer = MakaleSerializer(makale,data=req.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_200_OK)