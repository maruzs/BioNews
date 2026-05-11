Haz las cards mas grandes ya que las palabras se sobrepone unas a otras y algunas no aparecen, ademas de salirse de la card. tambien que esten mas pegadas a la izquierda.
Las barras mas gruesas para que el texto quepa bien, asi como en la foto.

O mejor aun, vamos a implementar que todos los graficos de barras (Excepto los circulares, pastel y los de cronologia) sean como el de pertinencias por tipo:

```html
<div
  class="MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation0 css-1kg2jed-MuiPaper-root"
  style="--Paper-shadow: none;"
>
  <div class="MuiBox-root css-mbsucw">
    <h6
      class="MuiTypography-root MuiTypography-subtitle1 css-ok3ajy-MuiTypography-root"
    >
      Pertinencias por Tipo
    </h6>
    <div class="MuiBox-root css-1utx3w7">
      <button
        class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-155wbr6-MuiButtonBase-root-MuiIconButton-root"
        tabindex="0"
        type="button"
        aria-label="Exportar"
        data-mui-internal-clone-element="true"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="lucide lucide-download"
          aria-hidden="true"
        >
          <path d="M12 15V3"></path>
          <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
          <path d="m7 10 5 5 5-5"></path>
        </svg></button
      ><button
        class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeSmall css-155wbr6-MuiButtonBase-root-MuiIconButton-root"
        tabindex="0"
        type="button"
        aria-label="Expandir"
        data-mui-internal-clone-element="true"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
          class="lucide lucide-maximize2 lucide-maximize-2"
          aria-hidden="true"
        >
          <path d="M15 3h6v6"></path>
          <path d="m21 3-7 7"></path>
          <path d="m3 21 7-7"></path>
          <path d="M9 21H3v-6"></path>
        </svg>
      </button>
    </div>
  </div>
  <div class="MuiBox-root css-x0pkpv">
    <div class="MuiBox-root css-y85hq0" id="chart-0">
      <div class="MuiBox-root css-1jdswee">
        <div class="MuiBox-root css-112dkhb">
          <div class="MuiBox-root css-wax5jp">
            <p
              class="MuiTypography-root MuiTypography-body2 css-10tja0m-MuiTypography-root"
            >
              Proyecto nuevo
            </p>
            <p
              class="MuiTypography-root MuiTypography-body2 css-17tcrs6-MuiTypography-root"
            >
              3,102
            </p>
          </div>
          <div
            class="MuiBox-root css-1he61sk"
            aria-label="Proyecto nuevo: 3102 (62%)"
            data-mui-internal-clone-element="true"
          >
            <div
              style="height: 100%; background-color: rgb(25, 118, 210); border-radius: 6px; box-shadow: none; width: 100%;"
            ></div>
          </div>
        </div>
        <div class="MuiBox-root css-112dkhb">
          <div class="MuiBox-root css-wax5jp">
            <p
              class="MuiTypography-root MuiTypography-body2 css-10tja0m-MuiTypography-root"
            >
              Modificación con RCA
            </p>
            <p
              class="MuiTypography-root MuiTypography-body2 css-17tcrs6-MuiTypography-root"
            >
              1,528
            </p>
          </div>
          <div
            class="MuiBox-root css-1he61sk"
            aria-label="Modificación con RCA: 1528 (30.6%)"
            data-mui-internal-clone-element="true"
          >
            <div
              style="height: 100%; background-color: rgb(156, 39, 176); border-radius: 6px; box-shadow: none; width: 49.2585%;"
            ></div>
          </div>
        </div>
        <div class="MuiBox-root css-112dkhb">
          <div class="MuiBox-root css-wax5jp">
            <p
              class="MuiTypography-root MuiTypography-body2 css-10tja0m-MuiTypography-root"
            >
              Modificación sin RCA
            </p>
            <p
              class="MuiTypography-root MuiTypography-body2 css-17tcrs6-MuiTypography-root"
            >
              370
            </p>
          </div>
          <div
            class="MuiBox-root css-1he61sk"
            aria-label="Modificación sin RCA: 370 (7.4%)"
            data-mui-internal-clone-element="true"
          >
            <div
              style="height: 100%; background-color: rgb(245, 158, 11); border-radius: 6px; box-shadow: none; width: 11.9278%;"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```

NO SE HAN HECHO LOS CAMBIOS EN PROYECTOS EVALUADOS, SIGUE MOSTRANDO NO ESPECIFICADO EN TIPO DE PRESENTACION Y ESTADO DE EVALUACION, CUANDO CLARAMENTE EN LA BASE DE DATOS EN LA TABLA SEA_PROYECTOS_EVALUADOS HAY DIFERENTES ESTADOS Y RAZONES DE INGRESO. ADEMAS LOS COLORES CAMBIARON, YA NO SON LOS QUE TENIAMOS ANTES
