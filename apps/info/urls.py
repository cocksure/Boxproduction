from django.urls import path
from . import views

urlpatterns = [
	# list
	path('warehouses/', views.WarehouseListView.as_view(), name='warehouse-list'),
	path('materials/', views.MaterialListView.as_view(), name='material-list'),
	path('material-types/', views.MaterialTypeListView.as_view(), name='material-type-list'),
	path('box-sizes/', views.BoxSizeListView.as_view(), name='box-size-list'),
	path('material-groups/', views.MaterialGroupListView.as_view(), name='material-group-list'),
	path('firms/', views.FirmListView.as_view(), name='firm-list'),
	path('material-special-groups/', views.MaterialSpecialGroupListView.as_view(), name='material-special-group-list'),
	path('brands/', views.BrandListView.as_view(), name='brand-list'),
	path('specifications/', views.SpecificationListView.as_view(), name='specification-list'),
	path('box-types/', views.BoxTypeListView.as_view(), name='box-type-list'),

	# create
	path('create/warehouse/', views.CreateWarehouseView.as_view(), name='create-warehouse'),
	path('create/brand/', views.CreateBrandView.as_view(), name='create-brand'),
	path('create/material-type/', views.CreateMaterialTypeView.as_view(), name='create-material-type'),
	path('create/material-group/', views.CreateMaterialGroupView.as_view(), name='create-material-group'),
	path('create/material-special-group/', views.CreateMaterialSpecialGroupView.as_view(),
		 name='create-material-special-group'),
	path('create/material/', views.CreateMaterialView.as_view(), name='create-material'),
	path('create/box-size/', views.CreateBoxSizeView.as_view(), name='create-box-size'),
	path('create/firm/', views.CreateFirmView.as_view(), name='create-firm'),
	path('create/specification/', views.CreateSpecificationView.as_view(), name='create-specification'),
	path('create/box-type/', views.CreateBoxTypeView.as_view(), name='create-box-type'),
]

