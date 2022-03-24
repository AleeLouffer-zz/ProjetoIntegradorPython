function pessoaFisica(event){
    event.preventDefault();
    mudaUsuario("Física", "CPF");
    var cnpj_cpf = document.getElementById('cnpj_cpf');
    cnpj_cpf.setAttribute('maxlength','14');
    cnpj_cpf.setAttribute('minlength','14');
    cnpj_cpf.value = converteCPF(cnpj_cpf.value.slice(0,14));
}

function pessoaJuridica(event){
    event.preventDefault();
    mudaUsuario("Juridica", "CNPJ");
    var cnpj_cpf = document.getElementById('cnpj_cpf');
    cnpj_cpf.setAttribute('maxlength','18');
    cnpj_cpf.setAttribute('minlength','18');
    cnpj_cpf.value = converteCNPJ(cnpj_cpf.value);
}

function mudaUsuario(pessoa, cpf_cnpj){
    document.getElementById('nome').placeholder = "Digite o nome da Pessoa " + pessoa;
    document.getElementById('label_cnpj_cpf').innerHTML = cpf_cnpj;
    document.getElementById('cnpj_cpf').placeholder = "Digite o " + cpf_cnpj;
}