FROM nginx

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/

RUN rm /etc/nginx/conf.d/default.conf
COPY pandemonium-nginx.conf /etc/nginx/conf.d/

COPY ./static ./static