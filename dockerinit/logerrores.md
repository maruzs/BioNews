docker compose logs -f
maru@maru:/opt/BioNews$ docker compose logs -f
bionews-redis | 1:C 18 May 2026 19:05:38.519 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit*memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
bionews-redis | 1:C 18 May 2026 19:05:38.519 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
bionews-redis | 1:C 18 May 2026 19:05:38.519 _ Redis version=7.4.9, bits=64, commit=00000000, modified=0, pid=1, just started
bionews-redis | 1:C 18 May 2026 19:05:38.519 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
bionews-redis | 1:M 18 May 2026 19:05:38.520 _ Increased maximum number of open files to 10032 (it was originally set to 1024).
bionews-redis | 1:M 18 May 2026 19:05:38.520 _ monotonic clock: POSIX clock_gettime
bionews-redis | 1:M 18 May 2026 19:05:38.522 _ Running mode=standalone, port=6379.
bionews-redis | 1:M 18 May 2026 19:05:38.523 \_ Server initialized
bionews-redis | 1:M 18 May 2026 19:05:38.524 * Ready to accept connections tcp
bionews-scheduler | 2026-05-18 15:05:45 [INFO] BioNews Scheduler iniciado.
bionews-scheduler | 2026-05-18 15:05:45 [INFO] Configurando scheduler con parametros: {'snifa_time_1': '16:12', 'snifa_time_2': '14:00', 'pertinencias_interval': '1', 'noticias_interval': 1, 'tribunales_interval': 1, 'notification_interval': 3, 'hora_inicio': '07:00', 'hora_fin': '19:00', 'test_time': '10:34', 'consultas_time_2': '15:50', 'consultas_time_1': '08:31'}
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-gateway | 2026/05/18 19:05:38 [emerg] 1#1: host not found in upstream "bionews-auth-service" in /etc/nginx/conf.d/default.conf:5
bionews-gateway | nginx: [emerg] host not found in upstream "bionews-auth-service" in /etc/nginx/conf.d/default.conf:5
bionews-gateway | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-gateway | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-gateway | 10-listen-on-ipv6-by-default.sh: info: can not modify /etc/nginx/conf.d/default.conf (read-only file system?)
bionews-gateway | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-gateway | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-gateway | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: using the "epoll" event method
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: nginx/1.31.0
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker processes
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 21
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 22
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 23
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 24
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 25
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 26
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 27
bionews-gateway | 2026/05/18 19:05:43 [notice] 1#1: start worker process 28
bionews-gateway | 2026/05/18 19:06:17 [error] 21#21: *1 open() "/etc/nginx/html/stub_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /stub_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:06:17 +0000] "GET /stub_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:06:17 [error] 22#22: *2 open() "/etc/nginx/html/basic_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /basic_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:06:17 +0000] "GET /basic_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:06:17 [error] 23#23: *3 open() "/etc/nginx/html/nginx_status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /nginx_status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:06:17 +0000] "GET /nginx_status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-gateway | 2026/05/18 19:06:17 [error] 24#24: *4 open() "/etc/nginx/html/status" failed (2: No such file or directory), client: 172.20.0.7, server: , request: "GET /status HTTP/1.1", host: "172.20.0.3:8000"
bionews-gateway | 172.20.0.7 - - [18/May/2026:19:06:17 +0000] "GET /status HTTP/1.1" 404 153 "-" "Netdata go.d.plugin/v2.10.0-212-nightly" "-"
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-postgres |
bionews-postgres | PostgreSQL Database directory appears to contain a database; Skipping initialization
bionews-postgres |
bionews-postgres | 2026-05-18 19:05:38.616 UTC [1] LOG: starting PostgreSQL 15.18 on x86_64-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
bionews-postgres | 2026-05-18 19:05:38.616 UTC [1] LOG: listening on IPv4 address "0.0.0.0", port 5432
bionews-postgres | 2026-05-18 19:05:38.616 UTC [1] LOG: listening on IPv6 address "::", port 5432
bionews-postgres | 2026-05-18 19:05:38.620 UTC [1] LOG: listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
bionews-postgres | 2026-05-18 19:05:38.627 UTC [29] LOG: database system was shut down at 2026-05-18 18:59:37 UTC
bionews-postgres | 2026-05-18 19:05:38.636 UTC [1] LOG: database system is ready to accept connections
bionews-consultations-service | return callback(*args, \*\*kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, \*\*kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, \*\*kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, \*\*kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | return self.main(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, \*\*kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, \*\*kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-web | /docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
bionews-web | /docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
bionews-web | 10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
bionews-web | 10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
bionews-web | /docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
bionews-web | /docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-web | /docker-entrypoint.sh: Configuration complete; ready for start up
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: using the "epoll" event method
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: nginx/1.31.0
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0)
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: OS: Linux 7.0.0-15-generic
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1024:524288
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker processes
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 29
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 30
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 31
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 32
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 33
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 34
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 35
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-web | 2026/05/18 19:05:38 [notice] 1#1: start worker process 36
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(*args, **kwargs)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | return ctx.invoke(self.callback, \*\*ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, \*\*kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(\*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(\*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | return callback(*args, \*\*kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, **kwargs)
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(\*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(\*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | run(
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, \*\*kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(\*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | return self.main(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, \*\*kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, \*\*kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(*args, \*\*kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-legal-service | return callback(*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(\*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(\*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(\*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(\*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service | Traceback (most recent call last):
bionews-news-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-news-service | sys.exit(main())
bionews-news-service | ^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-news-service | return self.main(\*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-news-service | rv = self.invoke(ctx)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-news-service | return ctx.invoke(self.callback, **ctx.params)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-news-service | return callback(\*args, **kwargs)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-news-service | run(
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-news-service | server.run()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-news-service | return asyncio.run(self.serve(sockets=sockets))
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-news-service | return runner.run(main)
bionews-news-service | ^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-news-service | return self.\_loop.run_until_complete(task)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-news-service | await self.\_serve(sockets)
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-news-service | config.load()
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-news-service | self.loaded_app = import_from_string(self.app)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-news-service | module = importlib.import_module(module_str)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-news-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-news-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-news-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-news-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-news-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-news-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-news-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-news-service | File "/app/src/services/news/main.py", line 32, in <module>
bionews-news-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-news-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-news-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-news-service | SyntaxError: expected 'except' or 'finally' block
bionews-legal-service | Traceback (most recent call last):
bionews-legal-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-legal-service | sys.exit(main())
bionews-legal-service | ^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-legal-service | return self.main(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-legal-service | rv = self.invoke(ctx)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-legal-service | return ctx.invoke(self.callback, **ctx.params)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-legal-service | return callback(*args, **kwargs)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-legal-service | run(
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-legal-service | server.run()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-legal-service | return asyncio.run(self.serve(sockets=sockets))
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-legal-service | return runner.run(main)
bionews-legal-service | ^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-legal-service | return self.\_loop.run_until_complete(task)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-legal-service | await self.\_serve(sockets)
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-legal-service | config.load()
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-legal-service | self.loaded_app = import_from_string(self.app)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-legal-service | module = importlib.import_module(module_str)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-legal-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-legal-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-legal-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-legal-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-legal-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-legal-service | File "/app/src/services/legal/main.py", line 32, in <module>
bionews-legal-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-legal-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-legal-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-legal-service | SyntaxError: expected 'except' or 'finally' block
bionews-consultations-service | Traceback (most recent call last):
bionews-consultations-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-consultations-service | sys.exit(main())
bionews-consultations-service | ^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-consultations-service | return self.main(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-consultations-service | rv = self.invoke(ctx)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-consultations-service | return ctx.invoke(self.callback, **ctx.params)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-consultations-service | return callback(\*args, **kwargs)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-consultations-service | run(
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-consultations-service | server.run()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-consultations-service | return asyncio.run(self.serve(sockets=sockets))
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-consultations-service | return runner.run(main)
bionews-consultations-service | ^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-consultations-service | return self.\_loop.run_until_complete(task)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-consultations-service | await self.\_serve(sockets)
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-consultations-service | config.load()
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-consultations-service | self.loaded_app = import_from_string(self.app)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-consultations-service | module = importlib.import_module(module_str)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-consultations-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-consultations-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-consultations-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-consultations-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-consultations-service | File "/app/src/services/consultations/main.py", line 32, in <module>
bionews-consultations-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-consultations-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-consultations-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-consultations-service | SyntaxError: expected 'except' or 'finally' block
bionews-auth-service | Traceback (most recent call last):
bionews-auth-service | File "/usr/local/bin/uvicorn", line 8, in <module>
bionews-auth-service | sys.exit(main())
bionews-auth-service | ^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1514, in **call**
bionews-auth-service | return self.main(*args, **kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1435, in main
bionews-auth-service | rv = self.invoke(ctx)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 1298, in invoke
bionews-auth-service | return ctx.invoke(self.callback, **ctx.params)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/click/core.py", line 853, in invoke
bionews-auth-service | return callback(*args, \*\*kwargs)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 413, in main
bionews-auth-service | run(
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/main.py", line 580, in run
bionews-auth-service | server.run()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 66, in run
bionews-auth-service | return asyncio.run(self.serve(sockets=sockets))
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 190, in run
bionews-auth-service | return runner.run(main)
bionews-auth-service | ^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/asyncio/runners.py", line 118, in run
bionews-auth-service | return self.\_loop.run_until_complete(task)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 70, in serve
bionews-auth-service | await self.\_serve(sockets)
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/server.py", line 77, in \_serve
bionews-auth-service | config.load()
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/config.py", line 435, in load
bionews-auth-service | self.loaded_app = import_from_string(self.app)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/site-packages/uvicorn/importer.py", line 19, in import_from_string
bionews-auth-service | module = importlib.import_module(module_str)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "/usr/local/lib/python3.11/importlib/**init**.py", line 126, in import_module
bionews-auth-service | return \_bootstrap.\_gcd_import(name[level:], package, level)
bionews-auth-service | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1204, in \_gcd_import
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1176, in \_find_and_load
bionews-auth-service | File "<frozen importlib._bootstrap>", line 1147, in \_find_and_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap>", line 690, in \_load_unlocked
bionews-auth-service | File "<frozen importlib._bootstrap_external>", line 940, in exec_module
bionews-auth-service | File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
bionews-auth-service | File "/app/src/services/auth/main.py", line 34, in <module>
bionews-auth-service | from src.scrapers.sea_legal import PertinenciasScraper
bionews-auth-service | File "/app/src/scrapers/sea_legal.py", line 106
bionews-auth-service | conn = db_manager.get_connection('bionews_legal_db')
bionews-auth-service | SyntaxError: expected 'except' or 'finally' block
bionews-news-service exited with code 1 (restarting)
bionews-legal-service exited with code 1 (restarting)
bionews-consultations-service exited with code 1 (restarting)
bionews-auth-service exited with code 1 (restarting)

# AQUI ES DESDE QUE FUI AL LOGIN

bionews-web | 172.20.0.2 - - [18/May/2026:19:08:13 +0000] "GET /login HTTP/1.1" 304 0 "http://192.168.1.35:81/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"

bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *23 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *17 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *15 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *25 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *19 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *21 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *27 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *29 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *31 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: *33 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-gateway | 2026/05/18 19:09:26 [error] 21#21: \*13 connect() failed (113: Host is unreachable) while connecting to upstream, client: 172.18.0.5, server: , request: "POST /api/auth/login HTTP/1.1", upstream: "http://172.18.0.8:8001/api/auth/login", host: "prairie-nissan-commonly-arabia.trycloudflare.com", referrer: "https://prairie-nissan-commonly-arabia.trycloudflare.com/login"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-gateway | 172.18.0.5 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1, 172.20.0.2"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
bionews-web | 172.20.0.2 - - [18/May/2026:19:09:26 +0000] "POST /api/auth/login HTTP/1.1" 502 559 "https://prairie-nissan-commonly-arabia.trycloudflare.com/login" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 OPR/131.0.0.0" "2803:c600:7115:a6b9:4167:19e3:e11f:2e18, 172.20.0.1"
