// A part of code was created with the help of AI and it handles the form submission
// its logic was fully understood first

document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const icon = document.getElementById('theme-icon');
    
    // use the local storage to store the user preferable theme
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
        icon.textContent = '🌙';  // Dark mode icon
    } else {
        body.classList.add('light-mode');
        icon.textContent = '☀️';  // Light mode icon
    }

    // change the button 
    document.getElementById('theme-toggle').addEventListener('click', function() {
        body.classList.toggle('dark-mode');
        body.classList.toggle('light-mode');

        // save the prefer them at local storage
        if (body.classList.contains('dark-mode')) {
            icon.textContent = '🌙';  // Dark Mode icon
            localStorage.setItem('theme', 'dark');
        } else {
            icon.textContent = '☀️';  // Light Mode icon
            localStorage.setItem('theme', 'light');
        }
    });
});