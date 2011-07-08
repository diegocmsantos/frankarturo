Alias /static/ "/var/www/frankarturo/static/"
<Directory "/var/www/frankarturo/static">
        Order allow,deny
        Options Indexes
        Allow from all
        IndexOptions FancyIndexing
</Directory>

Alias /media/ "/usr/lib/python2.5/site-packages/django/contrib/admin/media/"
<Directory "/usr/lib/python2.5/site-packages/django/contrib/admin/media">
        Order allow,deny
        Options Indexes
        Allow from all
        IndexOptions FancyIndexing
</Directory>


WSGIDaemonProcess frankarturo python-path=/var/envs/frankarturo/lib/python2.5/site-packages
WSGIProcessGroup frankarturo
WSGIScriptAlias / "/var/www/frankarturo/deploy/script.wsgi"
WSGIPassAuthorization On


<Directory "/var/www/frankarturo/deploy">
        Allow from all
</Directory>

ErrorLog /var/log/apache2/frankarturo_error.log
CustomLog /var/log/apache2/frankarturo_access.log combined
LogLevel warn

