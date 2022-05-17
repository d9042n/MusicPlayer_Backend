# Create your views here.
from musicplayer.utils import Utils
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.views import APIView
from songs.models import Song
from songs.serializers import SongSerializer
from songs.serializers import SongDetailSerializer

util_function = Utils()


class SongsView(APIView):
    serializer_class = SongSerializer

    def get(self, request):
        try:
            songs = Song.objects.filter().all()
            serializer = self.serializer_class(songs, many=True)

            data = {
                "code": 200,
                "content": "Get successfully!",
                "data": serializer.data,
            }

            exception = False

        except Exception as e:
            data = {
                "error": str(e),
                "code": 500,
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save()

                data = {
                    "code": 201,
                    "content": "Create song successfully!",
                    "data": serializer.data,
                }
            else:
                raise ValidationError(serializer.errors)

            exception = False

        except Exception as e:
            data = {
                "error": str(e),
                "code": 500,
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)


class SongDetailView(APIView):
    serializer_class = SongDetailSerializer

    @staticmethod
    def get_object(id):
        try:
            return Song.objects.get(id=id)

        except Song.DoesNotExist:
            return None

    # READ
    def get(self, request, id):
        try:
            song = self.get_object(id)
            if song:
                serializer = self.serializer_class(song)
                data = {
                    "code": 200,
                    "content": "Get Successfully!",
                    "data": serializer.data
                }

            else:
                raise NotFound("Song not found!")

            exception = False

        except Exception as e:
            data = {
                "error": str(e),
                "code": 500,
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)

    # UPDATE
    def put(self, request, id):
        try:
            song = self.get_object(id)
            serializer = self.serializer_class(song, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                data = {
                    "code": 200,
                    "content": serializer.data,
                }

            else:
                raise ValidationError(serializer.errors)

            exception = False

        except Exception as e:
            data = {
                "error": str(e),
                "code": 500,
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)

    # DELETE
    def delete(self, request, id):
        try:
            song = self.get_object(id)
            song.delete()

            data = {
                "content": "No content!",
                "code": 204,
            }

            exception = False

        except Exception as e:
            data = {
                "error": str(e),
                "code": 400,
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)
