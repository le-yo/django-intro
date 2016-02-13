from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^$', views.wallet, name='transactions'),
    url(r'^add-transaction',views.addtransaction, name='addtransaction'),
)
