#!/bin/sh

export NSS_WRAPPER_PASSWD=/tmp/passwd.nss_wrapper
export NSS_WRAPPER_GROUP=/etc/group

cp /etc/passwd $NSS_WRAPPER_PASSWD
echo _graphite:x:$(id -u):0::/home:/bin/sh >> $NSS_WRAPPER_PASSWD

export LD_PRELOAD=/usr/lib/libnss_wrapper.so

if [ ! -f /var/lib/graphite/graphite.db ]; then
    graphite-manage syncdb --noinput
fi

. /etc/apache2/envvars

exec $@
