1. El scheduler alterable mediante el panel de administrador (la frecuencia, osea cada cuanto tiempo se ejecuta) no esta funcionando correctamente, los cambios no surten efecto. Arreglalo y para probar implementa un boton y api que sea solamente para ver el tiempo que ha pasado entre llamadas. Por ejemplo

- Crea una api que no haga nada mas que mostrar en terminal cuanto tiempo ha pasado desde la ultima llamada
  INFO: 127.0.0.1:59309 - "GET /api/test/status HTTP/1.1" 200 OK -> 0 segundos. (para la primera vez)
- En Configuracion del scheduler agrega un input select que permita elegir entre: 2 segundos, 3 segundos, 5 segundos, 7 segundos y 11 minuto (por defecto 2 segundos)
  INFO: 127.0.0.1:59309 - "GET /api/notifications/status HTTP/1.1" 200 OK -> 2 segundos
  despues de 2 segundos deberia mostrar 4 segundos, y asi sucesivamente.
  Si yo lo cambio a 3 segundos la siguiente ejecucion deberia decir "-> 3 segundos" y asi sucesivamente.
  O algun metodo similar para comprobar que los cambios del scheduler mediante el panel estan funcionando.

Tambien otro metodo tambien en Configuracion del scheduler que sea por hora, es decir que si yo pongo que sea a las 10:05 a las 10:05 deberia aparecer en consola un mensaje que diga 'Se ejecuto el scheduler a las 10:05' y asi dependiendo de la hora que ponga. Esto es solo de prueba y luego lo comentare/borrare para que deje de aparecer.

2. Etiqueta 'Nuevos' no aparece en items nuevos, pero si funciona el puntito rojo del sidebar.
   Desde Admin -> Vi que se actualizaron las noticias por el puntito rojo en el sidebar, pero al entrar no tenia la etiqueta 'Nuevo' ni un borde verde (en la card)
   Desde el perfil de prueba: decidi ir a ver si ahi si aparecia y tampoco
