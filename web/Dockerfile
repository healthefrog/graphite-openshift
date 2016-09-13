FROM ubuntu:16.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 graphite-web libapache2-mod-wsgi libnss-wrapper && \
    cp /usr/share/graphite-web/apache2-graphite.conf /etc/apache2/sites-available/graphite-web.conf && \
    chgrp -R root /run /var && chmod g+rwX -R /run /var && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ports.conf /etc/apache2/
ADD graphite-web.conf /etc/apache2/sites-available
ADD local_settings.py /etc/graphite/
ADD entry.sh /

RUN a2dissite 000-default && a2ensite graphite-web

ENTRYPOINT ["/entry.sh"]
CMD ["apache2", "-DFOREGROUND"]
