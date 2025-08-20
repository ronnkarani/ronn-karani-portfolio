particlesJS("particles-js", {
  particles: {
    number: {
      value: 100,
      density: {
        enable: true,
        value_area: 1000
      }
    },
    color: {
      value: "#ffffff"
    },
    shape: {
      type: "circle"
    },
    opacity: {
      value: 0.8,
      random: true
    },
    size: {
      value: 2,
      random: true
    },
    line_linked: {
      enable: false
    },
    move: {
      enable: true,
      speed: 0.6,
      direction: "none",
      random: true,
      straight: false,
      bounce: false
    }
  },
  interactivity: {
    events: {
      onhover: { enable: false },
      onclick: { enable: false }
    }
  },
  retina_detect: true
});


// Show or hide scroll-to-top button
// ===== Scroll to Top =====
const scrollTopBtn = document.getElementById("scrollTopBtn");

window.addEventListener("scroll", () => {
  scrollTopBtn.style.display =
    document.body.scrollTop > 100 || document.documentElement.scrollTop > 100
      ? "block"
      : "none";
});

scrollTopBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});


document.addEventListener('DOMContentLoaded', () => {
  const userDropdown = document.querySelector('.user-dropdown');
  if (!userDropdown) return;

  const dropdownContent = userDropdown.querySelector('.dropdown-content');
  const arrow = userDropdown.querySelector('.dropdown-arrow');
  const menuToggle = document.getElementById('menu-toggle');

  const toggleDropdown = (e) => {
    e.stopPropagation();
    dropdownContent.classList.toggle('active');
    arrow.classList.toggle('rotated');
  };

  userDropdown.addEventListener('click', toggleDropdown);

  // Close when clicking outside
  document.addEventListener('click', () => {
    dropdownContent.classList.remove('active');
    arrow.classList.remove('rotated');
  });

  // Optional: close dropdown when mobile menu closes
  if (menuToggle) {
    menuToggle.addEventListener('change', () => {
      if (!menuToggle.checked) {
        dropdownContent.classList.remove('active');
        arrow.classList.remove('rotated');
      }
    });
  }
});
const carousel = document.querySelector('.testimonial-carousel');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

let isDragging = false;
let startX, scrollLeft;

// Arrow buttons
nextBtn.addEventListener('click', () => {
  carousel.scrollBy({ left: 320, behavior: 'smooth' });
});

prevBtn.addEventListener('click', () => {
  carousel.scrollBy({ left: -320, behavior: 'smooth' });
});

// Mouse drag
carousel.addEventListener('mousedown', (e) => {
  isDragging = true;
  startX = e.pageX - carousel.offsetLeft;
  scrollLeft = carousel.scrollLeft;
});

carousel.addEventListener('mouseleave', () => {
  isDragging = false;
});

carousel.addEventListener('mouseup', () => {
  isDragging = false;
});

carousel.addEventListener('mousemove', (e) => {
  if (!isDragging) return;
  e.preventDefault();
  const x = e.pageX - carousel.offsetLeft;
  const walk = (x - startX) * 2; // scroll-fast
  carousel.scrollLeft = scrollLeft - walk;
});

// Touch events for mobile
carousel.addEventListener('touchstart', (e) => {
  startX = e.touches[0].pageX - carousel.offsetLeft;
  scrollLeft = carousel.scrollLeft;
});

carousel.addEventListener('touchmove', (e) => {
  const x = e.touches[0].pageX - carousel.offsetLeft;
  const walk = (x - startX) * 2;
  carousel.scrollLeft = scrollLeft - walk;
});