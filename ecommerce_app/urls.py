from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('contact/',views.contact,name="contact"),
    path('cart/',views.cart,name="cart"),
    path('detail/<int:id>',views.detail,name="detail"),
    path('checkout/',views.checkout,name="checkout"),
    path('shop/',views.shop_view,name="shop"),
    path('accounts/login/',views.sign_in,name="login"),
    path('accounts/create/',views.sign_up,name="create"),
    path('logout/',views.logout_u,name="logout"),
    path('add_cart/<int:id1>/<int:id2>',views.add_cart,name="add_cart"),
    path('remove_cart/<id1>/<int:id2>/<str:size>/<str:colour>',views.remove_cart,name="remove_cart"),
    path('update_cart/<id1>/<int:id2>/<str:size>/<str:colour>',views.update_cart,name="update_cart"),
    path('category/<int:id>',views.category_view,name="category"),
    path('billing/<int:id>',views.billing,name="billing"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)