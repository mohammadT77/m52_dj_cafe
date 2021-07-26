from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _, get_language

from core.models import BaseModel


class MenuItem(BaseModel):
    name = models.CharField(verbose_name=_("Name"), max_length=100,
                            help_text=_("Name of the item"))
    price = models.PositiveIntegerField(_('Price (Tooman)'),
                                        help_text=_("Price in Tooman"))
    discount = models.PositiveIntegerField(_('Discount (%)'),
                                   null=True, blank=True, help_text=_("Discount in %"))
    category = models.CharField(max_length=100)
    image = models.FileField(_('Image'), upload_to='menu_item/',
                             null=True, default=None, blank=True)

    def final_price(self):
        disc = self.discount or 0
        discounted_price = self.price * disc / 100
        return max(0.0, self.price - discounted_price)


