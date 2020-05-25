FROM primiano/docker-webvirtmgr:latest
RUN sed -i 's#GSSAPIAuthentication yes#GSSAPIAuthentication no#' /etc/ssh/ssh_config && \
    sed -i 's/#   StrictHostKeyChecking ask/    StrictHostKeyChecking no/' /etc/ssh/ssh_config && \
    sed -i 's#webvirtmgr:x:1010:108::/data/vm/:/sbin/nologin#webvirtmgr:x:1010:108::/data/vm/:/bin/bash#g' /etc/passwd && \
    rm -fr /webvirtmgr && \
    chown -R 1010:108 /data/vm

COPY --chown=1010:108 ./ /webvirtmgr
COPY conf/conf.d/webvirtmgr.conf /etc/supervisor/conf.d/webvirtmgr.conf

RUN pip install -r /webvirtmgr/requirements.txt

WORKDIR /webvirtmgr
VOLUME /data/vm

EXPOSE 8080
EXPOSE 6080
CMD ["supervisord", "-n"]
