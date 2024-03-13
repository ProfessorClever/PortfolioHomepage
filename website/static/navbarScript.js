document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("about-me-link").addEventListener("click", toAboutMe);
  document.getElementById("projects-link").addEventListener("click", toProjects);
  document.getElementById("contacts-link").addEventListener("click", toContact);
});

function toAboutMe() {
  window.location.assign("/AboutMe");
}

function toProjects() {
  window.location.assign("/Projects")
}

function toContact() {
  window.location.assign("/Contact")
}
