from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """
        Sobrescreve o método delete padrão para implementar a exclusão lógica.
        Em vez de excluir o registro do banco de dados, define o campo deleted_at para a hora atual da exclusão.
        """
        self.deleted_at = timezone.now()
        self.save()


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        ordering = ['name']
