# LINK
https://www.portaljudicial1ta.cl/sgc-web/inicio.html
# ANALISIS
Es una pagina simple y dinamica, muestra los ultimos ingresos y el Estado diario.
Se puede obtener la info desde un json, pero desde ese json no se logra obtener el link a los detalles
Ese link (aqui un ejemplo) es con este formato https://www.portaljudicial1ta.cl/sgc-web/ver-causa.html?rol=R-156-2026, eso significa que con el rolCausa podemos formar el link correcto a donde tiene que ir
## INFO A OBTENER
Nombre, fecha, rol, tipo de causa, link al detalle
# ESTRUCTURA PAGINA E INFORMACION
```json
{"response":"[{\"caratulaCausa\":\"Comunidad Indígena Colla Tata Inti del Pueblo de Los Loros  con Servicio de Evaluación Ambiental \",\"data\":0,\"fechaIngreso\":\"27/03/2026\",\"idCausa\":\"a4f0c42b-a984-413c-9132-72ac14f22bec\",\"rolCausa\":\"R-156-2026\",\"tipoCausa\":\"Reclamación\"},{\"caratulaCausa\":\"Comunidad Indígena Ancestral Wara QDA. Chañaral Alto y sus quebradas Copiapó-Diego de Almagro con Superintendencia del Medio Ambiente.\",\"data\":0,\"fechaIngreso\":\"23/03/2026\",\"idCausa\":\"f3846c3e-d54e-4323-a55d-4204a5a3fc27\",\"rolCausa\":\"R-155-2026\",\"tipoCausa\":\"Reclamación\"},{\"caratulaCausa\":\"Sara Larraín y otros con Servicio de Evaluación Ambiental \",\"data\":0,\"fechaIngreso\":\"03/03/2026\",\"idCausa\":\"f886a7a8-8260-4f02-9c68-234fe0c53942\",\"rolCausa\":\"R-154-2026\",\"tipoCausa\":\"Reclamación\"},{\"caratulaCausa\":\"Manuel Jesús Carvajal Donoso y otro con Servicio de Evaluación Ambiental \",\"data\":0,\"fechaIngreso\":\"03/03/2026\",\"idCausa\":\"0e653232-1870-49df-8a18-e7a63360572c\",\"rolCausa\":\"R-153-2026\",\"tipoCausa\":\"Reclamación\"},{\"caratulaCausa\":\"Andes Iron con Servicio de Evaluación Ambiental\",\"data\":0,\"fechaIngreso\":\"27/02/2026\",\"idCausa\":\"9d2081e5-23e5-44c6-bc53-8f2c529d13c8\",\"rolCausa\":\"R-152-2026\",\"tipoCausa\":\"Reclamación\"}]","status":"200"}
```