const botao_adicionar = document.getElementById("adicionar");

botao_adicionar.addEventListener('click', (event) => {
    
    selects.forEach(select => {
        verificaValorSelect(select);
    })
    
    inputs.forEach(input =>{
        valida(input)
    })
    
    var valido = verificaCamposInvalidosExistentes();

    if (!valido) {
        event.preventDefault(); 
    }
})

function verificaCamposInvalidosExistentes(){
    var camposInvalidos = document.querySelectorAll('.invalido');
    if (camposInvalidos.length == 0){
        return true
    }
    else{
        return false
    }
}