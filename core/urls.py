from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/v1/', include('djoser.urls')),
                  path('api/v1/', include('djoser.urls.authtoken')),
                  path('api/v1/product/', include('api_products.urls')),
                  path('api/v1/category/', include('api_categories.urls')),
                  path('api/v1/account/', include('api_accounts.urls')),
                  path('api/v1/order/', include('api_orders.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
