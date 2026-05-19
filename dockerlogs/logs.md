```bash
maru@maru:/opt/BioNews$ docker compose logs -f
bionews-scheduler | 2026-05-19 11:40:02 [INFO] BioNews Scheduler iniciado.
bionews-scheduler | 2026-05-19 11:40:02 [INFO] Configurando scheduler con parametros: {'snifa_time_1': '07:00', 'snifa_time_2': '14:00', 'pertinencias_interval': 1, 'noticias_interval': 1, 'tribunales_interval': 1, 'consultas_time_1': '08:30', 'consultas_time_2': '15:30', 'hora_inicio': '07:00', 'hora_fin': '19:00'}
bionews-web | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-web | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-web | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-web | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: using the "epoll" event method
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: nginx/1.31.0
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker processes
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 29
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 30
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 31
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 32
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 33
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 34
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 35
bionews-web | 2026/05/19 15:40:02 [notice] 1#1: start worker process 36
bionews-api | 2026-05-19 11:39:57,926 [INFO] Inicializando pool DB Única (bionews@postgres-db/bionews)
bionews-api | 2026-05-19 11:39:57,933 [WARNING] Fallo de conexión inicial con contraseña. Reintentando con contraseña alternativa...
bionews-api | 2026-05-19 11:39:57,947 [INFO] Conectado con éxito usando contraseña alternativa.
bionews-api | INFO: Started server process [1]
bionews-api | INFO: Waiting for application startup.
bionews-api | 2026-05-19 11:39:58,005 [INFO] BioNews Backend Started. Scheduler monitor active.
bionews-api | INFO: Application startup complete.
bionews-api | INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
bionews-api | INFO: 127.0.0.1:51298 - "GET /api/health HTTP/1.1" 200 OK
bionews-api | INFO: 172.18.0.5:60718 - "GET /api/notifications/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZW1haWwiOiJhZG1pbmlzdHJhZG9yQGJpb25ld3MuY2wiLCJyb2xlIjoiYWRtaW4iLCJuYW1lIjoiQWRtaW5pc3RyYWRvciIsImV4cCI6MTc4MTc5NDQ0NH0.kOrXf32fRvj35xugkUc-iJ-EA5BV7-33k_mu_Wlqz7g HTTP/1.1" 200 OK
bionews-redis | 1:C 19 May 2026 00:51:22.361 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 19 May 2026 00:51:22.361 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 19 May 2026 00:51:22.361 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 19 May 2026 00:51:22.361 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 19 May 2026 00:51:22.361 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 19 May 2026 00:51:22.361 _ monotonic clock: POSIX clock_gettime
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-05-19 00:51:22.433 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-05-19 00:51:22.433 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-05-19 00:51:22.433 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-05-19 00:51:22.438 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-05-19 00:51:22.450 UTC [29] LOG: database system was shut down at 2026-05-19 00:50:48 UTC
bionews-db | 2026-05-19 00:51:22.466 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 00:51:34.392 UTC [40] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 00:51:34.392 UTC [40] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 00:56:22.543 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 00:56:22.752 UTC [27] LOG: checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.107 s, sync=0.011 s, total=0.209 s; sync files=3, longest=0.008 s, average=0.004 s; distance=2 kB, estimate=2 kB; lsn=0/31840F8, redo lsn=0/31840C0
bionews-db | 2026-05-19 01:01:22.815 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 01:01:23.450 UTC [27] LOG: checkpoint complete: wrote 7 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.605 s, sync=0.012 s, total=0.635 s; sync files=7, longest=0.009 s, average=0.002 s; distance=13 kB, estimate=13 kB; lsn=0/31875A8, redo lsn=0/3187570
bionews-db | 2026-05-19 10:51:32.883 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 10:51:33.213 UTC [27] LOG: checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.305 s, sync=0.009 s, total=0.330 s; sync files=4, longest=0.008 s, average=0.003 s; distance=9 kB, estimate=12 kB; lsn=0/3189A00, redo lsn=0/31899C8
bionews-db | 2026-05-19 11:00:10.313 UTC [27197] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 11:00:10.313 UTC [27197] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 11:01:32.413 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 11:01:32.920 UTC [27] LOG: checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.012 s, total=0.507 s; sync files=5, longest=0.009 s, average=0.003 s; distance=17 kB, estimate=17 kB; lsn=0/318E150, redo lsn=0/318E118
bionews-db | 2026-05-19 11:06:32.955 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 11:06:34.535 UTC [27] LOG: checkpoint complete: wrote 15 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.486 s, sync=0.006 s, total=1.581 s; sync files=9, longest=0.003 s, average=0.001 s; distance=79 kB, estimate=79 kB; lsn=0/31A1E38, redo lsn=0/31A1E00
bionews-db | 2026-05-19 11:11:32.615 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 11:11:33.118 UTC [27] LOG: checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.009 s, total=0.503 s; sync files=5, longest=0.008 s, average=0.002 s; distance=17 kB, estimate=73 kB; lsn=0/31A6558, redo lsn=0/31A6520
bionews-db | 2026-05-19 11:16:32.219 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 11:16:32.824 UTC [27] LOG: checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.506 s, sync=0.011 s, total=0.605 s; sync files=5, longest=0.009 s, average=0.003 s; distance=29 kB, estimate=68 kB; lsn=0/31ADA00, redo lsn=0/31AD9C8
bionews-db | 2026-05-19 11:21:32.858 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 11:21:33.361 UTC [27] LOG: checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.404 s, sync=0.010 s, total=0.503 s; sync files=5, longest=0.009 s, average=0.002 s; distance=11 kB, estimate=62 kB; lsn=0/31B0650, redo lsn=0/31B0618
bionews-db | 2026-05-19 11:51:00.048 UTC [1] LOG: received fast shutdown request
bionews-db | 2026-05-19 11:51:00.059 UTC [1] LOG: aborting any active transactions
bionews-db | 2026-05-19 11:51:00.059 UTC [27199] FATAL: terminating connection due to administrator command
bionews-db | 2026-05-19 11:51:00.059 UTC [27198] FATAL: terminating connection due to administrator command
bionews-db | 2026-05-19 11:51:00.064 UTC [88] FATAL: terminating connection due to administrator command
bionews-db | 2026-05-19 11:51:00.069 UTC [41] FATAL: terminating connection due to administrator command
bionews-db | 2026-05-19 11:51:00.073 UTC [1] LOG: background worker "logical replication launcher" (PID 32) exited with exit code 1
bionews-db | 2026-05-19 11:51:00.076 UTC [27] LOG: shutting down
bionews-db | 2026-05-19 11:51:00.087 UTC [27] LOG: checkpoint starting: shutdown immediate
bionews-db | 2026-05-19 11:51:00.284 UTC [27] LOG: checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.083 s, sync=0.027 s, total=0.209 s; sync files=4, longest=0.013 s, average=0.007 s; distance=0 kB, estimate=56 kB; lsn=0/31B0700, redo lsn=0/31B0700
bionews-db | 2026-05-19 11:51:00.346 UTC [1] LOG: database system is shut down
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-04-15 18:33:02.768 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-04-15 18:33:02.768 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-04-15 18:33:02.768 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-04-15 18:33:02.780 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-04-15 18:33:02.795 UTC [28] LOG: database system was shut down at 2026-05-19 11:51:00 UTC
bionews-db | 2026-04-15 18:33:02.819 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 12:44:46.840 UTC [99] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 12:44:46.840 UTC [99] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 12:45:16.220 UTC [1] LOG: received fast shutdown request
bionews-db | 2026-05-19 12:45:16.252 UTC [1] LOG: aborting any active transactions
bionews-db | 2026-05-19 12:45:16.252 UTC [101] FATAL: terminating connection due to administrator command
bionews-db | 2026-05-19 12:45:16.254 UTC [100] FATAL: terminating connection due to administrator command
bionews-db | 2026-05-19 12:45:16.261 UTC [1] LOG: background worker "logical replication launcher" (PID 31) exited with exit code 1
bionews-db | 2026-05-19 12:45:16.269 UTC [26] LOG: shutting down
bionews-db | 2026-05-19 12:45:16.288 UTC [26] LOG: checkpoint starting: shutdown immediate
bionews-db | 2026-05-19 12:45:16.343 UTC [26] LOG: checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.020 s, sync=0.005 s, total=0.074 s; sync files=2, longest=0.003 s, average=0.003 s; distance=0 kB, estimate=0 kB; lsn=0/31B07B0, redo lsn=0/31B07B0
bionews-db | 2026-05-19 12:45:16.387 UTC [1] LOG: database system is shut down
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-05-19 12:53:38.656 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-05-19 12:53:38.657 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-05-19 12:53:38.657 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-05-19 12:53:38.667 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-05-19 12:53:38.682 UTC [29] LOG: database system was shut down at 2026-05-19 12:45:16 UTC
bionews-db | 2026-05-19 12:53:38.709 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 12:54:38.224 UTC [1] LOG: received fast shutdown request
bionews-db | 2026-05-19 12:54:38.227 UTC [1] LOG: aborting any active transactions
bionews-db | 2026-05-19 12:54:38.243 UTC [1] LOG: background worker "logical replication launcher" (PID 32) exited with exit code 1
bionews-db | 2026-05-19 12:54:38.248 UTC [27] LOG: shutting down
bionews-db | 2026-05-19 12:54:38.251 UTC [27] LOG: checkpoint starting: shutdown immediate
bionews-db | 2026-05-19 12:54:38.316 UTC [27] LOG: checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.024 s, sync=0.003 s, total=0.069 s; sync files=2, longest=0.002 s, average=0.002 s; distance=0 kB, estimate=0 kB; lsn=0/31B0860, redo lsn=0/31B0860
bionews-db | 2026-05-19 12:54:38.325 UTC [1] LOG: database system is shut down
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-05-19 12:57:03.992 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-05-19 12:57:03.992 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-05-19 12:57:03.992 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-05-19 12:57:04.001 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-05-19 12:57:04.015 UTC [29] LOG: database system was shut down at 2026-05-19 12:54:38 UTC
bionews-db | 2026-05-19 12:57:04.057 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 12:58:46.976 UTC [1] LOG: received fast shutdown request
bionews-db | 2026-05-19 12:58:46.980 UTC [1] LOG: aborting any active transactions
bionews-db | 2026-05-19 12:58:47.024 UTC [1] LOG: background worker "logical replication launcher" (PID 32) exited with exit code 1
bionews-db | 2026-05-19 12:58:47.025 UTC [27] LOG: shutting down
bionews-db | 2026-05-19 12:58:47.030 UTC [27] LOG: checkpoint starting: shutdown immediate
bionews-db | 2026-05-19 12:58:47.059 UTC [27] LOG: checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.007 s, sync=0.005 s, total=0.035 s; sync files=2, longest=0.004 s, average=0.003 s; distance=0 kB, estimate=0 kB; lsn=0/31B0910, redo lsn=0/31B0910
bionews-db | 2026-05-19 12:58:47.076 UTC [1] LOG: database system is shut down
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-05-19 12:59:44.113 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-05-19 12:59:44.113 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-05-19 12:59:44.113 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-05-19 12:59:44.120 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-05-19 12:59:44.132 UTC [30] LOG: database system was shut down at 2026-05-19 12:58:47 UTC
bionews-db | 2026-05-19 12:59:44.151 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 13:01:20.538 UTC [1] LOG: received fast shutdown request
bionews-db | 2026-05-19 13:01:20.540 UTC [1] LOG: aborting any active transactions
bionews-db | 2026-05-19 13:01:20.549 UTC [1] LOG: background worker "logical replication launcher" (PID 33) exited with exit code 1
bionews-db | 2026-05-19 13:01:20.551 UTC [28] LOG: shutting down
bionews-db | 2026-05-19 13:01:20.554 UTC [28] LOG: checkpoint starting: shutdown immediate
bionews-db | 2026-05-19 13:01:20.600 UTC [28] LOG: checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.018 s, sync=0.004 s, total=0.049 s; sync files=2, longest=0.003 s, average=0.002 s; distance=0 kB, estimate=0 kB; lsn=0/31B09C0, redo lsn=0/31B09C0
bionews-db | 2026-05-19 13:01:20.613 UTC [1] LOG: database system is shut down
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-04-15 18:33:02.603 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-04-15 18:33:02.603 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-04-15 18:33:02.603 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-04-15 18:33:02.608 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-04-15 18:33:02.619 UTC [29] LOG: database system was shut down at 2026-05-19 13:01:20 UTC
bionews-db | 2026-04-15 18:33:02.638 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 13:15:30.840 UTC [56] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 13:15:30.840 UTC [56] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db |
bionews-db | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db |
bionews-db | 2026-04-15 18:33:04.835 UTC [1] LOG: starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db | 2026-04-15 18:33:04.835 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-db | 2026-04-15 18:33:04.835 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-db | 2026-04-15 18:33:04.843 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db | 2026-04-15 18:33:04.852 UTC [29] LOG: database system was interrupted; last known up at 2026-04-15 18:33:02 UTC
bionews-db | 2026-04-15 18:33:05.503 UTC [29] LOG: database system was not properly shut down; automatic recovery in progress
bionews-db | 2026-04-15 18:33:05.515 UTC [29] LOG: redo starts at 0/31B0A38
bionews-db | 2026-04-15 18:33:05.515 UTC [29] LOG: invalid record length at 0/31B0A70: expected at least 24, got 0
bionews-db | 2026-04-15 18:33:05.515 UTC [29] LOG: redo done at 0/31B0A38 system usage: CPU: user: 0.00 s, system: 0.00 s, elapsed: 0.00 s
bionews-db | 2026-04-15 18:33:05.530 UTC [27] LOG: checkpoint starting: end-of-recovery immediate wait
bionews-db | 2026-04-15 18:33:05.566 UTC [27] LOG: checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.016 s, sync=0.003 s, total=0.039 s; sync files=2, longest=0.002 s, average=0.002 s; distance=0 kB, estimate=0 kB; lsn=0/31B0A70, redo lsn=0/31B0A70
bionews-db | 2026-04-15 18:33:05.581 UTC [1] LOG: database system is ready to accept connections
bionews-db | 2026-05-19 13:17:51.523 UTC [53] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 13:17:51.523 UTC [53] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 13:22:21.092 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 13:22:26.051 UTC [27] LOG: checkpoint complete: wrote 50 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.926 s, sync=0.015 s, total=4.959 s; sync files=27, longest=0.011 s, average=0.001 s; distance=387 kB, estimate=387 kB; lsn=0/3222940, redo lsn=0/3211840
bionews-db | 2026-05-19 14:01:17.138 UTC [1903] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 14:01:17.138 UTC [1903] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 14:05:21.708 UTC [2086] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 14:05:21.708 UTC [2086] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 14:07:21.866 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 14:07:23.075 UTC [27] LOG: checkpoint complete: wrote 12 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.115 s, sync=0.005 s, total=1.210 s; sync files=11, longest=0.003 s, average=0.001 s; distance=80 kB, estimate=356 kB; lsn=0/3225940, redo lsn=0/3225908
bionews-db | 2026-05-19 14:12:21.174 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 14:12:21.401 UTC [27] LOG: checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.203 s, sync=0.010 s, total=0.227 s; sync files=3, longest=0.009 s, average=0.004 s; distance=7 kB, estimate=321 kB; lsn=0/3227908, redo lsn=0/32278D0
bionews-db | 2026-05-19 14:17:21.501 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 14:17:22.026 UTC [27] LOG: checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.506 s, sync=0.009 s, total=0.525 s; sync files=5, longest=0.008 s, average=0.002 s; distance=30 kB, estimate=292 kB; lsn=0/322F338, redo lsn=0/322F300
bionews-db | 2026-05-19 14:22:21.125 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 14:22:21.560 UTC [27] LOG: checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.011 s, total=0.435 s; sync files=5, longest=0.009 s, average=0.003 s; distance=27 kB, estimate=266 kB; lsn=0/3236200, redo lsn=0/32361C8
bionews-db | 2026-05-19 14:57:22.100 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 14:57:22.691 UTC [27] LOG: checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.507 s, sync=0.012 s, total=0.592 s; sync files=6, longest=0.008 s, average=0.002 s; distance=11 kB, estimate=240 kB; lsn=0/3238F60, redo lsn=0/3238F28
bionews-db | 2026-05-19 15:02:22.728 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 15:02:24.273 UTC [27] LOG: checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.520 s, sync=0.008 s, total=1.546 s; sync files=16, longest=0.003 s, average=0.001 s; distance=50 kB, estimate=221 kB; lsn=0/3245A00, redo lsn=0/32459C8
bionews-db | 2026-05-19 15:07:22.374 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 15:07:23.792 UTC [27] LOG: checkpoint complete: wrote 14 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.320 s, sync=0.008 s, total=1.419 s; sync files=14, longest=0.003 s, average=0.001 s; distance=16 kB, estimate=201 kB; lsn=0/3249C70, redo lsn=0/3249C38
bionews-db | 2026-05-19 15:17:22.994 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 15:17:23.604 UTC [27] LOG: checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.507 s, sync=0.012 s, total=0.610 s; sync files=5, longest=0.008 s, average=0.003 s; distance=31 kB, estimate=184 kB; lsn=0/32518E0, redo lsn=0/32518A8
bionews-db | 2026-05-19 15:22:22.704 UTC [27] LOG: checkpoint starting: time
bionews-db | 2026-05-19 15:22:24.118 UTC [27] LOG: checkpoint complete: wrote 14 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.311 s, sync=0.011 s, total=1.414 s; sync files=11, longest=0.008 s, average=0.001 s; distance=74 kB, estimate=173 kB; lsn=0/32643D8, redo lsn=0/32643A0
bionews-db | 2026-05-19 15:27:46.397 UTC [5603] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 15:27:46.397 UTC [5603] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:27:52.462 UTC [5604] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 15:27:52.462 UTC [5604] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:27:52.578 UTC [5606] FATAL: password authentication failed for user "postgres"
bionews-db | 2026-05-19 15:27:52.578 UTC [5606] DETAIL: Role "postgres" does not exist.
bionews-db | Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:27:52.610 UTC [5607] FATAL: password authentication failed for user "postgres"
bionews-db | 2026-05-19 15:27:52.610 UTC [5607] DETAIL: Role "postgres" does not exist.
bionews-db | Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:27:52.641 UTC [5608] FATAL: password authentication failed for user "postgres"
bionews-db | 2026-05-19 15:27:52.641 UTC [5608] DETAIL: Role "postgres" does not exist.
bionews-db | Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:27:52.673 UTC [5609] FATAL: password authentication failed for user "postgres"
bionews-db | 2026-05-19 15:27:52.673 UTC [5609] DETAIL: Role "postgres" does not exist.
bionews-db | Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:27:52.706 UTC [5610] FATAL: password authentication failed for user "postgres"
bionews-db | 2026-05-19 15:27:52.706 UTC [5610] DETAIL: Role "postgres" does not exist.
bionews-db | Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:28:31.140 UTC [5641] ERROR: relation "Tribunales" does not exist at character 21
bionews-db | 2026-05-19 15:28:31.140 UTC [5641] STATEMENT: SELECT "Fecha" FROM "Tribunales" WHERE "Fecha" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:28:31.141 UTC [5641] ERROR: relation "pertinencias" does not exist at character 21
bionews-db | 2026-05-19 15:28:31.141 UTC [5641] STATEMENT: SELECT "Fecha" FROM "pertinencias" WHERE "Fecha" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:28:31.143 UTC [5641] ERROR: relation "sea_proyectos_evaluados" does not exist at character 34
bionews-db | 2026-05-19 15:28:31.143 UTC [5641] STATEMENT: SELECT "fecha_presentacion" FROM "sea_proyectos_evaluados" WHERE "fecha_presentacion" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:28:31.145 UTC [5641] ERROR: relation "minsal_vigentes" does not exist at character 28
bionews-db | 2026-05-19 15:28:31.145 UTC [5641] STATEMENT: SELECT "fecha_inicio" FROM "minsal_vigentes" WHERE "fecha_inicio" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:28:31.146 UTC [5641] ERROR: relation "mma_abiertas" does not exist at character 28
bionews-db | 2026-05-19 15:28:31.146 UTC [5641] STATEMENT: SELECT "fecha_inicio" FROM "mma_abiertas" WHERE "fecha_inicio" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:28:31.148 UTC [5641] ERROR: relation "normativas" does not exist at character 21
bionews-db | 2026-05-19 15:28:31.148 UTC [5641] STATEMENT: SELECT "fecha" FROM "normativas" WHERE "fecha" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:28:31.150 UTC [5641] ERROR: relation "noticias" does not exist at character 21
bionews-db | 2026-05-19 15:28:31.150 UTC [5641] STATEMENT: SELECT "fecha" FROM "noticias" WHERE "fecha" IS NOT NULL LIMIT 5
bionews-db | 2026-05-19 15:33:30.078 UTC [5858] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 15:33:30.078 UTC [5858] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db | 2026-05-19 15:39:57.933 UTC [6133] FATAL: password authentication failed for user "bionews"
bionews-db | 2026-05-19 15:39:57.933 UTC [6133] DETAIL: Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-redis | 1:M 19 May 2026 00:51:22.362 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 19 May 2026 00:51:22.363 _ Server initialized
bionews-redis | 1:M 19 May 2026 00:51:22.363 _ Ready to accept connections tcp
bionews-redis | 1:M 19 May 2026 01:51:23.004 _ 1 changes in 3600 seconds. Saving...
bionews-redis | 1:M 19 May 2026 01:51:23.005 _ Background saving started by pid 2159
bionews-redis | 2159:C 19 May 2026 01:51:23.088 _ DB saved on disk
bionews-redis | 2159:C 19 May 2026 01:51:23.089 _ Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-redis | 1:M 19 May 2026 01:51:23.106 _ Background saving terminated with success
bionews-redis | 1:M 19 May 2026 10:49:32.058 _ 1 changes in 3600 seconds. Saving...
bionews-redis | 1:M 19 May 2026 10:49:32.059 _ Background saving started by pid 21364
bionews-redis | 21364:C 19 May 2026 10:49:32.071 _ DB saved on disk
bionews-redis | 21364:C 19 May 2026 10:49:32.072 _ Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-redis | 1:M 19 May 2026 10:49:32.160 _ Background saving terminated with success
bionews-redis | 1:M 19 May 2026 11:49:33.094 _ 1 changes in 3600 seconds. Saving...
bionews-redis | 1:M 19 May 2026 11:49:33.094 _ Background saving started by pid 23515
bionews-redis | 23515:C 19 May 2026 11:49:33.105 _ DB saved on disk
bionews-redis | 23515:C 19 May 2026 11:49:33.106 _ Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-redis | 1:M 19 May 2026 11:49:33.196 _ Background saving terminated with success
bionews-redis | 1:signal-handler (1779191460) Received SIGTERM scheduling shutdown...
bionews-redis | 1:M 19 May 2026 11:51:00.123 _ User requested shutdown...
bionews-redis | 1:M 19 May 2026 11:51:00.123 _ Saving the final RDB snapshot before exiting.
bionews-redis | 1:M 19 May 2026 11:51:00.163 _ DB saved on disk
bionews-redis | 1:M 19 May 2026 11:51:00.163 # Redis is now ready to exit, bye bye...
bionews-redis | 1:C 15 Apr 2026 18:33:02.401 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 15 Apr 2026 18:33:02.401 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 15 Apr 2026 18:33:02.401 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 15 Apr 2026 18:33:02.401 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 15 Apr 2026 18:33:02.402 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 15 Apr 2026 18:33:02.402 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 15 Apr 2026 18:33:02.415 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 15 Apr 2026 18:33:02.415 _ Server initialized
bionews-redis | 1:M 15 Apr 2026 18:33:02.418 _ Loading RDB produced by version 7.4.9
bionews-redis | 1:M 15 Apr 2026 18:33:02.418 _ RDB age 0 seconds
bionews-redis | 1:M 15 Apr 2026 18:33:02.418 _ RDB memory usage when created 1.05 Mb
bionews-redis | 1:M 15 Apr 2026 18:33:02.418 _ Done loading RDB, keys loaded: 0, keys expired: 0.
bionews-redis | 1:M 15 Apr 2026 18:33:02.418 _ DB loaded from disk: 0.003 seconds
bionews-redis | 1:M 15 Apr 2026 18:33:02.418 _ Ready to accept connections tcp
bionews-redis | 1:signal-handler (1779194716) Received SIGTERM scheduling shutdown...
bionews-redis | 1:M 19 May 2026 12:45:16.320 _ User requested shutdown...
bionews-redis | 1:M 19 May 2026 12:45:16.320 _ Saving the final RDB snapshot before exiting.
bionews-redis | 1:M 19 May 2026 12:45:16.338 _ DB saved on disk
bionews-redis | 1:M 19 May 2026 12:45:16.338 # Redis is now ready to exit, bye bye...
bionews-redis | 1:C 19 May 2026 12:53:38.431 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 19 May 2026 12:53:38.431 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 19 May 2026 12:53:38.431 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 19 May 2026 12:53:38.431 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 19 May 2026 12:53:38.432 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 19 May 2026 12:53:38.432 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 19 May 2026 12:53:38.441 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 19 May 2026 12:53:38.441 _ Server initialized
bionews-redis | 1:M 19 May 2026 12:53:38.445 _ Loading RDB produced by version 7.4.9
bionews-redis | 1:M 19 May 2026 12:53:38.445 _ RDB age 502 seconds
bionews-redis | 1:M 19 May 2026 12:53:38.445 _ RDB memory usage when created 0.98 Mb
bionews-redis | 1:M 19 May 2026 12:53:38.445 _ Done loading RDB, keys loaded: 0, keys expired: 0.
bionews-redis | 1:M 19 May 2026 12:53:38.445 _ DB loaded from disk: 0.004 seconds
bionews-redis | 1:M 19 May 2026 12:53:38.445 _ Ready to accept connections tcp
bionews-redis | 1:signal-handler (1779195278) Received SIGTERM scheduling shutdown...
bionews-redis | 1:M 19 May 2026 12:54:38.266 _ User requested shutdown...
bionews-redis | 1:M 19 May 2026 12:54:38.266 _ Saving the final RDB snapshot before exiting.
bionews-redis | 1:M 19 May 2026 12:54:38.292 _ DB saved on disk
bionews-redis | 1:M 19 May 2026 12:54:38.292 # Redis is now ready to exit, bye bye...
bionews-redis | 1:C 19 May 2026 12:57:03.630 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 19 May 2026 12:57:03.631 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 19 May 2026 12:57:03.631 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 19 May 2026 12:57:03.631 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 19 May 2026 12:57:03.631 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 19 May 2026 12:57:03.631 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 19 May 2026 12:57:03.643 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 19 May 2026 12:57:03.643 _ Server initialized
bionews-redis | 1:M 19 May 2026 12:57:03.649 _ Loading RDB produced by version 7.4.9
bionews-redis | 1:M 19 May 2026 12:57:03.649 _ RDB age 145 seconds
bionews-redis | 1:M 19 May 2026 12:57:03.649 _ RDB memory usage when created 0.93 Mb
bionews-redis | 1:M 19 May 2026 12:57:03.649 _ Done loading RDB, keys loaded: 0, keys expired: 0.
bionews-redis | 1:M 19 May 2026 12:57:03.649 _ DB loaded from disk: 0.006 seconds
bionews-redis | 1:M 19 May 2026 12:57:03.649 _ Ready to accept connections tcp
bionews-redis | 1:signal-handler (1779195527) Received SIGTERM scheduling shutdown...
bionews-redis | 1:M 19 May 2026 12:58:47.098 _ User requested shutdown...
bionews-redis | 1:M 19 May 2026 12:58:47.098 _ Saving the final RDB snapshot before exiting.
bionews-redis | 1:M 19 May 2026 12:58:47.105 _ DB saved on disk
bionews-redis | 1:M 19 May 2026 12:58:47.105 # Redis is now ready to exit, bye bye...
bionews-redis | 1:C 19 May 2026 12:59:43.848 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 19 May 2026 12:59:43.848 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 19 May 2026 12:59:43.848 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 19 May 2026 12:59:43.848 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 19 May 2026 12:59:43.849 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 19 May 2026 12:59:43.849 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 19 May 2026 12:59:43.858 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 19 May 2026 12:59:43.858 _ Server initialized
bionews-redis | 1:M 19 May 2026 12:59:43.861 _ Loading RDB produced by version 7.4.9
bionews-redis | 1:M 19 May 2026 12:59:43.861 _ RDB age 56 seconds
bionews-redis | 1:M 19 May 2026 12:59:43.861 _ RDB memory usage when created 0.93 Mb
bionews-redis | 1:M 19 May 2026 12:59:43.861 _ Done loading RDB, keys loaded: 0, keys expired: 0.
bionews-redis | 1:M 19 May 2026 12:59:43.861 _ DB loaded from disk: 0.003 seconds
bionews-redis | 1:M 19 May 2026 12:59:43.861 _ Ready to accept connections tcp
bionews-redis | 1:signal-handler (1779195680) Received SIGTERM scheduling shutdown...
bionews-redis | 1:M 19 May 2026 13:01:20.626 _ User requested shutdown...
bionews-redis | 1:M 19 May 2026 13:01:20.626 _ Saving the final RDB snapshot before exiting.
bionews-redis | 1:M 19 May 2026 13:01:20.634 _ DB saved on disk
bionews-redis | 1:M 19 May 2026 13:01:20.635 # Redis is now ready to exit, bye bye...
bionews-redis | 1:C 15 Apr 2026 18:33:02.198 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 15 Apr 2026 18:33:02.199 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 15 Apr 2026 18:33:02.199 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 15 Apr 2026 18:33:02.199 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 15 Apr 2026 18:33:02.202 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 15 Apr 2026 18:33:02.202 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 15 Apr 2026 18:33:02.217 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 15 Apr 2026 18:33:02.218 _ Server initialized
bionews-redis | 1:M 15 Apr 2026 18:33:02.221 _ Loading RDB produced by version 7.4.9
bionews-redis | 1:M 15 Apr 2026 18:33:02.221 _ RDB age 0 seconds
bionews-redis | 1:M 15 Apr 2026 18:33:02.221 _ RDB memory usage when created 0.93 Mb
bionews-redis | 1:M 15 Apr 2026 18:33:02.221 _ Done loading RDB, keys loaded: 0, keys expired: 0.
bionews-redis | 1:M 15 Apr 2026 18:33:02.221 _ DB loaded from disk: 0.003 seconds
bionews-redis | 1:M 15 Apr 2026 18:33:02.221 _ Ready to accept connections tcp
bionews-redis | 1:C 15 Apr 2026 18:33:04.487 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 15 Apr 2026 18:33:04.488 _ oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 15 Apr 2026 18:33:04.488 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 15 Apr 2026 18:33:04.488 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 15 Apr 2026 18:33:04.488 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 15 Apr 2026 18:33:04.488 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 15 Apr 2026 18:33:04.496 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 15 Apr 2026 18:33:04.496 _ Server initialized
bionews-redis | 1:M 15 Apr 2026 18:33:04.499 _ Loading RDB produced by version 7.4.9
bionews-redis | 1:M 15 Apr 2026 18:33:04.499 _ RDB age 0 seconds
bionews-redis | 1:M 15 Apr 2026 18:33:04.499 _ RDB memory usage when created 0.93 Mb
bionews-redis | 1:M 15 Apr 2026 18:33:04.499 _ Done loading RDB, keys loaded: 0, keys expired: 0.
bionews-redis | 1:M 15 Apr 2026 18:33:04.499 _ DB loaded from disk: 0.003 seconds
bionews-redis | 1:M 15 Apr 2026 18:33:04.499 _ Ready to accept connections tcp
bionews-redis | 1:M 19 May 2026 14:04:32.385 _ 1 changes in 3600 seconds. Saving...
bionews-redis | 1:M 19 May 2026 14:04:32.393 _ Background saving started by pid 1704
bionews-redis | 1704:C 19 May 2026 14:04:32.404 _ DB saved on disk
bionews-redis | 1704:C 19 May 2026 14:04:32.405 _ Fork CoW for RDB: current 0 MB, peak 0 MB, average 0 MB
bionews-redis | 1:M 19 May 2026 14:04:32.495 _ Background saving terminated with success
bionews-redis | 1:M 19 May 2026 14:50:02.605 # Possible SECURITY ATTACK detected. It looks like somebody is sending POST or Host: commands to Redis. This is likely due to an attacker attempting to use Cross Protocol Scripting to compromise your Redis instance. Connection from 192.168.1.24:65231 aborted.
bionews-redis | 1:M 19 May 2026 15:04:33.007 _ 1 changes in 3600 seconds. Saving...
bionews-redis | 1:M 19 May 2026 15:04:33.010 _ Background saving started by pid 3844
bionews-redis | 3844:C 19 May 2026 15:04:33.064 _ DB saved on disk
bionews-redis | 3844:C 19 May 2026 15:04:33.064 _ Fork CoW for RDB: current 1 MB, peak 1 MB, average 1 MB
bionews-redis | 1:M 19 May 2026 15:04:33.111 \* Background saving terminated with success
bionews-api | INFO: 127.0.0.1:43006 - "GET /api/health HTTP/1.1" 200 OK
```
