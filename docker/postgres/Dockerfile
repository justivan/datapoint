FROM postgis/postgis:15-3.4

COPY ./docker/postgres/maintenance /usr/local/bin/maintenance
COPY ./server.key /var/lib/postgresql/
COPY ./server.crt /var/lib/postgresql/

RUN chmod og-rwx /var/lib/postgresql/server.key \
    && chown -R postgres:postgres /var/lib/postgresql \
    && chmod +x /usr/local/bin/maintenance/* \
    && mv /usr/local/bin/maintenance/* /usr/local/bin \
    && rmdir /usr/local/bin/maintenance

RUN 

CMD ["postgres", "-c", "ssl=on", "-c", "ssl_cert_file=/var/lib/postgresql/server.crt", "-c", "ssl_key_file=/var/lib/postgresql/server.key"]