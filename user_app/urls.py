
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="loginUser"),
    path('logout/',views.logout,name="logout"),
    path('product/<int:product_id>/',views.product,name="product"),   
    path('category/<str:selCategory>/',views.getProductsCategory,name="category"),
    path('search/',views.search,name="search"),
    path('myProducts/',views.myProducts,name="myProducts"),
    path('myCart/',views.myCart,name="myCart"),
    path('savefav/<int:product_id>/',views.savefav,name="savefav"),
    path('removefav/<int:product_id>/',views.removefav,name="removefav"),
    path('give_review/<int:product_id>/',views.give_review,name="give_review"), 
    path('addToCart/<int:product_id>',views.addToCart,name="addToCart"),
    path('buyedProducts/',views.buyedProducts,name='buyedProducts'),
    path('checkout/<int:price>/',views.checkout,name='checkout'), 
    path('removeCart/<int:product_id>/',views.removeCart,name="removeCart"),
    path('checkout/<int:price>/paymenthandler/', views.paymenthandler, name='paymenthandler'),
]
