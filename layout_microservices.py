import os
import shutil

# Create directories
os.makedirs('src/services/auth', exist_ok=True)
os.makedirs('src/services/news', exist_ok=True)
os.makedirs('src/services/legal', exist_ok=True)
os.makedirs('src/services/consultations', exist_ok=True)
os.makedirs('gateway', exist_ok=True)

# Copy server.py to all services
shutil.copy('server.py', 'src/services/auth/main.py')
shutil.copy('server.py', 'src/services/news/main.py')
shutil.copy('server.py', 'src/services/legal/main.py')
shutil.copy('server.py', 'src/services/consultations/main.py')

# Create gateway.conf
gateway_conf = """server {
    listen 8000;

    location ~ ^/api/(auth|users|favorites|bugs|admin/users|admin/bugs) {
        proxy_pass http://bionews-auth-service:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location ~ ^/api/news {
        proxy_pass http://bionews-news-service:8002;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location ~ ^/api/(data|options|admin/debug/delete-latest|search) {
        proxy_pass http://bionews-legal-service:8003;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location ~ ^/api/(consultas|minsal) {
        proxy_pass http://bionews-consultations-service:8004;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
"""

with open('gateway/gateway.conf', 'w', encoding='utf-8') as f:
    f.write(gateway_conf)

print("Microservices layout created successfully!")
