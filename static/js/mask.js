$(document).ready( () => {
    
    const cpf = document.getElementById("id_cpf");
  
    if (cpf) {
        $("#id_cpf").mask("000.000.000-00");
    } else {
        $("#id_cnpj").mask("00.000.000/0000-00");
    }   

    var SPMaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
      },
      spOptions = {
        onKeyPress: function(val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
          }
      };
      
      $('#id_telefone').mask(SPMaskBehavior, spOptions);
})