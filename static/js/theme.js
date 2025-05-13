document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('.theme-toggle');
    const body = document.body;

    // Load saved theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    body.setAttribute('data-theme', savedTheme);

    themeToggle.addEventListener('click', () => {
        const currentTheme = body.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

        body.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        // Update button emoji
        themeToggle.textContent = newTheme === 'dark' ? '🌓' : '🌞';
    });
});


// Modify existing smooth scroll code
document.querySelectorAll('.nav-links a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if(href.startsWith('#')) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });

                // Update URL without reload
                history.pushState(null, null, href);

                // Close mobile menu
                if(window.innerWidth <= 768) {
                    hamburger.classList.remove('active');
                    navLinks.classList.remove('active');
                }
            }
        }
    });
});

const arrows = document.querySelectorAll('.nav-arrow');
const markers = document.querySelectorAll('.year-marker');
let currentCard = 0;

arrows.forEach(arrow => {
    arrow.addEventListener('click', () => {
        const isNext = arrow.classList.contains('next');
        currentCard = isNext ?
            Math.min(currentCard + 1, markers.length - 1) :
            Math.max(currentCard - 1, 0);

        updateExperience();
    });
});

markers.forEach((marker, index) => {
    marker.addEventListener('click', () => {
        currentCard = index;
        updateExperience();
    });
});

function updateExperience() {
    // Remove active classes
    document.querySelectorAll('.timeline-card, .year-marker')
        .forEach(el => el.classList.remove('active'));

    // Add active classes
    markers[currentCard].classList.add('active');
    document.querySelectorAll('.timeline-card')[currentCard].classList.add('active');
}
