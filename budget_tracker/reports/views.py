from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from transactions.models import Transaction
from django.db.models import Sum
from transactions.serializers import TransactionSerializer

class SummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        total_income = transactions.filter(type='Income').aggregate(Sum('amount'))['amount__sum'] or 0
        total_expenses = transactions.filter(type='Expense').aggregate(Sum('amount'))['amount__sum'] or 0
        balance = total_income - total_expenses
        return Response({
            'total_income': total_income,
            'total_expenses': total_expenses,
            'balance': balance
        })

class FilterView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transaction.objects.filter(user=request.user)
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        category_id = request.query_params.get('category_id')

        if start_date:
            transactions = transactions.filter(date__gte=start_date)
        if end_date:
            transactions = transactions.filter(date__lte=end_date)
        if category_id:
            transactions = transactions.filter(category_id=category_id)

        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)