## En servidor
No se que significa eso, supongo que todo esta bien ahora.
```
maru@maru:/opt/BioNews$ docker exec -it bionews-db env PGPASSWORD=changeme psql -U bionews -d bionews -c 'ALTER USER bionews WITH PASSWORD '\''CambiameBionews2026!'\'';'
ALTER ROLE
```

## En el PC de desarrollo:
```bash
Obteniendo total de registros de Fiscalizaciones...
Total de registros a descargar: 49966
Descargando lote desde el registro 0 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 500/49966)
Descargando lote desde el registro 500 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 1000/49966)
Descargando lote desde el registro 1000 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 1500/49966)
Descargando lote desde el registro 1500 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 2000/49966)
Descargando lote desde el registro 2000 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 2500/49966)
Descargando lote desde el registro 2500 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 3000/49966)
Descargando lote desde el registro 3000 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 3500/49966)
Descargando lote desde el registro 3500 (lote de 500)...
  -> Descargados 500 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 4000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 4500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 5000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 5500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 6000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 6500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 7000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 7500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 8000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 8500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 9000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 9500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 10000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 10500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 11000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 11500 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 12000 (lote de 500)...
  -> Descargados 0 registros (Total acumulado: 4000/49966)
Descargando lote desde el registro 12500 (lote de 500)...
```
La verdad prefiero dejarlo hasta ahi, aparentemente no funciona para construir la bd, se demora un monton y le exije demasiado. Si me interesa eso si que al menos para el scraper snifa.py funcione siempre mediante request.

## Logs en el servidor
```bash
maru@maru:/opt/BioNews$ docker compose logs postgres-db
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-05-19 00:51:22.433 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-05-19 00:51:22.433 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-05-19 00:51:22.433 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-05-19 00:51:22.438 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-05-19 00:51:22.450 UTC [29] LOG:  database system was shut down at 2026-05-19 00:50:48 UTC
bionews-db  | 2026-05-19 00:51:22.466 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 00:51:34.392 UTC [40] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 00:51:34.392 UTC [40] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 00:56:22.543 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 00:56:22.752 UTC [27] LOG:  checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.107 s, sync=0.011 s, total=0.209 s; sync files=3, longest=0.008 s, average=0.004 s; distance=2 kB, estimate=2 kB; lsn=0/31840F8, redo lsn=0/31840C0
bionews-db  | 2026-05-19 01:01:22.815 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 01:01:23.450 UTC [27] LOG:  checkpoint complete: wrote 7 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.605 s, sync=0.012 s, total=0.635 s; sync files=7, longest=0.009 s, average=0.002 s; distance=13 kB, estimate=13 kB; lsn=0/31875A8, redo lsn=0/3187570
bionews-db  | 2026-05-19 10:51:32.883 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 10:51:33.213 UTC [27] LOG:  checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.305 s, sync=0.009 s, total=0.330 s; sync files=4, longest=0.008 s, average=0.003 s; distance=9 kB, estimate=12 kB; lsn=0/3189A00, redo lsn=0/31899C8
bionews-db  | 2026-05-19 11:00:10.313 UTC [27197] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 11:00:10.313 UTC [27197] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 11:01:32.413 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 11:01:32.920 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.012 s, total=0.507 s; sync files=5, longest=0.009 s, average=0.003 s; distance=17 kB, estimate=17 kB; lsn=0/318E150, redo lsn=0/318E118
bionews-db  | 2026-05-19 11:06:32.955 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 11:06:34.535 UTC [27] LOG:  checkpoint complete: wrote 15 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.486 s, sync=0.006 s, total=1.581 s; sync files=9, longest=0.003 s, average=0.001 s; distance=79 kB, estimate=79 kB; lsn=0/31A1E38, redo lsn=0/31A1E00
bionews-db  | 2026-05-19 11:11:32.615 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 11:11:33.118 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.009 s, total=0.503 s; sync files=5, longest=0.008 s, average=0.002 s; distance=17 kB, estimate=73 kB; lsn=0/31A6558, redo lsn=0/31A6520
bionews-db  | 2026-05-19 11:16:32.219 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 11:16:32.824 UTC [27] LOG:  checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.506 s, sync=0.011 s, total=0.605 s; sync files=5, longest=0.009 s, average=0.003 s; distance=29 kB, estimate=68 kB; lsn=0/31ADA00, redo lsn=0/31AD9C8
bionews-db  | 2026-05-19 11:21:32.858 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 11:21:33.361 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.404 s, sync=0.010 s, total=0.503 s; sync files=5, longest=0.009 s, average=0.002 s; distance=11 kB, estimate=62 kB; lsn=0/31B0650, redo lsn=0/31B0618
bionews-db  | 2026-05-19 11:51:00.048 UTC [1] LOG:  received fast shutdown request
bionews-db  | 2026-05-19 11:51:00.059 UTC [1] LOG:  aborting any active transactions
bionews-db  | 2026-05-19 11:51:00.059 UTC [27199] FATAL:  terminating connection due to administrator command
bionews-db  | 2026-05-19 11:51:00.059 UTC [27198] FATAL:  terminating connection due to administrator command
bionews-db  | 2026-05-19 11:51:00.064 UTC [88] FATAL:  terminating connection due to administrator command
bionews-db  | 2026-05-19 11:51:00.069 UTC [41] FATAL:  terminating connection due to administrator command
bionews-db  | 2026-05-19 11:51:00.073 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited with exit code 1
bionews-db  | 2026-05-19 11:51:00.076 UTC [27] LOG:  shutting down
bionews-db  | 2026-05-19 11:51:00.087 UTC [27] LOG:  checkpoint starting: shutdown immediate
bionews-db  | 2026-05-19 11:51:00.284 UTC [27] LOG:  checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.083 s, sync=0.027 s, total=0.209 s; sync files=4, longest=0.013 s, average=0.007 s; distance=0 kB, estimate=56 kB; lsn=0/31B0700, redo lsn=0/31B0700
bionews-db  | 2026-05-19 11:51:00.346 UTC [1] LOG:  database system is shut down
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-04-15 18:33:02.768 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-04-15 18:33:02.768 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-04-15 18:33:02.768 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-04-15 18:33:02.780 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-04-15 18:33:02.795 UTC [28] LOG:  database system was shut down at 2026-05-19 11:51:00 UTC
bionews-db  | 2026-04-15 18:33:02.819 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 12:44:46.840 UTC [99] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 12:44:46.840 UTC [99] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 12:45:16.220 UTC [1] LOG:  received fast shutdown request
bionews-db  | 2026-05-19 12:45:16.252 UTC [1] LOG:  aborting any active transactions
bionews-db  | 2026-05-19 12:45:16.252 UTC [101] FATAL:  terminating connection due to administrator command
bionews-db  | 2026-05-19 12:45:16.254 UTC [100] FATAL:  terminating connection due to administrator command
bionews-db  | 2026-05-19 12:45:16.261 UTC [1] LOG:  background worker "logical replication launcher" (PID 31) exited with exit code 1
bionews-db  | 2026-05-19 12:45:16.269 UTC [26] LOG:  shutting down
bionews-db  | 2026-05-19 12:45:16.288 UTC [26] LOG:  checkpoint starting: shutdown immediate
bionews-db  | 2026-05-19 12:45:16.343 UTC [26] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.020 s, sync=0.005 s, total=0.074 s; sync files=2, longest=0.003 s, average=0.003 s; distance=0 kB, estimate=0 kB; lsn=0/31B07B0, redo lsn=0/31B07B0
bionews-db  | 2026-05-19 12:45:16.387 UTC [1] LOG:  database system is shut down
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-05-19 12:53:38.656 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-05-19 12:53:38.657 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-05-19 12:53:38.657 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-05-19 12:53:38.667 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-05-19 12:53:38.682 UTC [29] LOG:  database system was shut down at 2026-05-19 12:45:16 UTC
bionews-db  | 2026-05-19 12:53:38.709 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 12:54:38.224 UTC [1] LOG:  received fast shutdown request
bionews-db  | 2026-05-19 12:54:38.227 UTC [1] LOG:  aborting any active transactions
bionews-db  | 2026-05-19 12:54:38.243 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited with exit code 1
bionews-db  | 2026-05-19 12:54:38.248 UTC [27] LOG:  shutting down
bionews-db  | 2026-05-19 12:54:38.251 UTC [27] LOG:  checkpoint starting: shutdown immediate
bionews-db  | 2026-05-19 12:54:38.316 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.024 s, sync=0.003 s, total=0.069 s; sync files=2, longest=0.002 s, average=0.002 s; distance=0 kB, estimate=0 kB; lsn=0/31B0860, redo lsn=0/31B0860
bionews-db  | 2026-05-19 12:54:38.325 UTC [1] LOG:  database system is shut down
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-05-19 12:57:03.992 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-05-19 12:57:03.992 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-05-19 12:57:03.992 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-05-19 12:57:04.001 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-05-19 12:57:04.015 UTC [29] LOG:  database system was shut down at 2026-05-19 12:54:38 UTC
bionews-db  | 2026-05-19 12:57:04.057 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 12:58:46.976 UTC [1] LOG:  received fast shutdown request
bionews-db  | 2026-05-19 12:58:46.980 UTC [1] LOG:  aborting any active transactions
bionews-db  | 2026-05-19 12:58:47.024 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited with exit code 1
bionews-db  | 2026-05-19 12:58:47.025 UTC [27] LOG:  shutting down
bionews-db  | 2026-05-19 12:58:47.030 UTC [27] LOG:  checkpoint starting: shutdown immediate
bionews-db  | 2026-05-19 12:58:47.059 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.007 s, sync=0.005 s, total=0.035 s; sync files=2, longest=0.004 s, average=0.003 s; distance=0 kB, estimate=0 kB; lsn=0/31B0910, redo lsn=0/31B0910
bionews-db  | 2026-05-19 12:58:47.076 UTC [1] LOG:  database system is shut down
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-05-19 12:59:44.113 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-05-19 12:59:44.113 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-05-19 12:59:44.113 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-05-19 12:59:44.120 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-05-19 12:59:44.132 UTC [30] LOG:  database system was shut down at 2026-05-19 12:58:47 UTC
bionews-db  | 2026-05-19 12:59:44.151 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 13:01:20.538 UTC [1] LOG:  received fast shutdown request
bionews-db  | 2026-05-19 13:01:20.540 UTC [1] LOG:  aborting any active transactions
bionews-db  | 2026-05-19 13:01:20.549 UTC [1] LOG:  background worker "logical replication launcher" (PID 33) exited with exit code 1
bionews-db  | 2026-05-19 13:01:20.551 UTC [28] LOG:  shutting down
bionews-db  | 2026-05-19 13:01:20.554 UTC [28] LOG:  checkpoint starting: shutdown immediate
bionews-db  | 2026-05-19 13:01:20.600 UTC [28] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.018 s, sync=0.004 s, total=0.049 s; sync files=2, longest=0.003 s, average=0.002 s; distance=0 kB, estimate=0 kB; lsn=0/31B09C0, redo lsn=0/31B09C0
bionews-db  | 2026-05-19 13:01:20.613 UTC [1] LOG:  database system is shut down
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-04-15 18:33:02.603 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-04-15 18:33:02.603 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-04-15 18:33:02.603 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-04-15 18:33:02.608 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-04-15 18:33:02.619 UTC [29] LOG:  database system was shut down at 2026-05-19 13:01:20 UTC
bionews-db  | 2026-04-15 18:33:02.638 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 13:15:30.840 UTC [56] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 13:15:30.840 UTC [56] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  |
bionews-db  | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-db  |
bionews-db  | 2026-04-15 18:33:04.835 UTC [1] LOG:  starting PostgreSQL 16.13 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-db  | 2026-04-15 18:33:04.835 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
bionews-db  | 2026-04-15 18:33:04.835 UTC [1] LOG:  listening on IPv6 address "::", port 5432
bionews-db  | 2026-04-15 18:33:04.843 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-db  | 2026-04-15 18:33:04.852 UTC [29] LOG:  database system was interrupted; last known up at 2026-04-15 18:33:02 UTC
bionews-db  | 2026-04-15 18:33:05.503 UTC [29] LOG:  database system was not properly shut down; automatic recovery in progress
bionews-db  | 2026-04-15 18:33:05.515 UTC [29] LOG:  redo starts at 0/31B0A38
bionews-db  | 2026-04-15 18:33:05.515 UTC [29] LOG:  invalid record length at 0/31B0A70: expected at least 24, got 0
bionews-db  | 2026-04-15 18:33:05.515 UTC [29] LOG:  redo done at 0/31B0A38 system usage: CPU: user: 0.00 s, system: 0.00 s, elapsed: 0.00 s
bionews-db  | 2026-04-15 18:33:05.530 UTC [27] LOG:  checkpoint starting: end-of-recovery immediate wait
bionews-db  | 2026-04-15 18:33:05.566 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.016 s, sync=0.003 s, total=0.039 s; sync files=2, longest=0.002 s, average=0.002 s; distance=0 kB, estimate=0 kB; lsn=0/31B0A70, redo lsn=0/31B0A70
bionews-db  | 2026-04-15 18:33:05.581 UTC [1] LOG:  database system is ready to accept connections
bionews-db  | 2026-05-19 13:17:51.523 UTC [53] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 13:17:51.523 UTC [53] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 13:22:21.092 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 13:22:26.051 UTC [27] LOG:  checkpoint complete: wrote 50 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.926 s, sync=0.015 s, total=4.959 s; sync files=27, longest=0.011 s, average=0.001 s; distance=387 kB, estimate=387 kB; lsn=0/3222940, redo lsn=0/3211840
bionews-db  | 2026-05-19 14:01:17.138 UTC [1903] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 14:01:17.138 UTC [1903] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 14:05:21.708 UTC [2086] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 14:05:21.708 UTC [2086] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 14:07:21.866 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 14:07:23.075 UTC [27] LOG:  checkpoint complete: wrote 12 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.115 s, sync=0.005 s, total=1.210 s; sync files=11, longest=0.003 s, average=0.001 s; distance=80 kB, estimate=356 kB; lsn=0/3225940, redo lsn=0/3225908
bionews-db  | 2026-05-19 14:12:21.174 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 14:12:21.401 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.203 s, sync=0.010 s, total=0.227 s; sync files=3, longest=0.009 s, average=0.004 s; distance=7 kB, estimate=321 kB; lsn=0/3227908, redo lsn=0/32278D0
bionews-db  | 2026-05-19 14:17:21.501 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 14:17:22.026 UTC [27] LOG:  checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.506 s, sync=0.009 s, total=0.525 s; sync files=5, longest=0.008 s, average=0.002 s; distance=30 kB, estimate=292 kB; lsn=0/322F338, redo lsn=0/322F300
bionews-db  | 2026-05-19 14:22:21.125 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 14:22:21.560 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.011 s, total=0.435 s; sync files=5, longest=0.009 s, average=0.003 s; distance=27 kB, estimate=266 kB; lsn=0/3236200, redo lsn=0/32361C8
bionews-db  | 2026-05-19 14:57:22.100 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 14:57:22.691 UTC [27] LOG:  checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.507 s, sync=0.012 s, total=0.592 s; sync files=6, longest=0.008 s, average=0.002 s; distance=11 kB, estimate=240 kB; lsn=0/3238F60, redo lsn=0/3238F28
bionews-db  | 2026-05-19 15:02:22.728 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:02:24.273 UTC [27] LOG:  checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.520 s, sync=0.008 s, total=1.546 s; sync files=16, longest=0.003 s, average=0.001 s; distance=50 kB, estimate=221 kB; lsn=0/3245A00, redo lsn=0/32459C8
bionews-db  | 2026-05-19 15:07:22.374 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:07:23.792 UTC [27] LOG:  checkpoint complete: wrote 14 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.320 s, sync=0.008 s, total=1.419 s; sync files=14, longest=0.003 s, average=0.001 s; distance=16 kB, estimate=201 kB; lsn=0/3249C70, redo lsn=0/3249C38
bionews-db  | 2026-05-19 15:17:22.994 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:17:23.604 UTC [27] LOG:  checkpoint complete: wrote 6 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.507 s, sync=0.012 s, total=0.610 s; sync files=5, longest=0.008 s, average=0.003 s; distance=31 kB, estimate=184 kB; lsn=0/32518E0, redo lsn=0/32518A8
bionews-db  | 2026-05-19 15:22:22.704 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:22:24.118 UTC [27] LOG:  checkpoint complete: wrote 14 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.311 s, sync=0.011 s, total=1.414 s; sync files=11, longest=0.008 s, average=0.001 s; distance=74 kB, estimate=173 kB; lsn=0/32643D8, redo lsn=0/32643A0
bionews-db  | 2026-05-19 15:27:46.397 UTC [5603] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 15:27:46.397 UTC [5603] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:27:52.462 UTC [5604] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 15:27:52.462 UTC [5604] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:27:52.578 UTC [5606] FATAL:  password authentication failed for user "postgres"
bionews-db  | 2026-05-19 15:27:52.578 UTC [5606] DETAIL:  Role "postgres" does not exist.
bionews-db  |   Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:27:52.610 UTC [5607] FATAL:  password authentication failed for user "postgres"
bionews-db  | 2026-05-19 15:27:52.610 UTC [5607] DETAIL:  Role "postgres" does not exist.
bionews-db  |   Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:27:52.641 UTC [5608] FATAL:  password authentication failed for user "postgres"
bionews-db  | 2026-05-19 15:27:52.641 UTC [5608] DETAIL:  Role "postgres" does not exist.
bionews-db  |   Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:27:52.673 UTC [5609] FATAL:  password authentication failed for user "postgres"
bionews-db  | 2026-05-19 15:27:52.673 UTC [5609] DETAIL:  Role "postgres" does not exist.
bionews-db  |   Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:27:52.706 UTC [5610] FATAL:  password authentication failed for user "postgres"
bionews-db  | 2026-05-19 15:27:52.706 UTC [5610] DETAIL:  Role "postgres" does not exist.
bionews-db  |   Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:28:31.140 UTC [5641] ERROR:  relation "Tribunales" does not exist at character 21
bionews-db  | 2026-05-19 15:28:31.140 UTC [5641] STATEMENT:  SELECT "Fecha" FROM "Tribunales" WHERE "Fecha" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:28:31.141 UTC [5641] ERROR:  relation "pertinencias" does not exist at character 21
bionews-db  | 2026-05-19 15:28:31.141 UTC [5641] STATEMENT:  SELECT "Fecha" FROM "pertinencias" WHERE "Fecha" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:28:31.143 UTC [5641] ERROR:  relation "sea_proyectos_evaluados" does not exist at character 34
bionews-db  | 2026-05-19 15:28:31.143 UTC [5641] STATEMENT:  SELECT "fecha_presentacion" FROM "sea_proyectos_evaluados" WHERE "fecha_presentacion" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:28:31.145 UTC [5641] ERROR:  relation "minsal_vigentes" does not exist at character 28
bionews-db  | 2026-05-19 15:28:31.145 UTC [5641] STATEMENT:  SELECT "fecha_inicio" FROM "minsal_vigentes" WHERE "fecha_inicio" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:28:31.146 UTC [5641] ERROR:  relation "mma_abiertas" does not exist at character 28
bionews-db  | 2026-05-19 15:28:31.146 UTC [5641] STATEMENT:  SELECT "fecha_inicio" FROM "mma_abiertas" WHERE "fecha_inicio" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:28:31.148 UTC [5641] ERROR:  relation "normativas" does not exist at character 21
bionews-db  | 2026-05-19 15:28:31.148 UTC [5641] STATEMENT:  SELECT "fecha" FROM "normativas" WHERE "fecha" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:28:31.150 UTC [5641] ERROR:  relation "noticias" does not exist at character 21
bionews-db  | 2026-05-19 15:28:31.150 UTC [5641] STATEMENT:  SELECT "fecha" FROM "noticias" WHERE "fecha" IS NOT NULL LIMIT 5
bionews-db  | 2026-05-19 15:33:30.078 UTC [5858] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 15:33:30.078 UTC [5858] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:39:57.933 UTC [6133] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 15:39:57.933 UTC [6133] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 15:42:22.421 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:42:24.112 UTC [27] LOG:  checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.594 s, sync=0.008 s, total=1.692 s; sync files=15, longest=0.003 s, average=0.001 s; distance=20 kB, estimate=157 kB; lsn=0/32695B0, redo lsn=0/3269578
bionews-db  | 2026-05-19 15:47:22.156 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:47:22.966 UTC [27] LOG:  checkpoint complete: wrote 8 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.707 s, sync=0.012 s, total=0.811 s; sync files=8, longest=0.009 s, average=0.002 s; distance=20 kB, estimate=144 kB; lsn=0/326E6F8, redo lsn=0/326E6C0
bionews-db  | 2026-05-19 15:52:23.055 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:52:24.670 UTC [27] LOG:  checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.592 s, sync=0.006 s, total=1.616 s; sync files=9, longest=0.003 s, average=0.001 s; distance=60 kB, estimate=135 kB; lsn=0/327DA00, redo lsn=0/327D9C8
bionews-db  | 2026-05-19 15:57:23.754 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 15:57:24.059 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.010 s, total=0.306 s; sync files=3, longest=0.009 s, average=0.004 s; distance=7 kB, estimate=123 kB; lsn=0/327F708, redo lsn=0/327F6D0
bionews-db  | 2026-05-19 16:02:23.160 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:02:23.489 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.011 s, total=0.329 s; sync files=3, longest=0.010 s, average=0.004 s; distance=6 kB, estimate=111 kB; lsn=0/32810C0, redo lsn=0/3281088
bionews-db  | 2026-05-19 16:05:02.903 UTC [7206] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 16:05:02.903 UTC [7206] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 16:12:23.649 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:12:24.562 UTC [27] LOG:  checkpoint complete: wrote 9 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.810 s, sync=0.012 s, total=0.914 s; sync files=9, longest=0.010 s, average=0.002 s; distance=26 kB, estimate=102 kB; lsn=0/3287C00, redo lsn=0/3287BC8
bionews-db  | 2026-05-19 16:17:23.628 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:17:28.451 UTC [27] LOG:  checkpoint complete: wrote 48 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=4.717 s, sync=0.016 s, total=4.824 s; sync files=27, longest=0.009 s, average=0.001 s; distance=279 kB, estimate=279 kB; lsn=0/32CD8C8, redo lsn=0/32CD890
bionews-db  | 2026-05-19 16:22:23.550 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:22:25.239 UTC [27] LOG:  checkpoint complete: wrote 16 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.592 s, sync=0.007 s, total=1.689 s; sync files=14, longest=0.003 s, average=0.001 s; distance=86 kB, estimate=259 kB; lsn=0/32E30E8, redo lsn=0/32E30B0
bionews-db  | 2026-05-19 16:27:23.340 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:27:23.845 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.011 s, total=0.506 s; sync files=5, longest=0.009 s, average=0.003 s; distance=16 kB, estimate=235 kB; lsn=0/32E72A8, redo lsn=0/32E7270
bionews-db  | 2026-05-19 16:32:23.946 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:32:25.175 UTC [27] LOG:  checkpoint complete: wrote 12 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.111 s, sync=0.085 s, total=1.230 s; sync files=8, longest=0.083 s, average=0.011 s; distance=44 kB, estimate=216 kB; lsn=0/32F24D0, redo lsn=0/32F2498
bionews-db  | 2026-05-19 16:42:23.227 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:42:23.461 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.011 s, total=0.235 s; sync files=3, longest=0.009 s, average=0.004 s; distance=10 kB, estimate=195 kB; lsn=0/32F4D68, redo lsn=0/32F4D30
bionews-db  | 2026-05-19 16:50:25.881 UTC [9138] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 16:50:25.881 UTC [9138] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 16:52:23.650 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:52:24.766 UTC [27] LOG:  checkpoint complete: wrote 11 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.017 s, sync=0.007 s, total=1.116 s; sync files=9, longest=0.005 s, average=0.001 s; distance=43 kB, estimate=180 kB; lsn=0/32FFA38, redo lsn=0/32FFA00
bionews-db  | 2026-05-19 16:57:23.790 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 16:57:25.000 UTC [27] LOG:  checkpoint complete: wrote 12 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.111 s, sync=0.007 s, total=1.210 s; sync files=10, longest=0.003 s, average=0.001 s; distance=35 kB, estimate=166 kB; lsn=0/33088A8, redo lsn=0/3308838
bionews-db  | 2026-05-19 17:02:23.092 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 17:02:24.682 UTC [27] LOG:  checkpoint complete: wrote 15 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.493 s, sync=0.007 s, total=1.590 s; sync files=13, longest=0.004 s, average=0.001 s; distance=72 kB, estimate=156 kB; lsn=0/331ABE8, redo lsn=0/331ABB0
bionews-db  | 2026-05-19 17:05:00.870 UTC [9771] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 17:05:00.870 UTC [9771] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 17:07:23.700 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 17:07:24.609 UTC [27] LOG:  checkpoint complete: wrote 9 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.809 s, sync=0.011 s, total=0.909 s; sync files=7, longest=0.010 s, average=0.002 s; distance=43 kB, estimate=145 kB; lsn=0/3325A20, redo lsn=0/33259E8
bionews-db  | 2026-05-19 17:12:23.676 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 17:12:25.162 UTC [27] LOG:  checkpoint complete: wrote 14 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=1.391 s, sync=0.008 s, total=1.487 s; sync files=13, longest=0.003 s, average=0.001 s; distance=52 kB, estimate=136 kB; lsn=0/3332CF0, redo lsn=0/3332CB8
bionews-db  | 2026-05-19 17:19:01.314 UTC [10368] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 17:19:01.314 UTC [10368] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 17:20:06.639 UTC [10422] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 17:20:06.639 UTC [10422] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 17:22:23.293 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 17:22:25.690 UTC [27] LOG:  checkpoint complete: wrote 23 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=2.298 s, sync=0.010 s, total=2.398 s; sync files=21, longest=0.004 s, average=0.001 s; distance=111 kB, estimate=133 kB; lsn=0/334E9B0, redo lsn=0/334E978
bionews-db  | 2026-05-19 17:32:23.872 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 17:32:24.581 UTC [27] LOG:  checkpoint complete: wrote 7 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.608 s, sync=0.011 s, total=0.709 s; sync files=4, longest=0.010 s, average=0.003 s; distance=28 kB, estimate=123 kB; lsn=0/3355D88, redo lsn=0/3355D50
bionews-db  | 2026-05-19 17:37:23.681 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 17:37:26.778 UTC [27] LOG:  checkpoint complete: wrote 30 buffers (0.2%); 0 WAL file(s) added, 0 removed, 0 recycled; write=3.003 s, sync=0.006 s, total=3.097 s; sync files=16, longest=0.003 s, average=0.001 s; distance=190 kB, estimate=190 kB; lsn=0/3385918, redo lsn=0/33858E0
bionews-db  | 2026-05-19 17:57:36.267 UTC [12020] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 17:57:36.267 UTC [12020] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 18:00:11.651 UTC [12137] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 18:00:11.651 UTC [12137] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 18:02:24.165 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 18:02:29.686 UTC [27] LOG:  checkpoint complete: wrote 54 buffers (0.3%); 0 WAL file(s) added, 0 removed, 0 recycled; write=5.427 s, sync=0.008 s, total=5.522 s; sync files=28, longest=0.002 s, average=0.001 s; distance=301 kB, estimate=301 kB; lsn=0/33D1000, redo lsn=0/33D0FC8
bionews-db  | 2026-05-19 18:22:24.951 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 18:22:25.454 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.010 s, total=0.504 s; sync files=5, longest=0.009 s, average=0.002 s; distance=27 kB, estimate=274 kB; lsn=0/33D7DF0, redo lsn=0/33D7DB8
bionews-db  | 2026-05-19 19:17:25.192 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 19:17:25.625 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.405 s, sync=0.011 s, total=0.434 s; sync files=5, longest=0.009 s, average=0.003 s; distance=26 kB, estimate=249 kB; lsn=0/33DE828, redo lsn=0/33DE7F0
bionews-db  | 2026-05-19 19:22:25.716 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 19:22:26.222 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.011 s, total=0.506 s; sync files=5, longest=0.010 s, average=0.003 s; distance=28 kB, estimate=227 kB; lsn=0/33E5978, redo lsn=0/33E5940
bionews-db  | 2026-05-19 19:32:25.343 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 19:32:29.052 UTC [27] LOG:  checkpoint complete: wrote 36 buffers (0.2%); 0 WAL file(s) added, 0 removed, 0 recycled; write=3.607 s, sync=0.014 s, total=3.709 s; sync files=19, longest=0.009 s, average=0.001 s; distance=205 kB, estimate=225 kB; lsn=0/3419098, redo lsn=0/3419060
bionews-db  | 2026-05-19 20:12:12.505 UTC [17758] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 20:12:12.505 UTC [17758] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 20:12:25.746 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 20:12:26.258 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.010 s, total=0.513 s; sync files=5, longest=0.009 s, average=0.002 s; distance=20 kB, estimate=204 kB; lsn=0/341E0F8, redo lsn=0/341E0C0
bionews-db  | 2026-05-19 20:15:24.845 UTC [17896] FATAL:  password authentication failed for user "bionews"
bionews-db  | 2026-05-19 20:15:24.845 UTC [17896] DETAIL:  Connection matched file "/var/lib/postgresql/data/pg_hba.conf" line 128: "host all all all scram-sha-256"
bionews-db  | 2026-05-19 20:17:25.359 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 20:17:27.556 UTC [27] LOG:  checkpoint complete: wrote 21 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=2.098 s, sync=0.008 s, total=2.197 s; sync files=18, longest=0.003 s, average=0.001 s; distance=59 kB, estimate=190 kB; lsn=0/342D078, redo lsn=0/342D040
bionews-db  | 2026-05-19 20:22:25.657 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 20:22:26.165 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.011 s, total=0.509 s; sync files=5, longest=0.009 s, average=0.003 s; distance=29 kB, estimate=174 kB; lsn=0/3434548, redo lsn=0/3434510
bionews-db  | 2026-05-19 20:27:25.264 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 20:27:25.664 UTC [27] LOG:  checkpoint complete: wrote 4 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.304 s, sync=0.011 s, total=0.400 s; sync files=4, longest=0.009 s, average=0.003 s; distance=14 kB, estimate=158 kB; lsn=0/3437D80, redo lsn=0/3437D48
bionews-db  | 2026-05-19 21:17:26.456 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 21:17:27.469 UTC [27] LOG:  checkpoint complete: wrote 10 buffers (0.1%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.916 s, sync=0.006 s, total=1.013 s; sync files=8, longest=0.003 s, average=0.001 s; distance=33 kB, estimate=145 kB; lsn=0/3440420, redo lsn=0/34403E8
bionews-db  | 2026-05-19 21:22:26.570 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 21:22:27.073 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.010 s, total=0.504 s; sync files=5, longest=0.008 s, average=0.002 s; distance=30 kB, estimate=134 kB; lsn=0/3447CA8, redo lsn=0/3447C70
bionews-db  | 2026-05-19 21:27:26.109 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 21:27:26.412 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.011 s, total=0.304 s; sync files=3, longest=0.009 s, average=0.004 s; distance=7 kB, estimate=121 kB; lsn=0/3449930, redo lsn=0/34498F8
bionews-db  | 2026-05-19 21:37:26.515 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 21:37:27.021 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.407 s, sync=0.011 s, total=0.507 s; sync files=5, longest=0.009 s, average=0.003 s; distance=7 kB, estimate=110 kB; lsn=0/344B6A8, redo lsn=0/344B670
bionews-db  | 2026-05-19 22:02:26.419 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 22:02:26.651 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.011 s, total=0.232 s; sync files=3, longest=0.010 s, average=0.004 s; distance=7 kB, estimate=99 kB; lsn=0/344D3E0, redo lsn=0/344D3A8
bionews-db  | 2026-05-19 22:12:26.851 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 22:12:27.157 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.205 s, sync=0.011 s, total=0.307 s; sync files=3, longest=0.009 s, average=0.004 s; distance=2 kB, estimate=90 kB; lsn=0/344DF68, redo lsn=0/344DF30
bionews-db  | 2026-05-19 22:17:26.218 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 22:17:26.927 UTC [27] LOG:  checkpoint complete: wrote 7 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.607 s, sync=0.012 s, total=0.710 s; sync files=7, longest=0.010 s, average=0.002 s; distance=31 kB, estimate=84 kB; lsn=0/3455B70, redo lsn=0/3455B38
bionews-db  | 2026-05-19 22:22:26.932 UTC [27] LOG:  checkpoint starting: time
bionews-db  | 2026-05-19 22:22:27.365 UTC [27] LOG:  checkpoint complete: wrote 5 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.406 s, sync=0.011 s, total=0.434 s; sync files=5, longest=0.009 s, average=0.003 s; distance=27 kB, estimate=78 kB; lsn=0/345C8E0, redo lsn=0/345C8A8
maru@maru:/opt/BioNews$
```

Recuerda que puedes acceder al servidor mediante ssh si lo deseas, pero no puedes desplegar nada ni hacer git pull, solo ver logs.
ssh maru@192.168.1.35
Memr2026.
el proyecto esta en /opt/BioNews


Como dato para el scraper de sancionatorios:
A veces puede fallar el ObtenerResultadosGrid y dar el error NS_BINDING_ABORTED
La pagina lo intentara nuevamente pero puede demorar, no se si aqui realmente importa al hacerlo directamente con requests pero lo informo por si acaso.

Ejecute los scrapers y esta casi todo perfecto.
Para los sancionatorios si filtro por 2026 en mi pagina tengo 81, pero en la pagina oficial hay 82
Para las fiscalizaciones si filtro por 2026 (que siempre hay que filtrar por DFZ-anio_actual) tengo 727 pero en la pagina son 732. Tal vez alguno se repite o no estan los que faltan dentro de los 10 mas nuevos que obtenemos con el POST
