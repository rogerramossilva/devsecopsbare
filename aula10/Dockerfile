# Etapa de build
FROM alpine:3.20 as builder
RUN echo '#!/bin/sh\n echo "App executando com segurança!"' > /app.sh && chmod +x /app.sh

# Imagem final (sem hardening)
FROM alpine:3.20
COPY --from=builder /app.sh /usr/local/bin/app.sh
ENTRYPOINT ["/usr/local/bin/app.sh"]
