from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from rest_framework.views import APIView

from payment.Service import PaymentService
from payment.serializers import PaymentRequestSerializer


class PaymentView(APIView):

    def __init__(self):
        super().__init__()
        self.service = PaymentService()

    def post(self, request):
        serializer = PaymentRequestSerializer(data=request.data)
        if serializer.is_valid():
            order_id = serializer.validated_data.get('order_id')
            amount = serializer.validated_data.get('amount')
            try:
                payment_link = self.service.initiate_payment(order_id, amount)
                return Response({'payment_link': payment_link}, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)