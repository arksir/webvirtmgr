FROM ubuntu:14.04

RUN apt-get -y update && \
    apt-get -y install python-pip python-libvirt python-libxml2 supervisor novnc && \
    sed -i 's#GSSAPIAuthentication yes#GSSAPIAuthentication no#' /etc/ssh/ssh_config && \
    sed -i 's/#   StrictHostKeyChecking ask/    StrictHostKeyChecking no/' /etc/ssh/ssh_config && \
    mkdir -p /data/vm/ && \
    useradd webvirtmgr -g libvirtd -u 1010 -m -d /data/vm/ -s /bin/bash && \
    chown -R webvirtmgr:libvirtd /data/vm/

COPY --chown=webvirtmgr:libvirtd ./ /webvirtmgr
COPY conf/conf.d/webvirtmgr.conf /etc/supervisor/conf.d/webvirtmgr.conf

RUN pip install -r /webvirtmgr/requirements.txt && \
    apt-get -ys clean

WORKDIR /webvirtmgr
VOLUME /data/vm

EXPOSE 8080
EXPOSE 6080
CMD ["supervisord", "-n"]
