jQuery(document).ready(function(){
        const textUserQuestion = document.getElementById('email_log');
        const textUserQuestion2 = document.getElementById('email_reg');
        var box1 = $.cookie('modal_log')//Получаем значение куки 
        textUserQuestion.focus();
        if(box1 =='none'){//Делаем проверку  
            $('#modal_log').hide();
            $('#modal_reg').show();
            textUserQuestion2.focus();
            } 
        $('#sz').click(function() {//При клике на id кнопки закрытия 
            $('#modal_log').hide();
            $('#modal_reg').show(); //Закрываем сам id блока 
            $.cookie('modal_log', 'none', { expires: 7});//И создаём куку 
            textUserQuestion2.focus();
        }); 
        $('#vt').click(function() {//При клике на id кнопки закрытия 
            $('#modal_reg').hide();
            $('#modal_log').show(); //Закрываем сам id блока 
            textUserQuestion.focus();
            $.cookie('modal_log', 'block', { expires: 7});//И создаём куку 
        }); 

    }); 
