function fecharModal(e) {
  console.log("hello")
  e.preventDefault();
  document.getElementById("caixa__modal").style.display = "none";
}
function abrirModal(e) {
  e.preventDefault();
  document.getElementById("caixa__modal").style.display = "block";
}

function  CalcularTotal(){
  var valor = parseFloat(document.getElementById("valor__pagamento").value);
  var valor_calculado = valor;
  var juros = parseFloat(document.getElementById("juros").value);
  var desconto = parseFloat(document.getElementById("desconto").value);
  var total = document.getElementById("total");

  valor_calculado = valor + (juros - desconto)
  total.innerHTML = "Total: R$" + valor_calculado
}