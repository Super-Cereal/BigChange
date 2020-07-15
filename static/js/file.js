$(document).ready(function() {
    for (let i = 0; i < 25; i++){ 
    $('label[for="photo"]').addClass("active"); 
    $('input[type="file"]').change(()=>{
        var filename = $("input[type='file']").val();
        if (filename.substring(3,11) == 'fakepath') {
            filename = filename.substring(12);}
        data = filename.split('.');
        if (filename.length > 0 ){
            $('label[for="photo"]').text(filename);
            $('label[for="photo"]').addClass("ok");$
            ('label[for="photo"]').removeClass("nook");}
        else{
            $('label[for="photo"]').addClass("nook");
            $('label[for="photo"]').removeClass("ok");
            $('label[for="photo"]').text('Загрузить файл');
        }
        
    }); 
}
});