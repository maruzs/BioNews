categoria economica y tipo deberian ser dropdowns
Borrar tipo_proyecto en las cards de Proyectos Evaluados ya que siempre dira "No especificado"

Quiero que el apartado de filtros y barra de busqueda de 'Proyectos evaluados' sea el formato para todos

## INSTRUCCIONES OBLIGATORIAS

No tienes acceso a la carpeta notasDesarrollador/, no intentes acceder a ella.
No toques cosas que no debas tocar.
No leas analisisEjecucion.md, esa carpeta es solo para mi investigacion.

En Proyectos Evaluados SEA al ver los filtros avanzados no quiero que activamente se cambien al seleccionar algo en un dropdown por ejemplo, quiero que sea cuando le das click a un boton al igual que al resto de paginas. Es decir quiero que

1. Quites el boton 'restablecer' en todas las categorias

2. Implementes un boton 'limpiar filtros' y 'aplicar filtros' en 'Proyectos evaluados' asi como todas las otras categorias lo tienen

3. Noticias recientes deberia desplegar su lista de organismos hacia el lado, actualmente lo hace 5 hacia el lado y luego 3 mas largos abajo, quiero que sea hacia los lados

4. En noticias se muestran 3 noticias por fila, quiero que sean todas las que quepan dentro del ancho de la barra de busqueda/filtro:

```hmtl
<div style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid var(--border); box-shadow: rgba(0, 0, 0, 0.03) 0px 2px 10px; margin-bottom: 25px; display: flex; flex-wrap: wrap; gap: 15px; align-items: center;" data-protonpass-form=""><div style="flex-grow: 1; position: relative; min-width: 300px;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-search" aria-hidden="true" style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-light);"><path d="m21 21-4.34-4.34"></path><circle cx="11" cy="11" r="8"></circle></svg><input placeholder="Buscar por palabras clave..." style="width: 100%; padding: 10px 40px; border-radius: 8px; border: 1px solid var(--border); outline: none; font-size: 14px;" type="text" value=""></div><button style="display: flex; align-items: center; gap: 8px; padding: 10px 15px; background-color: var(--primary-light); color: var(--primary); border: 1px solid var(--primary); border-radius: 8px; cursor: pointer; font-weight: 500; font-size: 14px; transition: 0.2s;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-funnel" aria-hidden="true"><path d="M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z"></path></svg>Filtros Avanzados<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-up" aria-hidden="true"><path d="m18 15-6-6-6 6"></path></svg></button><button title="Restablecer todos los filtros" style="display: flex; align-items: center; gap: 8px; padding: 10px 15px; background-color: white; color: var(--text-dark); border: 1px solid var(--border); border-radius: 8px; cursor: pointer; font-weight: 500; font-size: 14px;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-rotate-ccw" aria-hidden="true"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>Restablecer</button><button style="display: flex; align-items: center; gap: 8px; padding: 10px 15px; background-color: var(--primary); color: white; border: medium; border-radius: 8px; cursor: pointer; font-weight: 500; font-size: 14px; transition: 0.2s; opacity: 1;"><svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-layout-dashboard" aria-hidden="true"><rect width="7" height="9" x="3" y="3" rx="1"></rect><rect width="7" height="5" x="14" y="3" rx="1"></rect><rect width="7" height="9" x="14" y="12" rx="1"></rect><rect width="7" height="5" x="3" y="16" rx="1"></rect></svg>Dashboard</button><div style="color: var(--text-light); font-size: 14px; margin-left: auto;">100 resultados encontrados</div></div>
```

6. Noticias no tiene que tener un boton 'Dashboard'
7. Quiero que al presionar el boton 'Dashboard' en cualquier categoria ya no diga dashboard si no que diga 'Registros' de manera que el boton cambie entre Dashboard y Registros, el cambio de color debe permanecer, el icono para volver a registros debera ser un libro o cuaderno y debera ser verde ya que los colores se invierten
