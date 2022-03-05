const botao_adicionar = document.getElementById("adicionar");

botao_adicionar.addEventListener('click', (event) => {
    var valido = false;

    selects.forEach(select => {
        verificaValorSelect(select);
    })

    inputs.forEach(input =>{
        valida(input)
    })

    if (!valido) {
        event.preventDefault(); 
    }
    
})