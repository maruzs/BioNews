maru@maru:/opt/BioNews$ docker compose up -d --build
[+] Building 179.3s (42/42) FINISHED
=> [internal] load local bake definitions 0.0s
=> => reading from stdin 2.56kB 0.0s
=> [scheduler internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 1.56kB 0.0s
=> [web internal] load build definition from Dockerfile 0.0s
=> => transferring dockerfile: 822B 0.0s
=> [auth-service internal] load metadata for docker.io/library/python:3.11-slim 0.7s
=> [web internal] load metadata for docker.io/library/node:20-alpine 0.7s
=> [web internal] load metadata for docker.io/library/nginx:alpine 0.0s
=> [auth-service internal] load .dockerignore 0.0s
=> => transferring context: 456B 0.0s
=> [web internal] load .dockerignore 0.0s
=> => transferring context: 97B 0.0s
=> [legal-service internal] load build context 0.0s
=> => transferring context: 16.04kB 0.0s
=> [scheduler 1/11] FROM docker.io/library/python:3.11-slim@sha256:9a7765b36773a37061455b332f18e265e7f58f6fea9c419a550d2a8b0e9db834 0.1s
=> => resolve docker.io/library/python:3.11-slim@sha256:9a7765b36773a37061455b332f18e265e7f58f6fea9c419a550d2a8b0e9db834 0.1s
=> [web stage-1 1/3] FROM docker.io/library/nginx:alpine@sha256:dc48b7a872a79fb541ba5081d320b11b549231bc63ba465a7495afaa7d2ebcb8 0.1s
=> => resolve docker.io/library/nginx:alpine@sha256:dc48b7a872a79fb541ba5081d320b11b549231bc63ba465a7495afaa7d2ebcb8 0.1s
=> [web builder 1/6] FROM docker.io/library/node:20-alpine@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293 0.1s
=> => resolve docker.io/library/node:20-alpine@sha256:fb4cd12c85ee03686f6af5362a0b0d56d50c58a04632e6c0fb8363f609372293 0.1s
=> [web internal] load build context 0.1s
=> => transferring context: 5.18kB 0.0s
=> CACHED [web builder 2/6] WORKDIR /app 0.0s
=> CACHED [web builder 3/6] COPY package.json package-lock.json ./ 0.0s
=> CACHED [web builder 4/6] RUN npm ci 0.0s
=> CACHED [web builder 5/6] COPY . . 0.0s
=> CACHED [web builder 6/6] RUN npm run build 0.0s
=> CACHED [web stage-1 2/3] COPY --from=builder /app/dist /usr/share/nginx/html 0.0s
=> CACHED [web stage-1 3/3] COPY nginx.conf /etc/nginx/conf.d/default.conf 0.0s
=> [web] exporting to image 0.4s
=> => exporting layers 0.0s
=> => exporting manifest sha256:0615af306fa7efdd7c4d926cd4ef123daa14ef1aaf27854297ee8a141681e965 0.0s
=> => exporting config sha256:ea92359b07d71ffff26bfdf9f9da6a0edb407716b4535b5a8aace3f00f7a8958 0.0s
=> => exporting attestation manifest sha256:ad51b0c6af04bdd1c2a2742d5b86a2a6e7abfb4aa0a8168fe20034b0fe5bf368 0.1s
=> => exporting manifest list sha256:64de496b1d35a539a725ab65ab8d1b108f977c1fbace9314f2d8af4283cf3421 0.0s
=> => naming to docker.io/library/bionews-web:latest 0.0s
=> => unpacking to docker.io/library/bionews-web:latest 0.0s
=> CACHED [news-service 2/11] WORKDIR /app 0.0s
=> CACHED [news-service 3/11] RUN apt-get update && apt-get install -y --no-install-recommends wget ca-certificates fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 0.0s
=> [consultations-service 4/11] COPY requirements.docker.txt ./requirements.txt 0.1s
=> [auth-service 5/11] RUN pip install --no-cache-dir -r requirements.txt 20.0s
=> [web] resolving provenance for metadata file 0.0s
=> [scheduler 6/11] RUN playwright install chromium && playwright install-deps chromium 64.9s
=> [scheduler 7/11] COPY server.py . 0.1s
=> [legal-service 8/11] COPY scheduler.py . 0.1s
=> [auth-service 9/11] COPY startScraping.py . 0.1s
=> [auth-service 10/11] COPY src/ ./src/ 0.1s
=> [scheduler 11/11] RUN mkdir -p /app/data /app/logs /app/uploads/bugs 0.3s
=> [scheduler] exporting to image 91.7s
=> => exporting layers 36.8s
=> => exporting manifest sha256:084dfd4f7c6569b5f7204a6cdfc8a56bdfd75eebdbda97755a5b264e3b34337c 0.1s
=> => exporting config sha256:619405ae52effbf9d085bc7aad27c434e911973a55451b8826a1c233e922ac46 0.2s
=> => exporting attestation manifest sha256:2cda8caf843bfb48377cee04287bfb93e9991b2e6b8055a531c9f2450ffe98f2 0.2s
=> => exporting manifest list sha256:bf3812fdb882fa978e9ac04930747adf0373823b65cb15f42ee7f32f10435c43 0.1s
=> => naming to docker.io/library/bionews-scheduler:latest 0.0s
=> => unpacking to docker.io/library/bionews-scheduler:latest 54.1s
=> [auth-service] exporting to image 91.7s
=> => exporting layers 36.8s
=> => exporting manifest sha256:73f7b55faac6792aa30dc442b0e1caa8c8fd15965ca863ebaf94d66e17903646 0.1s
=> => exporting config sha256:47bb977efa639e95e0ac8dfd15622e6cc863ce5a2a77e7fef500d8c64a5dd30f 0.2s
=> => exporting attestation manifest sha256:04f1bb9580fba154edc2b2392d882b3334217a4413d8f60a260c2f9b83a02944 0.2s
=> => exporting manifest list sha256:8a6efd4fc8ec59b87fb99f3517826d3bd8e169a5532ea4fc250caa94a96381e0 0.1s
=> => naming to docker.io/library/bionews-auth-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-auth-service:latest 54.1s
=> [consultations-service] exporting to image 91.7s
=> => exporting layers 36.8s
=> => exporting manifest sha256:4eda92f299c91c142384dbe25d2df041ff394f5ff7c977a7c23e04bacee826fc 0.1s
=> => exporting config sha256:516a615d8cb309e07520aa0281512bb4e61c2a361d997766e71067f631beef90 0.2s
=> => exporting attestation manifest sha256:4bbd55697451035fc51e72af4bbbf5f1c79ba6ba2fe579f76f6d41c8f03f8555 0.2s
=> => exporting manifest list sha256:4e06becc3d48a0e90401aa958dd0ac27c1d3d5dac743b6f0e88eab1236e37082 0.1s
=> => naming to docker.io/library/bionews-consultations-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-consultations-service:latest 54.1s
=> [news-service] exporting to image 91.7s
=> => exporting layers 36.8s
=> => exporting manifest sha256:05665f534279cb8ed2c3cf2aa4c452b745d5f6619f45c46bfe72b0acd5fc57c4 0.2s
=> => exporting config sha256:79b77e2af3416c9348f9ef130daa1bd726a3d65e4a5a61f4beddad3e599c19ba 0.1s
=> => exporting attestation manifest sha256:8124b193e74ae7a2a751dedec9f39e03a529852a4a52400ce57b7ec397a36c1b 0.2s
=> => exporting manifest list sha256:a5844c71013285630451ee6937a4d4743a643ddb44a2ee954ab54173d3ec8d08 0.1s
=> => naming to docker.io/library/bionews-news-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-news-service:latest 54.1s
=> [legal-service] exporting to image 91.7s
=> => exporting layers 36.8s
=> => exporting manifest sha256:1a7a3ff2228dc8e8ed31b73d731ac54590fdd625b9d42a73f020ea43911673c5 0.1s
=> => exporting config sha256:a908beacca575ffdd747ea1fbd1af46a2ef258ff117d6527a31d69b1cbd8b6c9 0.2s
=> => exporting attestation manifest sha256:b152fec4dbc375a6678cac6993ad69023f5d020bd3cbe105cb10830da3f3d804 0.2s
=> => exporting manifest list sha256:cc22b7607d69cf8d514564acc7c98582901fd31dfbce9a364c189aac5d45474d 0.1s
=> => naming to docker.io/library/bionews-legal-service:latest 0.0s
=> => unpacking to docker.io/library/bionews-legal-service:latest 54.1s
=> [auth-service] resolving provenance for metadata file 0.4s
=> [news-service] resolving provenance for metadata file 0.3s
=> [scheduler] resolving provenance for metadata file 0.2s
=> [consultations-service] resolving provenance for metadata file 0.1s
=> [legal-service] resolving provenance for metadata file 0.0s
[+] up 16/16
✔ Image bionews-auth-service Built 179.4s
✔ Image bionews-web Built 179.4s
✔ Image bionews-legal-service Built 179.4s
✔ Image bionews-consultations-service Built 179.4s
✔ Image bionews-scheduler Built 179.4s
✔ Image bionews-news-service Built 179.4s
✔ Network bionews_bionews-net Created 0.0s
✔ Container bionews-redis Started 3.4s
✔ Container bionews-postgres Healthy 8.9s
✔ Container bionews-gateway Started 3.4s
✔ Container bionews-legal-service Started 6.8s
✔ Container bionews-news-service Started 6.8s
✔ Container bionews-scheduler Started 6.8s
✔ Container bionews-auth-service Started 6.8s
✔ Container bionews-consultations-service Started 6.8s
✔ Container bionews-web Started
