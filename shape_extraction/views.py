from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import requests
from PIL import Image


class ShapeExtractionAPIView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        detected_image_url = request.data['url']
        resp = requests.get(detected_image_url)
        print('request ok')
        detected_image = Image.open(resp.content)
        # TODO : model restore 하고 결과값 불러오기
        return Response({"shape_result": shape_result}, status=status.HTTP_200_OK)