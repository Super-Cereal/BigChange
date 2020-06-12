$(document).ready(function(){
  $('.menu_ul').hide();

  const textUserQuestion = document.getElementById('email_log');
  const textUserQuestion2 = document.getElementById('email_reg');

  function explode(){
    $('#hamb').fadeIn(1000);
    textUserQuestion.focus();
    }
  setTimeout(explode, 500);

  $('.vt').on('click', function(){
    $('.modal_reg').hide()
    $('.modal_log').show() 
    function explode(){
      textUserQuestion.focus();
    }
    setTimeout(explode, 500);
  });

  $('.sz').on('click', function(){
    $('.modal_log').hide()
    $('.modal_reg').show() 
    function explode(){
      textUserQuestion2.focus();
    }
    setTimeout(explode, 500);
  });
});