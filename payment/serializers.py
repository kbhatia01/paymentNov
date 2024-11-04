from rest_framework import serializers


class PaymentRequestSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    amount = serializers.IntegerField()
