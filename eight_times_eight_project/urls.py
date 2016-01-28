from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', 'eight_times_eight_project.core.views.home', name='home'),
    url(r'^signin', 'django.contrib.auth.views.login', {'template_name': 'core/cover.html'}, name='signin'),
    url(r'^signout', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='signout'),
    url(r'^signup/$', 'eight_times_eight_project.auth_new.views.signup', name='signup'),
    url(r'^me/$', 'eight_times_eight_project.core.views.me', name='me'),
    url(r'^me/update_profile/$', 'eight_times_eight_project.core.views.update_profile', name='update_profile'),
    url(r'^me/picture/$', 'eight_times_eight_project.core.views.picture', name='picture'),
    url(r'^me/upload_picture/$', 'eight_times_eight_project.core.views.upload_picture', name='upload_picture'),
    url(r'^me/save_uploaded_picture/$', 'eight_times_eight_project.core.views.save_uploaded_picture', name='save_uploaded_picture'),
    url(r'^me/update_password/$', 'eight_times_eight_project.core.views.update_password', name='update_password'),
    url(r'^friends/', 'eight_times_eight_project.core.views.friends', name='friends'),
    url(r'^friends/add_friend/$', 'eight_times_eight_project.core.views.add_friend', name='add_friend'),
    url(r'^friends/confirm_friend/$', 'eight_times_eight_project.core.views.confirm_friend', name='confirm_friend'),
    url(r'^friends/remove_friend/$', 'eight_times_eight_project.core.views.remove_friend', name='remove_friend'),
    url(r'^friends/decline_friend/$', 'eight_times_eight_project.core.views.decline_friend', name='decline_friend'),
    url(r'^network/$', 'eight_times_eight_project.core.views.network', name='network'),
    url(r'^square/', include('eight_times_eight_project.feeds.urls'), name='square'),
    url(r'^messages/', include('eight_times_eight_project.messages_new.urls')),
    url(r'^notifications/$', 'eight_times_eight_project.activities.views.notifications', name='notifications'),
    url(r'^notifications/last/$', 'eight_times_eight_project.activities.views.last_notifications', name='last_notifications'),
    url(r'^notifications/check/$', 'eight_times_eight_project.activities.views.check_notifications', name='check_notifications'),
    url(r'^search/$', 'eight_times_eight_project.search.views.search', name='search'),
    url(r'^user/(?P<id>[^/]+)/$', 'eight_times_eight_project.core.views.profile', name='profile'),
    url(r'^vote/$', 'eight_times_eight_project.core.views.vote', name='vote'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
