$(document).ready(function(){

    $()

    $("#inenviar").click(function(e){

        if(validacion()!=""){
            swal("Error de envio",validacion(),"Warning");
        }else{
            swal("Todo correcto");
        }
        e.preventDefault();
    });

    function validacion(){
        var html="";
        var nombre=$("#txtnombre").val();
        var appaterno=$("#txtappaterno").val();
        var apmaterno=$("#txtapmaterno").val();
        var email=$("#txtcorreo").val();
        var locacion=$("#cbxlocacion").val();
        var comentarios=$("#tacomentario").val();
        var fechanac=$("#datefechanacimiento").val();
        
        if(nombre.trim().length<7){
            html+="Ingrese minimo 10 caracteres para el primer nombre\n";
        }
        if(appaterno.trim().length<10){
            html+="Ingrese minimo 10 caracteres para el apellido paterno\n";
        }
        if(apmaterno.trim().length<10){
            html+="Ingrese minimo 10 caracteres para el apellido materno\n";
        }
        if( ($("#rbtnrut")).is(":not(:checked)") ){
            html+="debe tener un tipo de identificacion\n";
        }
        if($("#txtident").val()==""){
            html+="Debe Ingresar el rut\n";
        }else{
           if(validarrut($("#txtident").val())==false){
               html+="Debe Ingresar un RUT Valido \n";
           }
       }
       if(fechanac==""){
        html+="Debe rellenar la fecha de nacimiento\n";
       }
        if(email==""){
            html+="Debe ingresar una dirección de correo electronico\n";
        }
        if(locacion=="0"){
            html+="Debe ingresar una locacion\n";
        }
        if(comentarios.trim().length<50){
            html+="debe tener al menos 50 caracteres\n"
        }
        return html;
    }
function validarrut(rutcomp) {
        rutcomp = rutcomp.replace("‐","-");

        if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rutcomp))
            return false;
        var tmp = rutcomp.split('-');
        var digitov = tmp[1];
        var rut = tmp[0];

        if (digitov == 'K') digitov = 'k';
        return (dv(rut) == digitov);
    }
function dv(V) {
        var M = 0,
            S = 1;
        for (; V; V = Math.floor(v / 10))
            S = (S + V % 10 * (9 - M++ % 6)) % 11;
        return S ? S - 1 : 'k';
    }
});