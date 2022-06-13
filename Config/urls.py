from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from News.views import NewsAPIViewSet, CommentAPIViewSet, CategoryAPIViewSet
from . import settings
from .swagger import swagger_urls

router = DefaultRouter()
router.register('news', NewsAPIViewSet)
router.register('comment', CommentAPIViewSet)
router.register('category', CategoryAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += swagger_urls
