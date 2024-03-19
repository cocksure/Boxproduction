from django.core.validators import FileExtensionValidator, MinValueValidator
from django.db import models

from apps.info.models import Material
from apps.shared.models import BaseModel
from apps.users.models import CustomUser


class Process(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class UploadImage(models.Model):
    photo = models.ImageField(
        upload_to='box_photos/',
        default='no-image.png',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic'])]
    )


class BoxModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    type_of_work = models.ManyToManyField(Process, related_name='processes')
    photos = models.ForeignKey(
        UploadImage,
        on_delete=models.CASCADE,
        related_name='box_model',
        blank=True,
        null=True
    )



class BoxOrder(BaseModel):
	class BoxOrderStatus(models.TextChoices):
		ACCEPT = 'Одобрено', 'Одобрено'
		REJECT = 'Отклонено', 'Отклонено'

	data = models.DateField(editable=True, null=True, blank=True)
	customer = models.CharField(max_length=100)
	status = models.CharField(choices=BoxOrderStatus.choices, default=None, null=True, blank=True, max_length=150)
	type_order = models.CharField(max_length=100)
	specification = models.CharField(max_length=100)
	manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	date_of_production = models.DateField(editable=True)

	def confirm(self):
		if self.status is None:
			self.status = BoxOrder.BoxOrderStatus.ACCEPT
			self.save()

	def reject(self):
		if self.status is None:
			self.status = BoxOrder.BoxOrderStatus.REJECT
			self.save()

	def __str__(self):
		return f"Order - {self.id}"


class BoxOrderDetail(models.Model):
	box_order = models.ForeignKey(BoxOrder, on_delete=models.CASCADE)
	box_model = models.ForeignKey(BoxModel, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

	def __str__(self):
		return f"{self.box_order} - {self.box_model}"


class ProductionOrder(models.Model):
	box_order_detail = models.ForeignKey(
		BoxOrderDetail,
		on_delete=models.CASCADE,
		related_name='production_orders',
		blank=True,
		null=True
	)
	shipping_date = models.DateField()
	amount = models.DecimalField(max_digits=10, decimal_places=2)

	status_choices = (
		('in_progress', 'In Progress'),
		('completed', 'Completed'),
		('not_started', 'Not Started'),
	)
	status = models.CharField(max_length=20, choices=status_choices, default='not_started')