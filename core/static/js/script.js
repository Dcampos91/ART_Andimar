function verificarRespuestas() {
    var total = 14;
    var puntos = 0;
    

    var myForm = document.forms["quizForm"];
    var respuestas = ["SI", "SI", "SI", "SI", "SI", "SI", "SI", "NO", "NO", "SI", "SI", "SI", "SI", "SI"];

    for (var i = 1; i <= total; i++) {
        if (myForm["p" + i].value === null || myForm["p" + i].value === "") {
            alert('Por Favor Responda la pregunta' + i);
            return false;
        } else {
            if (myForm["p" + i].value === respuestas[i - 1]) {
                puntos++;
            }
        }
    }

    var resultado = document.getElementById("resultado");
    resultado.innerHTML = '<h3>Obtuvistes <span>' + puntos + '</span> de <span>' + total + ' puntos</span></h3>';
    if(puntos==14){
        alert('bien')
    }else{
        alert('mal')
    }
    console.log(puntos)
    return false;
}


function mostrar(){
    let id = document.getElementById("id").value;
    let idconductor = document.getElementById("idconductor").value;
    let idconductor2 = document.getElementById("idconductor2").value;
    let idauxiliar = document.getElementById("idauxiliar").value;
    let idbus = document.getElementById("idbus").value;
    let conductor = document.getElementById("conductor").value;
    let conductordos = document.getElementById("conductordos").value;
    let auxiliar = document.getElementById("auxiliar").value;
    let bus = document.getElementById("bus").value;
    

    console.log(id);
    console.log(idconductor);
    console.log(idconductor2);
    console.log(idauxiliar);
    console.log(idbus);    
    console.log(conductor);
    console.log(conductordos);
    console.log(auxiliar);
    console.log(bus);
    


}