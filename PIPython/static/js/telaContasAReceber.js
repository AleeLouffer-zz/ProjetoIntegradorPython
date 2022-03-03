function fecharModal(e) {
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
  
  valor_calculado = (valor + (juros - desconto)).toFixed(2);
  
  var total = document.getElementById("total");
  total.innerHTML = "Total: R$" + valor_calculado;
  
  var input_total = document.getElementById("input_total");
  input_total.value = valor_calculado;
}