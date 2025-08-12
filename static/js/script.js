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

// Fake comment submission (no backend)
const form = document.querySelector('.comment-form');
const commentList = document.querySelector('.comment-list');

form?.addEventListener('submit', function (e) {
  e.preventDefault();
  const textarea = this.querySelector('textarea');
  const comment = textarea.value.trim();
  if (comment) {
    const el = document.createElement('div');
    el.classList.add('comment');
    el.innerHTML = `<p><strong>You:</strong> ${comment}</p>`;
    commentList.appendChild(el);
    textarea.value = '';
  }
});


const blogForm = document.querySelector('.comment-form');
const blogCommentList = document.querySelector('.comment-list');

blogForm?.addEventListener('submit', function (e) {
  e.preventDefault();
  const textarea = this.querySelector('textarea');
  const comment = textarea.value.trim();
  if (comment) {
    const el = document.createElement('div');
    el.classList.add('comment');
    el.innerHTML = `<p><strong>You:</strong> ${comment}</p>`;
    blogCommentList.appendChild(el);
    textarea.value = '';
  }
});


document.querySelector('.contact-form')?.addEventListener('submit', function (e) {
  e.preventDefault();
  alert('Thanks for your message, Ronny will get back to you soon!');
  this.reset();
});
