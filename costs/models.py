from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("costs:user_detail", kwargs={'pk': self.pk})


class Cost(models.Model):
    categories = [
        ("Одяг", "Одяг"),
        ("Подорож", "Подорож"),
        ("Техніка", "Техніка"),
        ("Продукти", "Продукти"),
        ("Усе для тварин", "Усе для тварин"),
        ("Усе для саду", "Усе для саду"),
        ("Таксі", "Таксі"),
        ("Розваги", "Розваги"),
    ]
    data = models.DateField("Рік/місяць/день")
    category = models.CharField("Категорія", max_length=100, choices=categories)
    price = models.DecimalField("Вартість витрати", max_digits=50, decimal_places=2)
    user = models.ManyToManyField(CustomUser, related_name="users")

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return f"{self.data} {self.category} {self.price}"
