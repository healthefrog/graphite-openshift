FROM debian:jessie

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install graphite-carbon && \
    chgrp -R root /run /var && chmod -R g+rwX /run /var && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD carbon.conf /etc/carbon/

CMD ["carbon-cache", "--debug", "--config=/etc/carbon/carbon.conf", "start"]

EXPOSE 2003 2004 7002
