from rest_framework import routers

from .views import ProfileViewSet, TransactionViewSet, AddBalanceViewSet, UserViewSet


router = routers.DefaultRouter()
router.register('profiles/', ProfileViewSet, basename='profiles')
router.register('transactions/', TransactionViewSet, basename='transactions')
router.register('add-balance/', AddBalanceViewSet, basename='add-balance')
router.register('users/', UserViewSet, basename='users')

urlpatterns = router.urls

