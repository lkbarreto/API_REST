from rest_framework.views import APIView
from rest_framework.response import Response
from productos import serializers

class HelloApiView(APIView):
    """ View prueba"""
    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Retornar lista  de caracteristicas del APIView"""
        an_apiview = [
            'usamos metodos  Http como funciones (get, post, patch, put,delete)',
            'estamapeado manualmente con urls'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ crea un mensaje con nuestro nombre"""
        serializer= self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello{name}'
            return Response ({'message': message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
 
    def put(self, request,pk=None):
        return Response(
            {'method': 'PUT'}
        )

    def patch(self, request,pk=None):
        """Actualizacion parcial"""
        return Response(
            {'method': 'PATCH'}
        )

    def delete(self, request,pk=None):
        """borrar"""
        return Response(
            {'method': 'DELETE'}
        )