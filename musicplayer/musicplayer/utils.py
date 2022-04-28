import random

from rest_framework import status as st
from rest_framework.response import Response


class Utils:
    response_code = {
        200: [st.HTTP_200_OK, 'success'],
        201: [st.HTTP_201_CREATED, 'created'],
        202: [st.HTTP_202_ACCEPTED, 'accepted'],
        203: [st.HTTP_203_NON_AUTHORITATIVE_INFORMATION, 'non authoritative'],
        204: [st.HTTP_204_NO_CONTENT, 'no content'],
        205: [st.HTTP_205_RESET_CONTENT, 'reset content'],
        206: [st.HTTP_206_PARTIAL_CONTENT, 'partial content'],
        207: [st.HTTP_207_MULTI_STATUS, 'multi status'],
        208: [st.HTTP_208_ALREADY_REPORTED, 'already reported'],
        209: [st.HTTP_226_IM_USED, 'im used'],
        300: [st.HTTP_300_MULTIPLE_CHOICES, 'multiple choices'],
        301: [st.HTTP_301_MOVED_PERMANENTLY, 'moved permanently'],
        302: [st.HTTP_302_FOUND, 'found'],
        303: [st.HTTP_303_SEE_OTHER, 'see other'],
        304: [st.HTTP_304_NOT_MODIFIED, 'no modified'],
        305: [st.HTTP_305_USE_PROXY, 'use proxy'],
        306: [st.HTTP_306_RESERVED, 'reserved'],
        307: [st.HTTP_307_TEMPORARY_REDIRECT, 'temporary redirect'],
        308: [st.HTTP_308_PERMANENT_REDIRECT, 'permanent redirect'],
        400: [st.HTTP_400_BAD_REQUEST, 'bad request'],
        401: [st.HTTP_401_UNAUTHORIZED, 'unauthorized'],
        402: [st.HTTP_402_PAYMENT_REQUIRED, 'payment required'],
        403: [st.HTTP_403_FORBIDDEN, 'forbidden'],
        404: [st.HTTP_404_NOT_FOUND, 'not found'],
        405: [st.HTTP_405_METHOD_NOT_ALLOWED, 'method not allowed'],
        406: [st.HTTP_406_NOT_ACCEPTABLE, 'not acceptable'],
        407: [st.HTTP_407_PROXY_AUTHENTICATION_REQUIRED, 'proxy authentication required'],
        408: [st.HTTP_408_REQUEST_TIMEOUT, 'request timeout'],
        409: [st.HTTP_409_CONFLICT, 'conflict'],
        410: [st.HTTP_410_GONE, 'gone'],
        411: [st.HTTP_411_LENGTH_REQUIRED, 'length required'],
        412: [st.HTTP_412_PRECONDITION_FAILED, 'precondition failed'],
        413: [st.HTTP_413_REQUEST_ENTITY_TOO_LARGE, 'request entity too large'],
        414: [st.HTTP_414_REQUEST_URI_TOO_LONG, 'request uri too long'],
        415: [st.HTTP_415_UNSUPPORTED_MEDIA_TYPE, 'unsupported media type'],
        416: [st.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE, 'requested range not satisfiable'],
        417: [st.HTTP_417_EXPECTATION_FAILED, 'expectation failed'],
        422: [st.HTTP_422_UNPROCESSABLE_ENTITY, 'unprocessable entity'],
        423: [st.HTTP_423_LOCKED, 'locked'],
        424: [st.HTTP_424_FAILED_DEPENDENCY, 'failed dependency'],
        426: [st.HTTP_426_UPGRADE_REQUIRED, 'upgrade required'],
        428: [st.HTTP_428_PRECONDITION_REQUIRED, 'precondition required'],
        429: [st.HTTP_429_TOO_MANY_REQUESTS, 'too many requests'],
        431: [st.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE, 'request header fields too large'],
        451: [st.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS, 'unavailable for legal reasons'],
        500: [st.HTTP_500_INTERNAL_SERVER_ERROR, 'internal server error'],
        501: [st.HTTP_501_NOT_IMPLEMENTED, 'not implemented'],
        502: [st.HTTP_502_BAD_GATEWAY, 'bad gateway'],
        503: [st.HTTP_503_SERVICE_UNAVAILABLE, 'service unavailable'],
        504: [st.HTTP_504_GATEWAY_TIMEOUT, 'gateway timeout'],
        505: [st.HTTP_505_HTTP_VERSION_NOT_SUPPORTED, 'http version not supported'],
        506: [st.HTTP_506_VARIANT_ALSO_NEGOTIATES, 'variant also negotiates'],
        507: [st.HTTP_507_INSUFFICIENT_STORAGE, 'insufficient storage'],
        508: [st.HTTP_508_LOOP_DETECTED, 'loop detected'],
        509: [st.HTTP_509_BANDWIDTH_LIMIT_EXCEEDED, 'bandwidth limit exceeded'],
        510: [st.HTTP_510_NOT_EXTENDED, 'not extended'],
        511: [st.HTTP_511_NETWORK_AUTHENTICATION_REQUIRED, 'network authentication required']
    }

    def response(self, data, code=200, status='success', exception=False):
        if exception:
            status = 'failed'
            code = 500

        response = Response()
        data["status"] = self.response_code[data["code"]][1] if "code" in data else self.response_code[code][1]
        data["status_code"] = status
        response.data = data

        response.status_code = self.response_code[data["code"]][0] if "code" in data else self.response_code[code][0]

        return response

    def user_id_generator(self):
        prefix = 'MP'
        user_id = str(''.join(random.sample('0123456789', 10)))

        return prefix + user_id

    def active_token_generator(self):
        random_int_list = random.sample(range(0, 10), 6)
        random_int_list = [str(i) for i in random_int_list]
        active_token = '' + ''.join(random_int_list)

        return active_token
