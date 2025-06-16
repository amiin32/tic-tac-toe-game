// Theme toggle functionality
const themeToggleButton = document.getElementById('theme-toggle');
const body = document.body;

// Check for saved theme in localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  body.classList.add(savedTheme);
}

// Toggle theme on button click
themeToggleButton.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  
  // Save the current theme to localStorage
  if (body.classList.contains('dark-mode')) {
    localStorage.setItem('theme', 'dark-mode');
  } else {
    localStorage.setItem('theme', '');
  }
});

// Contact form submission alert
document.getElementById('contact-form').addEventListener('submit', function(event) {
  event.preventDefault();
  alert('Thank you for reaching out! I will get back to you soon.');
});