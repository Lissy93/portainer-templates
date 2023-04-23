FROM nginx:stable-alpine

COPY templates.json /usr/share/nginx/html/templates.json
COPY index.html /usr/share/nginx/html/index.html

EXPOSE 80
