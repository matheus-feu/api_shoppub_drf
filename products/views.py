from django.utils import timezone
from rest_framework import generics, status
from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    """
    ViewSet para listar todos os produtos ativos.
    """
    queryset = Product.objects.filter(deleted_at=None, is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDetailView(generics.RetrieveAPIView,
                        generics.UpdateAPIView,
                        generics.DestroyAPIView):
    """
    ViewSet para visualizar detalhes de um produto existente.
    """
    queryset = Product.objects.filter(deleted_at=None)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductCreateView(generics.CreateAPIView):
    """
    View para criar um novo produto.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateView(generics.UpdateAPIView,
                        generics.RetrieveAPIView):
    """
    View para atualizar um produto existente.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        """
        Retorna o produto a ser atualizado.
        """
        return Product.objects.filter(id=self.kwargs['pk'], deleted_at=None)


class ProductReactivateView(views.APIView):
    """
    View para reativar um produto inativo.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Reativa um produto inativo.
        """
        product = Product.objects.filter(id=self.kwargs['pk'], is_active=False, deleted_at=None).first()
        if product is None:
            return Response(data={"detail": "Product not found, or is already active."},
                            status=status.HTTP_404_NOT_FOUND)
        elif product.is_active:
            return Response(data={"detail": "Product is already active."}, status=status.HTTP_400_BAD_REQUEST)

        product.deleted_at = None
        product.is_active = True
        product.save()
        return Response(data={"detail": "Product successfully reactivated."}, status=status.HTTP_200_OK)


class ProductDeleteView(generics.DestroyAPIView,
                        generics.RetrieveAPIView):
    """
    View para excluir um produto existente.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        """
        Retorna o produto a ser excluído.
        """
        return Product.objects.filter(id=self.kwargs['pk'], deleted_at=None)

    def destroy(self, request, *args, **kwargs):
        """
        Sobrescreve o método destroy padrão para implementar a exclusão lógica.
        Em vez de excluir o registro do banco de dados, define o campo deleted_at para a hora atual da exclusão.

        Verifica se o produto está inativo e, se estiver, solicita confirmação para excluir.
        Se confirmado, define o campo deleted_at para a hora atual da exclusão.
        """
        instance = self.get_object()
        if instance.deleted_at is not None:
            return Response(data={"detail": "Product has been previously deleted."}, status=status.HTTP_204_NO_CONTENT)

        if not instance.is_active:
            confirm_delete = request.query_params.get('confirm_delete', 'false').lower() == 'true'
            if not confirm_delete:
                return Response(data={
                    "message": "Product is already inactive. Please confirm to delete by passing 'confirm_delete=true' in the query parameters."
                }, status=status.HTTP_400_BAD_REQUEST)

        instance.deleted_at = timezone.now()
        instance.is_active = False
        instance.save()
        return Response(data={"detail": "Product successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
