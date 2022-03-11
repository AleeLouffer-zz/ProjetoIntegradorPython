function valida(input){
    const tipodeInput = input.dataset.tipo;
    if(validadores[tipodeInput]){
        validadores[tipodeInput](input)
    }
}

const validadores = {
    data:input => validaInput(input),
    hora:input => validaInput(input),
    valor:input=> validaInput(input),
    texto:input=> validaInput(input),
    email:input=> validaInput(input),
    senha:input=> validaInput(input),
    inputComLabel:input=>validaInputComLabel(input)
}

const inputs = document.querySelectorAll('input');

inputs.forEach(input => {
    input.addEventListener('change', (evento) =>{
        valida(evento.target)
    })
})

function validaInput(input){
    if(input.value==""){
        input.classList.add('invalido');
    }
    else{
        input.classList.remove('invalido'); 
    }
}

function validaInputComLabel(input){
    if(input.value==""){
        input.parentNode.classList.add('invalido');
    }
    else{
        input.parentNode.classList.remove('invalido'); 
    }
}