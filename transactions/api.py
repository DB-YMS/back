#    from rest_framework.views import APIView
#    from rest_framework.response import Response
#    from .serializers import *
#    from rest_framework import status
#
#    class TransactionList(APIView):
#        def get(self, request):
#            model = Transaction.objects.all()
#            serializer = TransactionSerializer(model, many=True)
#            return Response(serializer.data)
#
#        def post(self, request):
#            serializer = TransactionSerializer(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data, status = status.HTTP_201_CREATED)
#            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
#
#    class TransactionDetail(APIView):
#        def get(self, request, transactions_id):
#            model = Transaction.objects.get(transactions_id = transactions_id)
#            serializer = TransactionSerializer(model)
#            return Response(serializer.data)
#
#        def put(self, request, transactions_id):
#            model = Transaction.objects.get(transactions_id=transactions_id)
#            serializer = TransactionSerializer(data=request.data)
#            if serializer.is_valid():
#                serializer.save()
#                return Response(serializer.data, status = status.HTTP_201_CREATED)
#            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#
#        def delete(self, request, transactions_id):
#            model = Transaction.objects.get(transactions_id=transactions_id)
#            model.delete()
#            return Response(status=status.HTTP_204_NO_CONTENT)