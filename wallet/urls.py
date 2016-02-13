from django.conf.urls import patterns, include, url
import views
from rest_framework import routers
from wallet.apiresource import TransactionsResource


router = routers.DefaultRouter()
router.register(r'transactions',TransactionsResource)

urlpatterns = patterns('',
    url(r'^$', views.wallet, name='transactions'),
    url(r'^add-transaction',views.addtransaction, name='addtransaction'),
    url(r'^api',include(router.urls)),
)
