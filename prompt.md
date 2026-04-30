Ok, lee el codigo y entiende como funciona. Luego quiero que implementemos lo siguiente:

1. Hostear en un servidor propio (es otro computador)
2. Que corra la web y la base de datos en el servidor propio
3. Que se pueda acceder desde cualquier computador con internet a la web usando un navegador (usa tailscale)
4. Que cada dentro de las 7 am y las 7pm cada una hora se ejecuten los scrapers de manera automatica, de momento de forma secuencial y en un tiempo mas implemntaremos de forma paralela
5. Borra el SC que aparece en el header del frontend arriba a la derecha

Pensaba hacerlo con contenedores de docker, actualmente mi servidor (es una laptop headless siempre prendida conectada al router por cable) esta funcionando con ubuntu server, como llevo todo el codigo para alla y lo despliego para poder acceder desde cualquier parte del mundo, desde cualquier dispositivo. Tengo nginx y docker ya instalados en la laptop servidor
