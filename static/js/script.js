$(document).ready(function(){
    $('.menu_ul').fadeOut(2000);
    function explode(){
        $('#hamb').fadeIn(1000);
      }
      setTimeout(explode, 2001);
    let textUserQuestion = document.getElementById('email_log');
                textUserQuestion.focus();
    $('.vt').on('click', function(){
            $('.modal_reg').fadeOut('slow')
            $('.modal_log').fadeIn(500)
            
            
          });
    $('.sz').on('click', function(){
            $('.modal_log').fadeOut('slow')
            $('.modal_reg').fadeIn(500)
            let textUserQuestion = document.getElementById('email_reg');
                textUserQuestion.focus();
          });

});