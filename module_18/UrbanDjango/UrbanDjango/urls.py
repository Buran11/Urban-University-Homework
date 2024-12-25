from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from task2.views import func_view, ClassView
from task3.views import cart, store, platform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', func_view),
    path('class/', ClassView.as_view()),
    path('platform/cart/', cart),
    path('platform/store/', store),
    path('platform/', platform),
]
