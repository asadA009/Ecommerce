from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name="shop"),
   path("about/",views.about,name="aboutUs"),
   path("contact/",views.contact,name="contactus"),
   path("tracker/",views.tracker,name="trackeing"),
   path("search/",views.search,name="search"),
   path("productview/",views.productview,name="ProductView"),
   path("checkout/",views.checkout,name="checkout"),
]