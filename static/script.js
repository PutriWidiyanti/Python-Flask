// Smooth Scroll for Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Alert on Button Click
document.querySelectorAll('.btn-primary').forEach(button => {
    button.addEventListener('click', function () {
        alert('Button clicked!');
    });
});
