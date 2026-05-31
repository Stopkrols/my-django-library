from django.db import models

class Well(models.Model):
    well_number = models.IntegerField(verbose_name="Номер свердловини")
    area = models.CharField(max_length=100, verbose_name="Площа")

    class Meta:
        verbose_name = "Свердловина"
        verbose_name_plural = "Свердловини"
        ordering = ['well_number']

    def __str__(self):
        return f"Свердловина {self.well_number} ({self.area})"

class RockSample(models.Model):
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name="Свердловина")
    sample_id = models.CharField(max_length=50, verbose_name="Зразок №")
    rock_type = models.CharField(max_length=50, verbose_name="Порода")
    mag_susceptibility = models.FloatField(verbose_name="Магнітна сприйнятливість")
    depth = models.FloatField(null=True, blank=True, verbose_name="Інтервал (глибина)")

    class Meta:
        verbose_name = "Зразок породи"
        verbose_name_plural = "Зразки порід"

    def __str__(self):
        return f"Зразок {self.sample_id} ({self.rock_type})"