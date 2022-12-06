from django.db import models


class Card(models.Model):
    CARD_STATUSES = [
        ('Not activated', 'не активирована'),
        ('Activated', 'активирована'),
        ('Overdue', 'просрочена')
    ]

    series = models.PositiveIntegerField(
        verbose_name='Серия',
        help_text='Введите серию карты',
    )
    number = models.PositiveIntegerField(
        verbose_name='Номер',
        help_text='Введите номер карты'
    )
    release_date = models.DateTimeField(
        verbose_name='Дата выпуска',
        auto_now_add=True
    )
    activity_end_date = models.DateTimeField(
        verbose_name='Дата окончания активности',
    )
    date_of_use = models.DateTimeField(
        verbose_name='Дата использования',
        auto_now_add=True
    )
    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits=11,
        decimal_places=2,
        default=0.00
    )
    status = models.CharField(
        verbose_name='Статус',
        choices=CARD_STATUSES,
        max_length=50,
        default='Not activated'
    )

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'
        ordering = ['-release_date']

    def __str__(self):
        return f'Card #{self.pk}'


class ShoppingHistory(models.Model):
    card = models.ForeignKey(
        verbose_name='Карта',
        to=Card,
        on_delete=models.CASCADE,
        related_name='history'
    )
    amount = models.DecimalField(
        verbose_name='Сумма',
        max_digits=11,
        decimal_places=2,
    )
    buying_date = models.DateTimeField(
        verbose_name='Дата покупки',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'История покупок карты'
        verbose_name_plural = 'История покупок карт'
        ordering = ['-buying_date']

    def __str__(self):
        return f'{self.card} history: {self.buying_date}'
