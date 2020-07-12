window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.menu'),
    hamburger = document.querySelector('.hamburger_main'),
    line = document.querySelector('.line'),
    black = document.querySelector('.black'),
    hamburger_cross = document.querySelector('.hamburger_cross');
    
    hamburger.addEventListener('click', () => {
        if (menu.style.opacity == '0')
        {
            hamburger.style.display = 'none';
            black.style.left = 0;
            menu.style.opacity = 1;
            menu.style.right = 0;
            menu.style.zIndex = 11;
            
        
        }else{
            menu.style.opacity = 0;
            menu.style.right = '-100%';
            hamburger.style.display = 'block';
        }
    });
    black.addEventListener('click', ()=>{
        menu.style.opacity = 0;
        hamburger.style.display = 'block';
        menu.style.zIndex = 0;
        menu.style.right = '-100%';
    });

    hamburger_cross.addEventListener('click', ()=>{
        menu.style.opacity = 0;
        hamburger.style.display = 'block';
        menu.style.zIndex = 0;
        menu.style.right = '-100%';
    });
});
