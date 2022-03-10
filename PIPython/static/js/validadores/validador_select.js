const selects = document.querySelectorAll("select");
selects.forEach(select => {
    select.addEventListener('change', (evento) => {
        verificaValorSelect(evento.target);
    })
})

function verificaValorSelect(select) {
    if (select.value == "None") {
        select.classList.add('invalido');
    }
    else {
        select.classList.remove('invalido');
    }
}