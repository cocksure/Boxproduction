from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from . import serializers
from . import models
from ..shared.utils import CustomPagination
from ..shared.views import BaseListView


class WarehouseListView(BaseListView):
	queryset = models.Warehouse.objects.all()
	serializer_class = serializers.WarehouseSerializer
	filterset_fields = ['is_active', ]
	search_fields = ['id', 'code', 'name']


class MaterialListView(BaseListView):
	queryset = models.Material.objects.all()
	serializer_class = serializers.MaterialSerializer
	filterset_fields = ['material_group', 'special_group', 'material_type']
	search_fields = ['code', 'name']


class MaterialTypeListView(ListAPIView):
	queryset = models.MaterialType.objects.all()
	serializer_class = serializers.MaterialTypeSerializer


class BoxSizeListView(ListAPIView):
	queryset = models.BoxSize.objects.all()
	serializer_class = serializers.BoxSizeSerializer


class MaterialGroupListView(ListAPIView):
	queryset = models.MaterialGroup.objects.all()
	serializer_class = serializers.MaterialGroupSerializer
	pagination_class = CustomPagination


class FirmListView(ListAPIView):
	queryset = models.Firm.objects.all()
	serializer_class = serializers.FirmSerializer
	pagination_class = CustomPagination
	filterset_fields = ['type_firm']
	search_fields = ['id', 'code', 'name', 'mfo']


class MaterialSpecialGroupListView(ListAPIView):
	queryset = models.MaterialSpecialGroup.objects.all()
	serializer_class = serializers.MaterialSpecialGroupSerializer
	pagination_class = CustomPagination


class BrandListView(ListAPIView):
	queryset = models.Brand.objects.all()
	serializer_class = serializers.BrandSerializer
	pagination_class = CustomPagination


class SpecificationListView(ListAPIView):
	queryset = models.Specification.objects.all()
	serializer_class = serializers.SpecificationSerializer
	pagination_class = CustomPagination


class BoxTypeListView(ListAPIView):
	queryset = models.BoxType.objects.all()
	serializer_class = serializers.BoxTypeSerializer
	pagination_class = CustomPagination


class CreateWarehouseView(CreateAPIView):
	serializer_class = serializers.WarehouseSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBrandView(CreateAPIView):
	serializer_class = serializers.BrandSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateMaterialTypeView(CreateAPIView):
	serializer_class = serializers.MaterialTypeSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateMaterialGroupView(CreateAPIView):
	serializer_class = serializers.MaterialGroupSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateMaterialSpecialGroupView(CreateAPIView):
	serializer_class = serializers.MaterialSpecialGroupSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateMaterialView(CreateAPIView):
	serializer_class = serializers.MaterialSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBoxSizeView(CreateAPIView):
	serializer_class = serializers.BoxSizeSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateFirmView(CreateAPIView):
	serializer_class = serializers.FirmSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateSpecificationView(CreateAPIView):
	serializer_class = serializers.SpecificationSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateBoxTypeView(CreateAPIView):
	serializer_class = serializers.BoxTypeSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		self.perform_create(serializer)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
