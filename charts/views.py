from django.views.generic import TemplateView

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class HomeView(TemplateView):
    template_name = 'charts/chart.html'


class ChartDataView(ListAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class ChartDetailView(RetrieveAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class ChartView(APIView):

    def get(self, request, format=None):
        users = get_user_model().objects.all()
        issues = Issue.objects.all()
        customers = Customer.objects.all()
        products = Product.objects.all()
        categories = Category.objects.all()

        issue_serializer = IssueSerializer(issues, many=True)
        customer_serializer = CustomerSerializer(customers, many=True)
        product_serializer = ProductSerializer(products, many=True)
        category_serializer = CategorySerializer(categories, many=True)
        user_serializer = UserSerializer(users, many=True)

        labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        values = [12, 21, 31, 43, 57, 3]

        data = {
            "labels": labels,
            "values": values,
            "issues": issue_serializer.data,
            "customers": customer_serializer.data,
            "products": product_serializer.data,
            "categories": category_serializer.data,
            "users": user_serializer.data
        }
        return Response(data)

