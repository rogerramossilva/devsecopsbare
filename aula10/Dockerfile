FROM debian:bullseye-slim AS builder
RUN echo '#!/bin/sh' > /app.sh && \
    echo 'echo "App executando com segurança!"' >> /app.sh && \
    chmod +x /app.sh

FROM debian:bullseye-slim
COPY --from=builder /app.sh /usr/local/bin/app.sh
ENTRYPOINT ["/usr/local/bin/app.sh"]
