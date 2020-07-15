$(document).ready(function() {
    for (let i = 0; i < 25; i++){ 
    $('label[for="photo"]').addClass("active"); 
    $('input[type="file"]').change(()=>{
        var filename = $("input[type='file']").val();
        if (filename.substring(3,11) == 'fakepath') {
            filename = filename.substring(12);}
        data = filename.split('.');
        if (filename.length > 0 && (data[data.length - 1] === 'jpg' || data[data.length - 1] === 'png' || data[data.length - 1] === 'jpeg')){
            $('label[for="photo"]').text(filename);}
        else{
            $('label[for="photo"]').addClass("nook");
            $('label[for="photo"]').text('Загрузить файл');
        }
        
    }); 
}
});