function ExibirCadastroFuncionario() {
  document.getElementById("checkBoxFuncEdit").style.display = "none";
  var x = document.getElementById("checkBoxFunc");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function ExibirCadastroServico() {
  document.getElementById("checkBoxServEdit").style.display = "none";
  var x = document.getElementById("checkBoxServ");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function ExibirEditarFuncionario(nomeFuncionario, idFuncionario) {
  document.getElementById("checkBoxFunc").style.display = "none";
  var boxEditFunc= document.getElementById("checkBoxFuncEdit"); 

  if (boxEditFunc.style.display != "none") {
    boxEditFunc.style.display = "none";
  } else {
    boxEditFunc.style.display = "block";
    document.getElementById("checkBoxServ").style.display = "none";

    document.getElementById("nome_funcionario").value = nomeFuncionario;
    
    document.getElementById("id_funcionario").value = idFuncionario;
    console.log(document.getElementById("id_funcionario"));
  }
}

function ExibirEditarServico(nome, valor, descricao, servicoId) {
  document.getElementById("checkBoxServ").style.display = "none";
  var boxEditServ = document.getElementById("checkBoxServEdit");

  if (boxEditServ.style.display != "none") {
    boxEditServ.style.display = "none";
  } else {
    boxEditServ.style.display = "block";
    document.getElementById("checkBoxFunc").style.display = "none";

    document.getElementById('servico_id').value = servicoId;
    document.getElementById('servico_descricao').value = descricao;
    document.getElementById('servico_valor').value= valor;
    document.getElementById("servico_nome").value = nome;
  }
}
