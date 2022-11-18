FROM python:3.8-alpine

LABEL org.opencontainers.image.authors="kyle@leblanc.sh"
LABEL version="0.7"
LABEL description="Flask Guestbook"

COPY * /app/
RUN pip3 install Flask
RUN apk --no-cache add curl
EXPOSE 8080

ENV COLOR=blue
ENV FONT=monospace
ENV ENV=Prod
ENV VER=0.7

HEALTHCHECK --interval=30s --timeout=30s --start-period=10s --retries=3 \
    CMD curl http://localhost:8080 || exit 1

RUN adduser -D flaskUser
USER flaskUser

CMD python /app/app.py