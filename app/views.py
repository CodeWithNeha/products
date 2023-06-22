from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from datetime import timedelta


# Django rest api for creating products, deleting, updating and list of all products
class ProductsViewManage(viewsets.ViewSet):
    queryset = ProductsDetails.objects
    subQueryset = ProductLogs.objects
    serializer_class = ProductSel
    
    def create(self,request):
        try:
            requestData = request.data
            try:
                title = requestData['title']
                description = requestData['description']
                price = requestData['price']
            except KeyError as e:
                error = str(error)
                return Response({
                        "message":f"Please enter valid {error} of product."
                    },status = status.HTTP_400_BAD_REQUEST)
            self.queryset.create(
                title = title,
                description = description,
                price = price
            )
            return Response({
                "message":"Product added successfully."
            },status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def list(self,request):
        try:
            data = self.queryset.all()
            serialized = self.serializer_class(data,many=True).data
            return Response({
                "data":serialized,
                "message":"Product data fetched successfully."
            },status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def retrieve(self,request,*args, **kwargs):
        try:
            try:
                id = self.kwargs['pk']
            except:
                return Response({
                        "message":"Please enter valid id of product."
                    },status = status.HTTP_400_BAD_REQUEST)
            data = self.queryset.get(id = id)
            self.subQueryset.create(
                product = data
            )
            serialized = self.serializer_class(data).data
            return Response({
                "data":serialized,
                "message":"Product details fetched successfully."
            },status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def update(self,request,*args, **kwargs):
        try:
            requestData = request.data
            try:
                id = self.kwargs['pk']
            except:
                return Response({
                        "message":"Please enter valid id of product."
                    },status = status.HTTP_400_BAD_REQUEST)
            data = self.queryset.get(id = id)
            try:
                title = requestData['title']
                data.title = title
            except:
                pass
            try:
                description = requestData['description']
                data.description = description
            except:
                pass
            try:
                price = requestData['price']
                data.price = price
            except:
                pass
            data.save()
            return Response({
                "message":"Product details updated successfully."
            },status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def destroy(self,request,*args, **kwargs):
        try:
            try:
                id = self.kwargs['pk']
            except:
                return Response({
                        "message":"Please enter valid id of product."
                    },status = status.HTTP_400_BAD_REQUEST)
            data = self.queryset.get(id = id)
            data.delete()
            return Response({
                "message":"Product deleted successfully."
            },status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
class FetchMostSearched(viewsets.ViewSet):
    queryset = ProductsDetails.objects
    subQueryset = ProductLogs.objects
    serializer_class = ProductSel
    
    def list(self,request):
        try:
            filterBy = request.GET.get('filterBy')
            if filterBy == "all": # all together
                topfiveviewed = self.subQueryset.filter().order_by('viewed_at').values('product_id')
            elif filterBy == "lastDay": # Last Day
                topfiveviewed = self.subQueryset.filter(viewed_at__gte=timezone.now()-timedelta(days=1)).order_by('viewed_at').values('product_id')
            else: # Last Week
                topfiveviewed = self.subQueryset.filter(viewed_at__gte=timezone.now()-timedelta(weeks=1)).order_by('viewed_at').values('product_id')
            data = self.queryset.filter(id__in = topfiveviewed)[:5]
            serialized = self.serializer_class(data,many=True).data
            return Response({
                "data":serialized,
                "message":"Product data fetched successfully."
            },status = status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "message":"Internal Server Error"
            },status = status.HTTP_500_INTERNAL_SERVER_ERROR)