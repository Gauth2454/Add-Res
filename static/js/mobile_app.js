document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".nav-links");

    // Toggle mobile menu when clicking hamburger icon
    hamburger.addEventListener("click", function() {
        navLinks.classList.toggle("active");
    });

    // Ensure nav items reappear properly when resizing back to desktop
    window.addEventListener("resize", function() {
        if (window.innerWidth > 768) {
            navLinks.classList.remove("active"); // Show menu on larger screens
        }
    });
});