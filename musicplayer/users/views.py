from django.db.models import Q
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.views import APIView

from musicplayer.utils import Utils
from .models import Users
from .serializers import UsersSerializer, UserDetailSerializer

util_function = Utils()


# Create your views here.
class UserRegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = UsersSerializer

    def post(self, request):
        try:
            email = request.data.get('email')
            username = request.data.get('username')

            user = Users.objects.filter(Q(email=email) | Q(username=username)).first()
            if user:
                data = {
                    "code": 409,
                    "content": "Email or username already exists!",
                }
            else:
                serializer = self.serializer_class(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()

                data = {
                    "code": 201,
                    "content": "Create account successfully!",
                    "data": serializer.data,
                }

            exception = False

        except Exception as e:
            data = {
                "code": 500,
                "error": str(e)
            }

            exception = True

        return util_function.response(data, code=data["code"], exception=exception)


class UserLoginView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = UsersSerializer

    def post(self, request):
        try:
            username_or_email = request.data.get('username_or_email')
            password = request.data.get('password')

            user = Users.objects.filter(Q(username=username_or_email) | Q(email=username_or_email)).first()
            if user:
                if not user.check_password(password):
                    data = {
                        "code": 401,
                        "content": "Wrong Password!",
                    }
                else:
                    serializer = self.serializer_class(user, data={"is_online": True, "refresh_token": "ABCDXYZ"},
                                                       partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

                    data = {
                        "code": 200,
                        "content": "Login Successfully!",
                        "data": serializer.data
                    }

            else:
                data = {
                    "code": 404,
                    "content": "User not found or not activated!",
                }

            exception = False

        except Exception as e:
            data = {
                "code": 500,
                "error": str(e)
            }
            exception = True

        return util_function.response(data, code=data["code"], exception=exception)


class UserLogoutView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = UsersSerializer

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')

            user = Users.objects.filter(refresh_token=refresh_token).first()
            if user:
                serializer = self.serializer_class(user, data={"is_online": False}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                data = {
                    "code": 200,
                    "content": "Logout successfully!"
                }
            else:
                data = {
                    "code": 404,
                    "content": "Refresh token Invalid!",
                }

            exception = False

        except Exception as e:
            data = {
                "code": 500,
                "error": str(e)
            }
            exception = True

        return util_function.response(data, code=data["code"], exception=exception)


class ChangePasswordView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = UsersSerializer

    def put(self, request):
        try:
            email = request.data.get('email')
            old_password = request.data.get('old_password')
            new_password = request.data.get('new_password')

            user = Users.objects.filter(email=email, is_active=True, is_deleted=False).first()
            if user:
                if user.check_password(old_password):
                    serializer = self.serializer_class(user, data={"password": new_password}, partial=True)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()

                    data = {
                        "code": 200,
                        "content": "Change Password Successfully!",
                    }
                else:
                    data = {
                        "code": 401,
                        "content": "Wrong Password!",
                    }
            else:
                data = {
                    "code": 404,
                    "content": "User not found or not activated!",
                }

            exception = False

        except Exception as e:
            data = {
                "code": 500,
                "errors": str(e),
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)


class UserDetailView(APIView):
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    serializer_class = UserDetailSerializer

    @staticmethod
    def get_user_by_user_id(user_id):
        user = Users.objects.filter(user_id=user_id, is_active=True, is_deleted=False).first()
        if user:
            return user
        else:
            return None

    def get(self, request, user_id):
        try:
            user = self.get_user_by_user_id(user_id=user_id)
            if user:
                serializer = self.serializer_class(user)
                data = {
                    "code": 200,
                    "content": "Successful get user!",
                    "data": serializer.data
                }
            else:
                data = {
                    "code": 404,
                    "content": "User not found or not activated!",
                }

            exception = False

        except Exception as e:
            data = {
                "error": str(e),
                "code": 500,
            }
            exception = True

        return util_function.response(data, code=data["code"], exception=exception)

    def put(self, request, user_id):
        try:
            user = self.get_user_by_user_id(user_id=user_id)
            if user:
                serializer = self.serializer_class(user, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                data = {
                    "code": 200,
                    "content": "Successful changes user information!",
                    "data": serializer.data
                }
            else:
                data = {
                    "code": 404,
                    "content": "User not found or not activated!",
                }

            exception = False

        except Exception as e:
            data = {
                "code": 500,
                "errors": str(e),
            }

            exception = True

        return util_function.response(data, code=data["code"], exception=exception)

    def delete(self, request, user_id):
        try:
            user = self.get_user_by_user_id(user_id=user_id)
            if user:
                serializer = self.serializer_class(user, data={"is_deleted": True}, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                data = {
                    "code": 204,
                    "content": "Delete user successfully!",
                }
            else:
                data = {
                    "code": 404,
                    "content": "User not found or not activated!",
                }

            exception = False


        except Exception as e:
            data = {
                "code": 500,
                "errors": str(e),
            }

            exception = True

        return util_function.response(data=data, code=data["code"], exception=exception)
