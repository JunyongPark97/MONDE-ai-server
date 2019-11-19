from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import requests
from PIL import Image


class ObjectDetectionAPIView(GenericAPIView):

    def post(self, request, *args, **kwargs):
        image_url = request.data['url']
        resp = requests.get(image_url)
        print('request ok')
        image = Image.open(resp.content)
        # TODO : model restore 하고 결과값 불러오기
        return Response({"detected_image": detected_image}, status=status.HTTP_200_OK)
