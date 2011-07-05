from django.conf.urls.defaults import *

from contact_form.forms import ContactForm

urlpatterns = patterns('www.views',
    url(r'^$', 'index', name="www_index"),
    url(r'^contact-us/$', 'contact_form', name='www_contact_form'),
)

# This is for layout-demonstration purposes. After you saw it, you can delete and implement urls in a proper manner.
urlpatterns += patterns('django.views.generic.simple',
    url(r'^obesity/$', 'direct_to_template', {'template': 'www/obesity.html'}, name="www_obesity"),
    url(r'^team/$', 'direct_to_template', {'template': 'www/team.html'}, name="www_team"),
    url(r'^photogallery/$', 'direct_to_template', {'template' : 'www/photogallery.html'}, name="www_photogallery"),
    url(r'^photogallery/capella$', 'direct_to_template', {'template' : 'www/capella.html'}, name="www_capella"),
    url(r'^photogallery/sleeve/$', 'direct_to_template', {'template' : 'www/sleeve.html'}, name="www_sleeve"),
    url(r'^articles/$', 'direct_to_template', {'template' : 'www/articles.html'}, name="www_articles"),
    url(r'^articles/article1/$', 'direct_to_template', {'template' : 'www/article1.html'}, name="www_article1"),
    url(r'^articles/article2/$', 'direct_to_template', {'template' : 'www/article2.html'}, name="www_article2"),
    url(r'^articles/obesitysearch/$', 'direct_to_template', {'template' : 'www/obesity_search.html'}, name="www_obesitysearch"),
)

urlpatterns += patterns('www.views',
    url(r'^bmi/$', 'calculate_bmi', name="www_bmi"),
)

urlpatterns += patterns('ajax_validation.views',
    url(r'^form/contact/validate/$', 'validate', {'form_class': ContactForm, 'callback' : lambda request, *args, **kwargs: {'request' : request}}, 'contact_form_validate'),
)
