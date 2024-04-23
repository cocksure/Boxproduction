from rest_framework import serializers
from apps.info import models
from apps.shared.serializers import BaseNameCodeSerializer


class WarehouseSerializer(BaseNameCodeSerializer):
	class Meta:
		model = models.Warehouse
		fields = '__all__'

	def validate(self, data):
		if not data.get('is_active'):
			raise serializers.ValidationError("Склад неактивен.")
		if not data.get('can_import'):
			raise serializers.ValidationError("Склад не может импортировать!")
		if not data.get('can_export'):
			raise serializers.ValidationError("Warehouse cannot export products.")
		if data.get('use_negative') and data.get('available_quantity') < 0:
			raise serializers.ValidationError("На складе отрицательный запас.")
		return data


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Brand
		fields = '__all__'


class MaterialTypeSerializer(BaseNameCodeSerializer):
	class Meta:
		model = models.MaterialType
		fields = ('id', 'name')


class MaterialGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MaterialGroup
		fields = '__all__'


class MaterialSpecialGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MaterialSpecialGroup
		fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
	material_group = MaterialGroupSerializer()
	special_group = MaterialSpecialGroupSerializer()
	brand = BrandSerializer()
	material_type = MaterialTypeSerializer()

	class Meta:
		model = models.Material
		fields = (
			'id', 'code', 'name', 'material_group', 'special_group', 'brand',
			'material_type', 'material_thickness', 'unit_of_measurement',
			'created_time', 'updated_time', 'created_by', 'updated_by'
		)


class BoxSizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BoxSize
		fields = ('name',)


class FirmSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Firm
		fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Specification
		fields = '__all__'


class BoxTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BoxType
		fields = '__all__'
