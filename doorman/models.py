from django.db import models


class Doorman(models.Model):
    
    user = models.OneToOneField(
        "users.User",
        verbose_name="Usuário",
        on_delete=models.PROTECT
    )
    
    full_name = models.CharField(
        verbose_name="Nome completo",
        max_length=194,
    )
    
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )
    
    phone =models.CharField(
        verbose_name="Telefone para contato",
        max_length=11
    )
    
    birthday_date = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False
    )
    
    class Meta:
        verbose_name = "Porteiro",
        verbose_name_plural = "Porteiros"
        db_table = "doorman"
        
    def __str__(self) -> str:
        return self.full_name
