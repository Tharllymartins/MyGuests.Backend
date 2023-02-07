from django.db import models


class Guest(models.Model):
    
    full_name = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )
    
    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )
    
    birthday_date = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False
    )
    
    house_number = models.PositiveSmallIntegerField(
        verbose_name="Número da casa a ser visitada"
    )
    
    license_plate = models.CharField(
        verbose_name="Placa do veiculo",
        max_length=7,
        blank=True,
        null=True
    )
    
    arrival_time = models.DateTimeField(
        verbose_name="Horário de chegada na portarioa",
        auto_now_add=True
    )
    
    departure_time = models.DateTimeField(
        verbose_name="Horário de saida do condominio",
        auto_now=False,
        blank=True,
        null=True
    )
    
    authorization_time = models.DateTimeField(
        verbose_name="Horário da autorização da entrada",
        auto_now=False,
        blank=True,
        null=True
    )
    
    responsible_resident = models.CharField(
        verbose_name="Nome do morador responsável",
        max_length=194,
        blank=True
    )

    register_by = models.ForeignKey(
        "doorman.Doorman",
        verbose_name="Porteiro responsável pelo registro",
        on_delete=models.PROTECT
    )
    
    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "guest"
        
        
    def __str__(self) -> str:
        return self.full_name