from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    # Замінюємо надписи в адмінці [
    def __str__(self):
        try:
            return self.name
        except:
            return '%s' % self.id


    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'
    # Замінюємо надписи в адмінці ]