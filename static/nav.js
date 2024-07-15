// arquivo script de js para responsividade da navbar
const nav = document.querySelector(".nav"),
  navOpenBtn = document.querySelector(".navOpenBtn"),
  navCloseBtn = document.querySelector(".navCloseBtn");
const body = document.querySelector("body");

let isNavOpen = false;

navOpenBtn.addEventListener("click", () => {
  nav.classList.add("openNav");
  isNavOpen = true;
  preventBodyScroll();
});

navCloseBtn.addEventListener("click", () => {
  nav.classList.remove("openNav");
  isNavOpen = false;
  allowBodyScroll();
});

// função que bloqueia o scroll do site quando a navbar lateral estiver aberta
function preventBodyScroll() {
  if (!isNavOpen) return;

  body.style.overflow = "hidden";
  document.documentElement.style.overflow = "hidden";
}

function allowBodyScroll() {
  if (isNavOpen) return;

  body.style.overflow = "auto";
  document.documentElement.style.overflow = "";
}