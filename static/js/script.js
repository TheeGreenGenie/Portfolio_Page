// Add JavaScript functionality here
document.addEventListener('DOMContentLoaded', function() {
    // Simple animation for page elements
    const fadeInElements = document.querySelectorAll('section');
    
    // Add a class to each section as it comes into view
    window.addEventListener('scroll', function() {
        fadeInElements.forEach(element => {
            const position = element.getBoundingClientRect();
            
            // If element is in viewport
            if(position.top < window.innerHeight && position.bottom >= 0) {
                element.classList.add('visible');
            }
        });
    });
    
    // Form submission (for contact form)
    const contactForm = document.querySelector('#contact form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // This would normally send the form data to a server
            alert('Thank you for your message! In a real application, this would be sent to a server.');
            
            // Reset the form
            contactForm.reset();
        });
    }
});