FROM nginx:stable-alpine

COPY templates.json /usr/share/nginx/html/templates.json

EXPOSE 80
