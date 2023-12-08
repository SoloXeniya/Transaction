
from django.contrib import admin
from django.urls import path, include
from main.views import ProfileViewSet, TransactionViewSet, UserViewSet, AddBalanceViewSet
from rest_framework import routers, permissions
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="API Transaction",
        default_version='v1',
        description="Эта API создана для просматривания транзакций",
        terms_of_service="http://itcbootcamp.com",
        contact=openapi.Contact(
            name = "Xeniya",
            url = "https://t.me/Xeniyakot",
            email="xeniasolovyovakot@yandex.kz",
            ),
        license=openapi.License(
            name="BSD License"
            ),
    ),    
    public = True,
    permission_classes = [
        permissions.IsAdminUser,]    
    
)


router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'user', UserViewSet)
router.register(r'addbalance', AddBalanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', include('django.contrib.admindocs.urls')), 
    path('api/', include(router.urls)),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
