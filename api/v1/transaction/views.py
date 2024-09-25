# api/v1/transaction/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from api.v1.common.models import Transactions
from .serializers import TransactionSerializer

class TransactionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        transactions = Transactions.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, transaction_id):
        try:
            return Transactions.objects.get(id=transaction_id)
        except Transactions.DoesNotExist:
            return None

    def get(self, request, transaction_id):
        transaction = self.get_object(transaction_id)
        if transaction is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, transaction_id):
        transaction = self.get_object(transaction_id)
        if transaction is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, transaction_id):
        transaction = self.get_object(transaction_id)
        if transaction is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


