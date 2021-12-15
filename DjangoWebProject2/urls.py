"""
Definition of urls for DjangoWebProject2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^links$', app.views.links, name='links'),
    url(r'^pool$', app.views.pool, name='pool'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^(?P<parameter>\d+)/$', app.views.blogpost, name='blogpost'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^vidiopost$', app.views.videopost, name='videopost'),
    url(r'^registration$', app.views.registration, name='registration'),
    
    url(r'^cart/', app.views.cart, name='cart'),
    url(r'^shop/', app.views.shop, name='shop'),
    url(r'^add-to-cart/', app.views.add_to_cart, name='add_to_cart'),
    url(r'^delete_item/(?P<item>[0-9]+)/', app.views.delete_item, name='delete_item'),
    url(r'^quantity_minus/', app.views.quantity_minus, name='quantity_minus'),
    url(r'^quantity_plus/', app.views.quantity_plus, name='quantity_plus'),
    url(r'^total_price/', app.views.total_price, name='total_price'),
    url(r'^deal_order/', app.views.deal_order, name='deal_order'),
    url(r'^delete_order/(?P<item>[0-9]+)/', app.views.delete_order, name='delete_order'),
    url(r'^delete_item_order/(?P<item>[0-9]+)/', app.views.delete_item_order, name='delete_item_order'),
    url(r'^quantity_minus_order/', app.views.quantity_minus_order, name='quantity_minus_order'),
    url(r'^quantity_plus_order/', app.views.quantity_plus_order, name='quantity_plus_order'),
    url(r'^total_price_order/(?P<order>[0-9]+)/', app.views.total_price_order, name='total_price_order'),
    url(r'^myOrders/', app.views.myOrders, name='myOrders'),
    url(r'^AllOrders/', app.views.AllOrders, name='AllOrders'),
    url(r'^orderDetails/(?P<order>[0-9]+)/', app.views.orderDetails, name='orderDetails'),
    url(r'^shop/(?P<parameter>\w+)/$', app.views.shop, name='shop'),
   
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Авторизация',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
