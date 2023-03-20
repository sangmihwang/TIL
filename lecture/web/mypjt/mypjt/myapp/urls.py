
from django.urls import path
from . import views



# path('admin/', admin.site.urls),
# path('myapps/', include('myapps.urls')),
# path('home/', myapp_views.index),
# path('hello/', articles_views.hello)




urlpatterns = [
    path('', views.index),
    path('<int:number>/', views.detail),
    path('calc/<int:num1>/<int:num2>/', views.calc),
]
