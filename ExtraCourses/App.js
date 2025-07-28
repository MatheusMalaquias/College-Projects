const btn = document.querySelector('.btn');
const body = document.body;

btn.addEventListener('click', () => {
    if (body.classList.contains('light-theme')) {
        body.classList.replace('light-theme', 'dark-theme');
        btn.textContent = 'Light';
    } else {
        body.classList.replace('dark-theme', 'light-theme');
        btn.textContent = 'Dark';
    }
});
