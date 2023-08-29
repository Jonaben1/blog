toggler = () => {
    let element = document.getElementById('mode');
    let body = document.body;
    if (element.innerHTML === 'Night Mode') {
       element.innerHTML = 'Light Mode';
       body.classList.toggle('dark-mode');
    } else {
        element.innerHTML = 'Night Mode';
        body.classList.toggle('dark-mode');
    }
}
