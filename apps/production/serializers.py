from rest_framework import serializers
from .models import Process, BoxModel, BoxOrder, BoxOrderDetail, ProductionOrder


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'


class BoxModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxModel
        fields = '__all__'


class BoxOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxOrderDetail
        fields = ['box_model', 'amount']


class BoxOrderSerializer(serializers.ModelSerializer):
    order_detail = BoxOrderDetailSerializer(many=True, source='boxorderdetail_set')

    class Meta:
        model = BoxOrder
        fields = ['data', 'customer', 'status', 'type_order', 'specification', 'manager',
                  'date_of_production', 'order_detail']

    def create(self, validated_data):
        order_detail_data = validated_data.pop('boxorderdetail_set')
        box_order = BoxOrder.objects.create(**validated_data)
        for detail_data in order_detail_data:
            BoxOrderDetail.objects.create(box_order=box_order, **detail_data)
        return box_order


class ProductionOrderSerializer(serializers.ModelSerializer):
    box_order_detail = BoxOrderDetailSerializer(many=True, read_only=True)
    class Meta:
        model = ProductionOrder
        fields = ['box_order_detail', 'shipping_date', 'amount']
