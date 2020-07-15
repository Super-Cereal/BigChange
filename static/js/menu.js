window.addEventListener('DOMContentLoaded', () => {
    const menu = document.querySelector('.menu'),
    hamburger = document.querySelector('.hamburger_main'),
    line = document.querySelector('.line'),
    black = document.querySelector('.black'),
    hamburger_cross = document.querySelector('.hamburger_cross');
    
    hamburger.addEventListener('click', () => {
        if (menu.style.opacity == '0')
        {
            setTimeout(()=>{hamburger.style.display = 'none';}, 400);
            black.style.left = 0;
            black.style.opacity = 1;
            menu.style.opacity = 1;
            menu.style.right = 0;
            menu.style.zIndex = 11;
        
        }else{
            menu.style.opacity = 0;
            black.style.display = 'none';
            menu.style.right = '-100%';
            hamburger.style.display = 'block';
            black.style.left = '-50%';
        }
    });
    black.addEventListener('click', ()=>{
        menu.style.opacity = 0;
        black.style.opacity = 0;
        black.style.left = '-50%';
        hamburger.style.display = 'block';
        menu.style.zIndex = 0;
        menu.style.right = '-100%';
    });

    hamburger_cross.addEventListener('click', ()=>{
        menu.style.opacity = 0;
        black.style.opacity = 0;
        black.style.left = '-50%';
        hamburger.style.display = 'block';
        menu.style.zIndex = 0;
        menu.style.right = '-100%';
    });
});
