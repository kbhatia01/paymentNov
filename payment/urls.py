from django.urls import path

from payment import views
from payment.views import PaymentView

urlpatterns = [
    path('',PaymentView.as_view(), name='payment'),
]