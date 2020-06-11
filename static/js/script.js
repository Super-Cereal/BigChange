$(document).ready(function(){
    $('.menu_ul').hide();

    function explode(){
        $('#hamb').fadeIn(1000);
      }
      setTimeout(explode, 500);
    const textUserQuestion = document.getElementById('email_log');
                textUserQuestion.focus();
    const textUserQuestion2 = document.getElementById('email_reg');
    $('.vt').on('click', function(){
            $('.modal_reg').hide()
            $('.modal_log').show() 
            textUserQuestion.focus();
            
            
          });
    $('.sz').on('click', function(){
            $('.modal_log').hide()
            $('.modal_reg').show() 
            textUserQuestion2.focus();
          });

});