# Usar imagem menor e mais segura (evitar ubuntu:latest)
FROM ubuntu:22.04

# Criação de um usuário sem privilégios (evitar root)
RUN useradd -ms /bin/bash appuser

# Atualização e instalação com limpeza para evitar cache de pacotes
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Mudar o usuário padrão para o não-root
USER appuser

# Definir comando padrão
CMD ["bash"]

# Adicionar verificação de saúde (healthcheck)
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:80 || exit 1

