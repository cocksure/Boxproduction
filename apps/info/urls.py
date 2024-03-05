

from rest_framework import routers

from apps.info.views import WarehouseViewSetView, MaterialViewSetView, MaterialTypeViewSetView

app_name = 'info'
router = routers.DefaultRouter()

router.register(r'material/type', MaterialTypeViewSetView)
router.register(r'material', MaterialViewSetView)

router.register(r'warehouse', WarehouseViewSetView)

urlpatterns = []

urlpatterns += router.urls
