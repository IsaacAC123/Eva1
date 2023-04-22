var donar = 0;
donar = document.getElementById("donacion");
function hacerDonacion(){
    console.log(donar)
  if(donar < 0){
    alert("Tu donacion fue recibida con exito!");
  }else{
    alert("No puedes hacer donaciones por este monto");
  }
};
