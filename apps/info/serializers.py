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
	group_id = serializers.SerializerMethodField()
	group_name = serializers.SerializerMethodField()
	type_id = serializers.SerializerMethodField()
	type_name = serializers.SerializerMethodField()
	spec_group_id = serializers.SerializerMethodField()
	spec_name = serializers.SerializerMethodField()

	class Meta:
		model = models.Material
		fields = (
			'id', 'code', 'name', 'group_id', 'group_name',
			'type_id', 'type_name', 'material_thickness', 'unit_of_measurement',
			'created_time', 'updated_time', 'created_by', 'updated_by'
		)

	def get_group_id(self, obj):
		return obj.material_group.id if obj.material_group else None

	def get_group_name(self, obj):
		return obj.material_group.name if obj.material_group else None

	def get_type_id(self, obj):
		return obj.material_type.id if obj.material_type else None

	def get_type_name(self, obj):
		return obj.material_type.name if obj.material_type else None

	def get_spec_group_id(self, obj):
		return obj.special_group.id if obj.special_group else None

	def get_spec_name(self, obj):
		return obj.special_group.name if obj.special_group else None


class BoxSizeSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.BoxSize
		fields = '__all__'


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
