from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class BeritaViewSet(viewsets.ModelViewSet):
    queryset = Berita.objects.all()
    serializer_class = BeritaSerializer
    authentication_classes = (TokenAuthentication,)

class ProdukViewSet(viewsets.ModelViewSet):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    authentication_classes = (TokenAuthentication,)

class PelatihViewSet(viewsets.ModelViewSet):
    queryset = Pelatih.objects.all()
    serializer_class = PelatihSerializer
    authentication_classes = (TokenAuthentication,)

class SiswaViewSet(viewsets.ModelViewSet):
    queryset = Siswa.objects.all()
    serializer_class = SiswaSerializer
    authentication_classes = (TokenAuthentication,)

class PesananViewSet(viewsets.ModelViewSet):
    queryset = Pesanan.objects.all()
    serializer_class = PesananSerializer
    authentication_classes = (TokenAuthentication,)



# class MovieViewSet(viewsets.ModelViewSet):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     authentication_classes = (TokenAuthentication,)

#     @action(detail=True, methods=['POST'])
#     def rate_movie(self, request, pk=None):
#         if 'stars' in request.data:

#             movie = Movie.objects.get(id=pk)
#             stars = request.data['stars']
#             user = request.user
#             # user = User.objects.get(id=1)

#             try:
#                 rating = Rating.objects.get(user=user.id, movie=movie.id)
#                 rating.stars = stars
#                 rating.save()
#                 serializer = RatingSerializer(rating, many=False)
#                 response = {'message': 'Rating updated', 'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)
#             except:
#                 rating = Rating.objects.create(user=user, movie=movie, stars=stars)
#                 serializer = RatingSerializer(rating, many=False)
#                 response = {'message': 'Rating created', 'result': serializer.data}
#                 return Response(response, status=status.HTTP_200_OK)

#         else:
#             response = {'message': 'You need to provide stars'}
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)


# class RatingViewSet(viewsets.ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer
#     authentication_classes = (TokenAuthentication,)

#     def update(self, *args, **kwargs):
#         response = {'message': 'You cannot update rating like this. Use rate_movie instead!'}
#         return Response(response, status=status.HTTP_400_BAD_REQUEST)

#     def create(self, *args, **kwargs):
#         response = {'message': 'You cannot create rating like this. Use rate_movie instead!'}
#         return Response(response, status=status.HTTP_400_BAD_REQUEST)
