from django.contrib import admin  # type: ignore
from django.urls import path  # type: ignore
from task2.views import func_view, ClassView
from task3.views import cart, store, platform
from task4.views import platform2, store2, cart2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', func_view),
    path('class/', ClassView.as_view()),
    path('platform/cart/', cart),
    path('platform/store/', store),
    path('platform/', platform),
    path('platform2/cart2/', cart2),
    path('platform2/store2/', store2),
    path('platform2/', platform2),
]
