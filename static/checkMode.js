// check the theme when the page is loading
document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    
    // checks if theme exists in local storage
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
    } else {
        body.classList.add('light-mode');
    }
});