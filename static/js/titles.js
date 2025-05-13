document.addEventListener('DOMContentLoaded', () => {
    const titles = [
        "Python Developer",
        "Web Developer",
        "Researcher",
        "Philosopher",
        "Neuroscientist",
        "Writer",
        "Rastafarian",
        "Entrepreneur"
    ];

    const container = document.querySelector('.dynamic-title');
    container.innerHTML = ''; // Clear existing titles

    titles.forEach((title, index) => {
        const span = document.createElement('span');
        span.className = 'title-rotator';
        span.textContent = title;
        span.style.animationDelay = `${index * 3}s`; // Set delay dynamically
        container.appendChild(span);
    });
});