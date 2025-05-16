document.addEventListener('DOMContentLoaded', () => {
    const titles = [
        "Full Stack Developer",
        "Web Developer",
        "Researcher",
        "Philosopher",
        "Neuroscientist",
        "Writer",
        "Coacher",
        "Healer",
        "Rastafarian",
        "Entrepreneur"  // Add any new titles here
    ];

    const container = document.querySelector('.dynamic-title');
    container.innerHTML = ''; // Clear existing titles

    // Add visibility control
    titles.forEach((title, index) => {
        const span = document.createElement('span');
        span.className = 'title-rotator';
        span.textContent = title;
        span.style.animation = `titleSlide 30s infinite ${index * 3}s`; // 10 titles × 3s each
        container.appendChild(span);
    });
});
