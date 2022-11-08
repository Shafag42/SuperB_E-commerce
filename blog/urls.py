from django.urls import path, include
from .views import PostListView, PostDetail


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('blog/', PostListView.as_view(), name='blog'),
    path('blog_detail/<slug:slug>/', PostDetail.as_view(), name='blog_detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]

