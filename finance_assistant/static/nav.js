const nav_stuff = document.querySelector("#navbar-cta");

const hamburger = document.querySelector("#hamburger");

hamburger.addEventListener("click", () => {
    nav_stuff.classList.toggle("hidden");
});