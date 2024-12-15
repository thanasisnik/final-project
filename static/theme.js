document.addEventListener('DOMContentLoaded', function () {
    const body = document.body;
    const icon = document.getElementById('theme-icon');
    
    // Use the local storage to store the user preferable theme
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
        icon.textContent = '🌙';  // Dark mode icon
    } else {
        body.classList.add('light-mode');
        icon.textContent = '☀️';  // Light mode icon
    }

    // Άλλαξε το θέμα όταν το κουμπί πατηθεί
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