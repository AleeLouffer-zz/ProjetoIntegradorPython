function abrirMenu(){
    const menu = document.querySelector(".menu");
    menu.classList.add("menu__aberto");
}

function fecharMenu(){
    const menu = document.querySelector(".menu");
    menu.classList.remove("menu__aberto");
}