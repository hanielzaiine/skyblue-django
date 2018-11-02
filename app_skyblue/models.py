from django.db import models

# Create your models here.
class Condominio(models.Model):
    class Meta:
        verbose_name = 'Condomínio'
        verbose_name_plural = 'Condomínios'
    nome = models.CharField('Nome', max_length=64)
    endereço = models.CharField('Endereço', max_length=128)
    taxa = models.DecimalField(max_digits=5,decimal_places=2)
    telefone = models.CharField('Telefone', max_length=15)
    def __str__(self):
        return self.nome

class DocumentoInstitucional(models.Model):
    class Meta:
        verbose_name = 'Documento Institucional'
        verbose_name_plural = 'Documentos Institucionais'
    nome = models.CharField('Nome', max_length=64)
    data_cadastro = models.DateField('Data Documento')
    autor = models.CharField('Autor', max_length=128)
    status = models.BooleanField('Status')
    condominio = models.ForeignKey(Condominio,NULL=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.nome