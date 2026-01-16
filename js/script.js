// Adiciona uma sombra na barra de navegação ao rolar a página
window.addEventListener('scroll', function() {
    const nav = document.querySelector('nav');
    if (window.scrollY > 50) {
        nav.style.background = 'rgba(15, 23, 42, 0.98)';
        nav.style.boxShadow = '0 2px 10px rgba(0,0,0,0.5)';
    } else {
        nav.style.background = 'rgba(15, 23, 42, 0.9)';
        nav.style.boxShadow = 'none';
    }
});