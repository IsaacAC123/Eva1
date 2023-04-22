const apiUrl =
  "https://gist.githubusercontent.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd/raw/b8575eb82dce974fd2647f46819a7568278396bd/comunas-regiones.json";
const regionSelect = document.getElementById("regionSelect");
const comunaSelect = document.getElementById("comunaSelect");
const regionValue = document.getElementById("regionValue");
const comunaValue = document.getElementById("comunaValue");
let regionesArray = [];
let comunasArray = [];

regionSelect.addEventListener("change", function () {
  // Borra todas las opciones del elemento comunaSelect
  while (comunaSelect.firstChild) {
    comunaSelect.removeChild(comunaSelect.firstChild);
  }

  // Obtiene las comunas correspondientes a la región seleccionada
  const regionIndex = regionSelect.value;
  const comunasDeRegion = comunasArray[regionIndex];

  // Crea una opción para cada comuna y agrega al elemento comunaSelect
  for (let i = 0; i < comunasDeRegion.length; i++) {
    if (i === 0) {
      comunaValue.innerHTML = comunasDeRegion[i];
    }
    const option = document.createElement("option");
    option.value = comunasDeRegion[i];
    option.text = comunasDeRegion[i];
    comunaSelect.appendChild(option);
  }
  regionValue.innerHTML = regionesArray[regionSelect.value].region;
});

comunaSelect.addEventListener("change", function () {
  comunaValue.innerHTML = comunaSelect.value;
});

async function consumeapi() {
  axios
    .get(apiUrl)
    .then((response) => {
      const regionesData = response.data.regiones;
      regionesArray = regionesData;
      for (let i = 0; i < regionesData.length; i++) {
        comunasArray.push(regionesData[i].comunas);
      }
      for (let i = 0; i < regionesArray.length; i++) {
        if (i === 0) {
          const comunasDeRegion = comunasArray[i];
          regionValue.innerHTML = regionesArray[i].region;
          for (let ix = 0; ix < comunasDeRegion.length; ix++) {
            if (ix === 0) {
              comunaValue.innerHTML = comunasDeRegion[i];
            }
            const option = document.createElement("option");
            option.value = comunasDeRegion[ix];
            option.text = comunasDeRegion[ix];
            comunaSelect.appendChild(option);
          }
        }
        const option = document.createElement("option");
        option.value = i;
        option.text = regionesArray[i].region;
        regionSelect.appendChild(option);
      }
    })
    .catch((error) => console.error(error));
}

consumeapi();
// validaciones

$(function () {
  $("formulario").validate({
    rules: {
      email: {
        required: true,
        email: true,
      },
      date: {
        required: true,
        date: true,
      },
      number: {
        required: true,
        minlenght: 9,
        maxlenght: 9,
      },
    },
    messages: {
      email: {
        required: "Ingresa tu correo electrónico",
        email: "Formato de correo no válido",
      },
    },
  });
});

// funcion btn enviar
function alertaenviar() {
  return confirm("¿Estás seguro de enviar el formulario?");
}
