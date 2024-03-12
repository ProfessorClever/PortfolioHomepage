document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("about-me-link").addEventListener("click", toAboutMe);
});

function toAboutMe() {
  window.location.assign("/AboutMe");
}
