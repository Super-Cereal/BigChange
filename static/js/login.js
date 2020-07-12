$(document).ready(function(){
    $('.menu').hide();
   document.querySelector('.hamburger_main').style.display = 'none';
    function explode(){
      $('#hamb').fadeIn(1000);
      textUserQuestion.focus();
      }
    setTimeout(explode, 500);
  });