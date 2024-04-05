FROM cgr.dev/chainguard/wolfi-base

ENV PYTHON_VERSION=3.12 \
    APP_USER=nonroot \
	PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1

RUN set -eux ;\
    apk update ;\
    apk upgrade ;\
    apk add python-${PYTHON_VERSION} ;

USER ${APP_USER}
WORKDIR /home/${APP_USER}
COPY --chown=${APP_USER}:${APP_USER} --chmod=775 tests /home/${APP_USER}/tests
COPY --chown=${APP_USER}:${APP_USER} --chmod=775 script/run_test.sh /home/${APP_USER}/run_test.sh

RUN set -eux; \
    chmod +x /home/${APP_USER}/run_test.sh ;

ENTRYPOINT ["sh", "-c", "./run_test.sh"]
