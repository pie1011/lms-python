/**
 * Dropdown Navigation Functionality
 * Handles click-based dropdown menus with proper accessibility
 */

function toggleDropdown() {
    const dropdown = document.getElementById('staffPortalDropdown');
    dropdown.classList.toggle('active');
}

// Close dropdown when clicking outside
document.addEventListener('click', function(event) {
    const dropdown = document.getElementById('staffPortalDropdown');
    const isClickInsideDropdown = dropdown.contains(event.target);
    
    if (!isClickInsideDropdown) {
        dropdown.classList.remove('active');
    }
});

// Close dropdown when pressing Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const dropdown = document.getElementById('staffPortalDropdown');
        dropdown.classList.remove('active');
    }
});

// Optional: Close dropdown when clicking on a dropdown item
// (useful if the dropdown items are regular links, not just the admin login)
document.addEventListener('click', function(event) {
    if (event.target.closest('.dropdown-item')) {
        const dropdown = document.getElementById('staffPortalDropdown');
        dropdown.classList.remove('active');
    }
});