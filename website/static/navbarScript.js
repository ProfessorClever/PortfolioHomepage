document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("logo").addEventListener("click", toHome)
  document.getElementById("about-me-link").addEventListener("click", toAboutMe);
  document.getElementById("projects-link").addEventListener("click", toProjects);
  document.getElementById("contact-link").addEventListener("click", toContact);
});

function toHome() {
  window.location.assign("/");
}

function toAboutMe() {
  window.location.assign("/AboutMe");
}

function toProjects() {
  window.location.assign("/Projects")
}

function toContact() {
  window.location.assign("/Contact")
}
