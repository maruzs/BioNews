# docker compose logs -f (Borre los de health)
```bash
maru@maru:/opt/BioNews$ docker compose logs -f
bionews-scheduler  | 2026-05-20 16:20:11  [INFO]  BioNews Scheduler iniciado.
bionews-scheduler  | 2026-05-20 16:20:11  [INFO]  Configurando scheduler con parametros: {'snifa_time_1': '07:00', 'snifa_time_2': '14:00', 'pertinencias_interval': 1, 'noticias_interval': 1, 'tribunales_interval': 1, 'consultas_time_1': '08:30', 'consultas_time_2': '15:30', 'hora_inicio': '07:00', 'hora_fin': '19:00'}
bionews-api        | 2026-05-20 16:20:06,256 [INFO] Inicializando pool DB Única (bionews@postgres-db/bionews)
bionews-api        | INFO:     Started server process [1]
bionews-api        | INFO:     Waiting for application startup.
bionews-api        | 2026-05-20 16:20:06,328 [INFO] Iniciando verificación y creación de índices de optimización en PostgreSQL...
bionews-api        | 2026-05-20 16:20:06,329 [INFO] Verificando extensión pg_trgm...
bionews-api        | 2026-05-20 16:20:06,329 [INFO] Creando índices de fecha_scraping en tablas del SEA, Normativas, Tribunales y Medidas...
bionews-api        | 2026-05-20 16:20:06,332 [INFO] Creando índices trigram GIN para búsquedas de texto rápido...
bionews-api        | 2026-05-20 16:20:06,333 [INFO] Creando índice funcional para ordenamiento de fecha de presentación en Proyectos Evaluados...
bionews-api        | 2026-05-20 16:20:06,434 [INFO] ✓ Índices del esquema scrapers verificados/creados exitosamente.
bionews-api        | 2026-05-20 16:20:06,434 [INFO] BioNews Backend Started. External scheduler.py is used as the primary scheduler.
bionews-api        | INFO:     Application startup complete.
bionews-api        | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
bionews-api        | INFO:     127.0.0.1:56232 - "GET /api/health HTTP/1.1" 200 OK
bionews-redis      | 1:C 20 May 2026 17:13:00.849 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis      | 1:C 20 May 2026 17:13:00.849 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis      | 1:C 20 May 2026 17:13:00.849 * Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis      | 1:C 20 May 2026 17:13:00.849 * Configuration loaded
bionews-redis      | 1:M 20 May 2026 17:13:00.849 * Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis      | 1:M 20 May 2026 17:13:00.849 * monotonic clock: POSIX clock_gettime
bionews-redis      | 1:M 20 May 2026 17:13:00.851 * Running mode=standalone, port=6379.
bionews-redis      | 1:M 20 May 2026 17:13:00.851 * Server initialized
bionews-redis      | 1:M 20 May 2026 17:13:00.851 * Ready to accept connections tcp
bionews-redis      | 1:M 20 May 2026 18:13:01.076 * 1 changes in 3600 seconds. Saving...
bionews-redis      | 1:M 20 May 2026 18:13:01.076 * Background saving started by pid 2152
bionews-redis      | 2152:C 20 May 2026 18:13:01.159 * DB saved on disk
bionews-redis      | 2152:C 20 May 2026 18:13:01.160 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-web        | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web        | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-db         |
bionews-db         | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db         |
bionews-redis      | 1:M 20 May 2026 18:13:01.177 * Background saving terminated with success
bionews-db         | 2026-05-20 17:13:00.927 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db         | 2026-05-20 17:13:00.928 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-redis      | 1:M 20 May 2026 19:13:02.046 * 1 changes in 3600 seconds. Saving...
bionews-redis      | 1:M 20 May 2026 19:13:02.048 * Background saving started by pid 4297
bionews-redis      | 4297:C 20 May 2026 19:13:02.140 * DB saved on disk
bionews-redis      | 4297:C 20 May 2026 19:13:02.142 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-redis      | 1:M 20 May 2026 19:13:02.149 * Background saving terminated with success
bionews-redis      | 1:M 20 May 2026 20:13:03.101 * 1 changes in 3600 seconds. Saving...
bionews-db         | 2026-05-20 17:13:00.928 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db         | 2026-05-20 17:13:00.932 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-redis      | 1:M 20 May 2026 20:13:03.102 * Background saving started by pid 6439
bionews-redis      | 6439:C 20 May 2026 20:13:03.114 * DB saved on disk
bionews-db         | 2026-05-20 17:13:00.949 UTC [29] LOG:  database system was shut down at 2026-05-20 17:10:22 UTC
bionews-web        | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web        | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-db         | 2026-05-20 17:13:00.963 UTC [1] LOG:  database system is ready to accept connections
bionews-web        | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-db         | 2026-05-20 17:18:01.049 UTC [27] LOG:  checkpoint starting: time
bionews-web        | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-db         | 2026-05-20 17:18:01.761 UTC [27] LOG:  checkpoint complete: wrote 9 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.610 s, sync=0.013 s, total=0.713 s; sync files=8, longest=0.010 s, average=0.002 s; distance=26 kB, estimate=26 kB; lsn=0/35A1EE8, redo lsn=0/35A1EB0
bionews-db         | 2026-05-20 17:23:01.862 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 17:23:02.567 UTC [27] LOG:  checkpoint complete: wrote 7 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.606 s, sync=0.012 s, total=0.706 s; sync files=7, longest=0.010 s, average=0.002 s; distance=35 kB, estimate=35 kB; lsn=0/35AACF8, redo lsn=0/35AACC0
bionews-web        | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-web        | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-web        | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-db         | 2026-05-20 17:33:01.768 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 17:33:02.197 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.404 s, sync=0.010 s, total=0.429 s; sync files=5, longest=0.008 s, average=0.002 s; distance=16 kB, estimate=33 kB; lsn=0/35AED50, redo lsn=0/35AED18
bionews-db         | 2026-05-20 17:38:01.229 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 17:38:02.920 UTC [27] LOG:  checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.594 s, sync=0.007 s, total=1.692 s; sync files=14, longest=0.004 s, average=0.001 s; distance=84 kB, estimate=84 kB; lsn=0/35C3D70, redo lsn=0/35C3D38
bionews-db         | 2026-05-20 18:23:02.579 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 18:23:03.086 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.010 s, total=0.508 s; sync files=5, longest=0.009 s, average=0.002 s; distance=28 kB, estimate=78 kB; lsn=0/35CADD0, redo lsn=0/35CAD98
bionews-db         | 2026-05-20 18:28:02.158 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 18:28:03.065 UTC [27] LOG:  checkpoint complete: wrote 9 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.806 s, sync=0.013 s, total=0.907 s; sync files=9, longest=0.010 s, average=0.002 s; distance=44 kB, estimate=75 kB; lsn=0/35D5E88, redo lsn=0/35D5E50
bionews-db         | 2026-05-20 18:33:02.132 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 18:33:02.436 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.011 s, total=0.305 s; sync files=3, longest=0.009 s, average=0.004 s; distance=7 kB, estimate=68 kB; lsn=0/35D7D68, redo lsn=0/35D7D30
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: using the "epoll" event method
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: nginx/1.31.0
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker processes
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 29
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 30
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 31
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 32
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 33
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 34
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 35
bionews-db         | 2026-05-20 18:38:02.535 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 18:38:03.043 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.011 s, total=0.508 s; sync files=5, longest=0.010 s, average=0.003 s; distance=7 kB, estimate=62 kB; lsn=0/35D9C08, redo lsn=0/35D9BD0
bionews-db         | 2026-05-20 19:13:02.616 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 19:13:11.462 UTC [27] LOG:  checkpoint complete: wrote 87 buffers (0.5%); 0 WAL file(s) added, 0 removed, 0 recycled; write=8.738 s, sync=0.089 s, total=8.846 s; sync files=20, longest=0.081 s, average=0.005 s; distance=776 kB, estimate=776 kB; lsn=0/369BCE8, redo lsn=0/369BCB0
bionews-db         | 2026-05-20 19:23:02.568 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 19:23:09.169 UTC [27] LOG:  checkpoint complete: wrote 64 buffers (0.4%); 0 WAL file(s) added, 0 removed, 0 recycled; write=6.504 s, sync=0.007 s, total=6.602 s; sync files=12, longest=0.003 s, average=0.001 s; distance=655 kB, estimate=764 kB; lsn=0/373FB48, redo lsn=0/373FB10
bionews-db         | 2026-05-20 19:33:02.220 UTC [27] LOG:  checkpoint starting: time
bionews-web        | 2026/05/20 20:20:11 [notice] 1#1: start worker process 36
bionews-db         | 2026-05-20 19:33:05.230 UTC [27] LOG:  checkpoint complete: wrote 30 buffers (0.2%); 0 WAL file(s) added, 0 removed, 0 recycled; write=2.914 s, sync=0.006 s, total=3.011 s; sync files=12, longest=0.001 s, average=0.001 s; distance=182 kB, estimate=706 kB; lsn=0/376D628, redo lsn=0/376D5F0
bionews-db         | 2026-05-20 19:33:29.383 UTC [6023] ERROR:  functions in index expression must be marked IMMUTABLE
bionews-db         | 2026-05-20 19:33:29.383 UTC [6023] STATEMENT:  CREATE INDEX IF NOT EXISTS idx_sea_fecha_presentacion_date ON sea_proyectos_evaluados (to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC);
bionews-db         | 2026-05-20 19:38:02.331 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 19:38:37.065 UTC [27] LOG:  checkpoint complete: wrote 341 buffers (2.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=34.553 s, sync=0.093 s, total=34.735 s; sync files=71, longest=0.081 s, average=0.002 s; distance=1520 kB, estimate=1520 kB; lsn=0/38E9938, redo lsn=0/38E9900
bionews-db         | 2026-05-20 20:01:57.854 UTC [7237] ERROR:  functions in index expression must be marked IMMUTABLE
bionews-db         | 2026-05-20 20:01:57.854 UTC [7237] STATEMENT:  CREATE INDEX IF NOT EXISTS idx_sea_fecha_presentacion_date ON sea_proyectos_evaluados (to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC);
bionews-db         | 2026-05-20 20:08:02.419 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 20:08:04.212 UTC [27] LOG:  checkpoint complete: wrote 17 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.694 s, sync=0.007 s, total=1.793 s; sync files=15, longest=0.003 s, average=0.001 s; distance=60 kB, estimate=1374 kB; lsn=0/38F8A30, redo lsn=0/38F89F8
bionews-db         | 2026-05-20 20:13:02.313 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 20:13:02.721 UTC [27] LOG:  checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.306 s, sync=0.011 s, total=0.409 s; sync files=4, longest=0.009 s, average=0.003 s; distance=11 kB, estimate=1238 kB; lsn=0/38FB898, redo lsn=0/38FB860
bionews-db         | 2026-05-20 20:18:02.768 UTC [27] LOG:  checkpoint starting: time
bionews-db         | 2026-05-20 20:18:03.680 UTC [27] LOG:  checkpoint complete: wrote 9 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.809 s, sync=0.012 s, total=0.913 s; sync files=7, longest=0.010 s, average=0.002 s; distance=48 kB, estimate=1119 kB; lsn=0/39078F0, redo lsn=0/39078B8
bionews-redis      | 6439:C 20 May 2026 20:13:03.116 * Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-redis      | 1:M 20 May 2026 20:13:03.204 * Background saving terminated with success
```

