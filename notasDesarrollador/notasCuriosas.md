En sancionatorios hay un problema al filtrar por categoria, y es que aparecen las siguiente opciones:
"Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura / Pesca y Acuicultura"
y de hecho al aplicarlo se muestra un registro (F-002-2015) que tiene eso en la categoria, y en la bd aparece con esa misma categoria

De hecho estoy revisando el filtro de categoria para la tabla de los sancionatorios y hay muchos raros, por ejemplo (los escribire textuales los que estan raros, el resto todo normal):
'/Vivienda e Inmobiliarios' -> Deberia ser 'Vivienda e Inmobiliarios'
'Agroindustrias/Forestal' -> No deberian ser los dos juntos
'Equipamiento/Equipamiento' -> No deberia repetirse
'Forestal/Forestal' -> no deberia repetirse

Ok, me acabo de dar cuenta que esta asi porque asi es como lo encuentras en la pagina oficial, ignoraremos eso. Resulta que al final en la pagina oficial puede haber mas de una categoria ya que puede tener mas de una unidad fiscalizable.
