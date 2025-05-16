// Update copyright year automatically
function updateCopyrightYear() {
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}

// Initialize when DOM loads
document.addEventListener('DOMContentLoaded', updateCopyrightYear);
