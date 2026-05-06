Quiero que en el panel de administrador haya un apartado especifico que yo le indico una hora y a esa hora en la terminal debe decirme 'Testeo ejecutado a las HH:MM'

Esto ya que configure a las 10:04 que el SNIFA Horario 1 se ejecutara a las 10:06 para ver si en consola me aparecia que se habia iniciado el scrapeo de SNIFA, pero solo me aparecio esto:
INFO: 127.0.0.1:57216 - "GET /api/test/status HTTP/1.1" 200 OK
2026-05-06 10:06:16,428 [INFO] TEST: Se ejecuto el scheduler a las 10:06 (SNIFA 1)
Lo cual no me dice si se ejecuto el scrapeo de SNIFA o no

Ademas borra lo de Polling Notificaciones (Segundos) que ya vi que esta funcionando correctamente.
