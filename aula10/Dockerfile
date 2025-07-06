# Etapa de build
FROM alpine:3.20 as builder
RUN cat << 'EOF' > /app.sh && chmod +x /app.sh
#!/bin/sh
echo "App executando com segurança!"
EOF

# Imagem final (sem hardening)
FROM alpine:3.20
COPY --from=builder /app.sh /usr/local/bin/app.sh
ENTRYPOINT ["/usr/local/bin/app.sh"]
