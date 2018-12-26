from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import PaginacaoContatos
from .serializers import *


class ContatoList(APIView):
    def get(self, request):
        try:
            lista_contatos = Contato.objects.all()
            paginator = PaginacaoContatos()
            result_page = paginator.paginate_queryset(lista_contatos, request)
            serializer = ContatoSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContatoCreate(APIView):
    def post(self, request):
        try:
            serializer = ContatoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContatoDetails(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({
                    'mensagem': "O ID deve ser maior que zero"
                }, status=status.HTTP_400_BAD_REQUEST)
            contato = Contato.objects.get(pk=pk)
            serializer = ContatoSerializer(contato)
            return Response(serializer.data)
        except Contato.DoesNotExist:
            return JsonResponse({
                'mensagem': "O contato não existe"
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({
                'mensagem': "Ocorreu um erro no servidor"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({
                    'mensagem': "O ID deve ser maior que zero"
                }, status=status.HTTP_400_BAD_REQUEST)

            contato = Contato.objects.get(pk=pk)
            contato.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Contato.DoesNotExist:
            return JsonResponse({'mensagem': "O Contato não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContatoUpdate(APIView):
    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({
                    'mensagem': "O ID deve ser maior que zero"
                }, status=status.HTTP_400_BAD_REQUEST)
            contato = Contato.objects.get(pk=pk)
            serializer = ContatoSerializer(contato, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Contato.DoesNotExist:
            return JsonResponse({'mensagem': "O Contato não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
