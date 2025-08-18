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

document.addEventListener("DOMContentLoaded", () => {
  // ✅ Initialize Swiper
  const swiper = new Swiper(".mySwiper", {
    loop: true,
    autoplay: {
      delay: 4000,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  // ✅ Make all slides same height
  const slides = document.querySelectorAll(".swiper-slide");
  let maxHeight = 0;

  slides.forEach(slide => {
    maxHeight = Math.max(maxHeight, slide.offsetHeight);
  });

  slides.forEach(slide => {
    slide.style.height = maxHeight + "px";
  });
});
