maru@maru:/opt/BioNews$ docker compose down --remove-orphans
[+] down 10/10
✔ Container bionews-scheduler Removed 10.2s
✔ Container bionews-redis Removed 0.3s
✔ Container bionews-web Removed 0.3s
✔ Container bionews-legal-service Removed 0.1s
✔ Container bionews-news-service Removed 0.1s
✔ Container bionews-consultations-service Removed 0.1s
✔ Container bionews-auth-service Removed 0.1s
✔ Container bionews-gateway Removed 0.3s
✔ Container bionews-postgres Removed 0.2s
✔ Network bionews_bionews-net Removed 0.1s
maru@maru:/opt/BioNews$ docker compose up -d --build
[+] Building 3.4s (42/42) FINISHED
=> [internal] load local bake definitions 0.0s
=> => reading from stdin 2.56kB 0.0s
=> [consultations-service internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 1.56kB 0.0s
=> [web internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 822B 0.0s
=> [web internal] load metadata for docker.io/library/nginx:alpine 0.0s
=> [web internal] load metadata for docker.io/library/node:20-alpine 0.9s
=> [auth-service internal] load metadata for docker.io/library/python:3.11-slim 1.1s
=> [web internal] load .dockerignore 0.0s
=> => transferring context: 97B 0.0s
=> [web builder 1/6] FROM docker.io/library/node:20-alpine@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293 0.0s
=> => resolve docker.io/library/node:20-alpine@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293 0.0s
=> [web internal] load build context 0.1s
=> => transferring context: 5.18kB 0.0s
=> [web stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:dc48b7a872a79fb541ba5081d320b11b549231bc63ba465a7495afaa7d2ebcb8 0.0s
=> => resolve docker.io/library/nginx:alpine@sha256:dc48b7a872a79fb541ba5081d320b11b549231bc63ba465a7495afaa7d2ebcb8 0.0s
=> CACHED [web builder 2/6] WORKDIR /app 0.0s
=> CACHED [web builder 3/6] COPY package.json package-lock.json ./ 0.0s
=> CACHED [web builder 4/6] RUN npm ci 0.0s
=> CACHED [web builder 5/6] COPY . . 0.0s
=> CACHED [web builder 6/6] RUN npm run build 0.0s
=> CACHED [web stage-1 2/3] COPY --from=builder /app/dist /usr/share/nginx/html 0.0s
=> CACHED [web stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf 0.0s
=> [web] exporting to image 0.1s
=> => exporting layers 0.0s
=> => exporting manifest sha256:0615af306fa7efdd7c4d926cd4ef123daa14ef1aaf27854297ee8a141681e965 0.0s
=> => exporting config sha256:ea92359b07d71ffff26bfdf9f9da6a0edb407716b4535b5a8aace3f00f7a8958 0.0s
=> => exporting attestation manifest sha256:e9a7098d39546755a219e76ea492446b2cb6b64604de84fb1700afcb4566f18b 0.0s
=> => exporting manifest list sha256:4c9096a5c0b327c3058639874d39b69df277e77fdc470f0b0383a7c4d5d97194 0.0s
=> => naming to docker.io/library/bionews-web:latest 0.0s
=> => unpacking to docker.io/library/bionews-web:latest 0.0s
=> [legal-service internal] load .dockerignore 0.0s
=> => transferring context: 456B 0.0s
=> [consultations-service internal] load build context 0.0s
=> => transferring context: 206.50kB 0.0s
=> [auth-service 1/11] FROM docker.io/library/python:3.11-slim@sha256:9a7765b36773a37061455b332f18e265e7f58f6fea9c419a550d2a8b0e9db834 0.0s
=> => resolve docker.io/library/python:3.11-slim@sha256:9a7765b36773a37061455b332f18e265e7f58f6fea9c419a550d2a8b0e9db834 0.0s
=> [web] resolving provenance for metadata file 0.0s
=> CACHED [auth-service 2/11] WORKDIR /app 0.0s
=> CACHED [auth-service 3/11] RUN apt-get update && apt-get install -y --no-install-recommends wget ca-certificates fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 0.0s
=> CACHED [auth-service 4/11] COPY requirements.docker.txt ./requirements.txt 0.0s
=> CACHED [auth-service 5/11] RUN pip install --no-cache-dir -r requirements.txt 0.0s
=> CACHED [auth-service 6/11] RUN playwright install chromium && playwright install-deps chromium 0.0s
=> CACHED [auth-service 7/11] COPY server.py . 0.0s
=> CACHED [auth-service 8/11] COPY scheduler.py . 0.0s
=> CACHED [auth-service 9/11] COPY startScraping.py . 0.0s
=> [auth-service 10/11] COPY src/ ./src/ 0.1s
=> [news-service 11/11] RUN mkdir -p /app/data /app/logs /app/uploads/bugs 0.4s
=> [legal-service] exporting to image 0.9s
=> => exporting layers 0.1s
=> => exporting manifest sha256:b7e368736de9a4f671c2b96ba5b7b88237c0c3de341e53013b7d1e8a8c671c8a 0.1s
=> => exporting config sha256:302983df56d39422bc68f59f55c969c26e3f133893ede5d84d8f28de1ba35608 0.1s
=> => exporting attestation manifest sha256:e04d2b807eeceb344aa19dd52b3055dcfdce86964dac7b0a5b5bc5a1eb1f7357 0.1s
=> => exporting manifest list sha256:34e4d55c0aa332d014b7d8902e0de764fa12ecde7f8aff408b9efaa3022273a6 0.1s
=> => naming to docker.io/library/bionews-legal-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-legal-service:latest 0.2s
=> [consultations-service] exporting to image 0.9s
=> => exporting layers 0.1s
=> => exporting manifest sha256:6b98070875b28b75358ca1595b56e6861e88b157a4fd30962c502ca3c4f33390 0.1s
=> => exporting config sha256:611267af8cc84d98d36a55f5dd910748819b1975e99bbd76d7d1e8d94ef12f69 0.1s
=> => exporting attestation manifest sha256:bf75d11272e5b28f6c7ecda33278ca225c697a08a2490c139d9bfb9b602296e6 0.1s
=> => exporting manifest list sha256:1396d04986d37279f9e4af8a87dc7a4e2591518a5031e0e5677cdecf3907d473 0.1s
=> => naming to docker.io/library/bionews-consultations-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-consultations-service:latest 0.2s
=> [scheduler] exporting to image 0.9s
=> => exporting layers 0.1s
=> => exporting manifest sha256:ddd2c13020e9b20e67a5a911f5ad87d8828ca3c531313efb98dabe741a5302d5 0.1s
=> => exporting config sha256:704d55dbdf177d196c76d5d1f14a7218077088d1d9de4ea3d3ba414238266a4d 0.1s
=> => exporting attestation manifest sha256:8c564dd6f11f6d5b942c07a8af40894b3beddbd3b28478127d1447e74e8f7c21 0.1s
=> => exporting manifest list sha256:77a7b448b6d83e168a2e73f7842ad4c1fed669e3f6f02866532447ab98f19dea 0.1s
=> => naming to docker.io/library/bionews-scheduler:latest 0.0s
=> => unpacking to docker.io/library/bionews-scheduler:latest 0.2s
=> [news-service] exporting to image 0.9s
=> => exporting layers 0.1s
=> => exporting manifest sha256:d596fdefaeb6086e09263748ca0d9df6af6573d7a57756fa780f0ca2dff3e705 0.1s
=> => exporting config sha256:4c6fafcbc213540480e0caba5f3d4ad1ac717953c04dee1f4a14cc59d9101ee3 0.1s
=> => exporting attestation manifest sha256:581860b77bd899118b752a1c4e84f69763d420e9aa824a3f4984b9e7cf4126fa 0.1s
=> => exporting manifest list sha256:ca7959d8b7093a134e82587553088213c9efa8cf7f95a56a73f036f24b2af5ea 0.1s
=> => naming to docker.io/library/bionews-news-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-news-service:latest 0.2s
=> [auth-service] exporting to image 0.9s
=> => exporting layers 0.1s
=> => exporting manifest sha256:cd83f7e2f3cd844fae4ab8b02924204932abcd5e2edf2141a7ba8a2c7d1c0d96 0.1s
=> => exporting config sha256:db091631585dc66bbceda74aa764a80f322ec0ec1b3edffbf04334532867325e 0.1s
=> => exporting attestation manifest sha256:d6b9b49f78213dd49cb5e2a8e79dde94d56862115f3faf214d675892df4639dd 0.1s
=> => exporting manifest list sha256:e1422000bf1b646230154c13c67d82c2029faba06a6958c3cf335f401da6b423 0.1s
=> => naming to docker.io/library/bionews-auth-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-auth-service:latest 0.2s
=> [legal-service] resolving provenance for metadata file 0.3s
=> [news-service] resolving provenance for metadata file 0.2s
=> [auth-service] resolving provenance for metadata file 0.1s
=> [scheduler] resolving provenance for metadata file 0.0s
=> [consultations-service] resolving provenance for metadata file 0.0s
[+] up 16/16
✔ Image bionews-scheduler Built 3.4s
✔ Image bionews-news-service Built 3.4s
✔ Image bionews-auth-service Built 3.4s
✔ Image bionews-legal-service Built 3.4s
✔ Image bionews-consultations-service Built 3.4s
✔ Image bionews-web Built 3.4s
✔ Network bionews_bionews-net Created 0.0s
✔ Container bionews-redis Started 0.7s
✔ Container bionews-gateway Started 0.8s
✔ Container bionews-postgres Healthy 6.2s
✔ Container bionews-consultations-service Started 6.4s
✔ Container bionews-news-service Started 6.4s
✔ Container bionews-legal-service Started 6.4s
✔ Container bionews-auth-service Started 6.4s
✔ Container bionews-scheduler Started 6.5s
✔ Container bionews-web Started
