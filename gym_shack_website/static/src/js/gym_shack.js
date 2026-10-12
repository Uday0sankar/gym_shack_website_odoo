document.addEventListener('DOMContentLoaded', function () {
  const menuToggle = document.querySelector('.menu-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener('click', function () {
      mobileMenu.classList.toggle('is-open');
    });
    mobileMenu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileMenu.classList.remove('is-open');
      });
    });
  }

  const header = document.querySelector('.gym-shack-header');
  if (header) {
    const applyHeaderState = function () {
      if (window.scrollY > 20) {
        header.style.background = 'rgba(5,5,5,0.75)';
        header.style.boxShadow = '0 10px 30px rgba(0,0,0,0.2)';
      } else {
        header.style.background = 'rgba(5,5,5,0.35)';
        header.style.boxShadow = 'none';
      }
    };
    applyHeaderState();
    window.addEventListener('scroll', applyHeaderState, { passive: true });
  }

  const successTarget = new URLSearchParams(window.location.search).get('submitted');
  if (successTarget === '1') {
    const formWrap = document.querySelector('.contact-form-wrap');
    if (formWrap) {
      formWrap.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
});
