Quiero que el formato de la interfaz de Proyectos evaluados se aplique en Todas las categorias.
Esto es para toda la pagina menos lo que respecta a las tablas, las cosas que tengan tablas actualmente no deben convertirse en cards.
Solo hay que cambiar el apartado de arriba que vemos en SEA - Proyectos evaluados

```html
<div
  style="background-color: white; padding: 15px; border-radius: 12px; border: 1px solid var(--border); box-shadow: rgba(0, 0, 0, 0.03) 0px 2px 10px; margin-bottom: 25px; display: flex; flex-wrap: wrap; gap: 15px; align-items: center;"
  data-protonpass-form=""
>
  <div style="flex-grow: 1; position: relative; min-width: 300px;">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-search"
      aria-hidden="true"
      style="position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-light);"
    >
      <path d="m21 21-4.34-4.34"></path>
      <circle cx="11" cy="11" r="8"></circle></svg
    ><input
      placeholder="Buscar por nombre o titular..."
      style="width: 100%; padding: 10px 40px; border-radius: 8px; border: 1px solid var(--border); outline: none; font-size: 14px;"
      type="text"
      value=""
    />
  </div>
  <button
    style="display: flex; align-items: center; gap: 8px; padding: 10px 15px; background-color: white; color: var(--text-dark); border: 1px solid var(--border); border-radius: 8px; cursor: pointer; font-weight: 500; font-size: 14px; transition: 0.2s;"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-funnel"
      aria-hidden="true"
    >
      <path
        d="M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z"
      ></path></svg
    >Filtros Avanzados<svg
      xmlns="http://www.w3.org/2000/svg"
      width="16"
      height="16"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-chevron-down"
      aria-hidden="true"
    >
      <path d="m6 9 6 6 6-6"></path>
    </svg></button
  ><button
    title="Restablecer todos los filtros"
    style="display: flex; align-items: center; gap: 8px; padding: 10px 15px; background-color: white; color: var(--text-dark); border: 1px solid var(--border); border-radius: 8px; cursor: pointer; font-weight: 500; font-size: 14px;"
  >
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="18"
      height="18"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
      class="lucide lucide-rotate-ccw"
      aria-hidden="true"
    >
      <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path>
      <path d="M3 3v5h5"></path></svg
    >Restablecer
  </button>
  <div style="color: var(--text-light); font-size: 14px; margin-left: auto;">
    0 resultados encontrados
  </div>
</div>
```

Tambien deberas implementar un boton para los dashboards (Aunque no haga nada) que sea del mismo color que se ha usado en la pagina y que este al lado del boton 'Restablecer', debe ser rectangular y tener el icono que se ha usado para los dashboards actualmente.

Ese boton para los dashboards debe implementarse en todas las categorias.

Este cambio de formato no debe afectar a la funcionalidad de los filtros ni la barra de busqueda (debe activarse al hacer enter)
