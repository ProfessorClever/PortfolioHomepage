document.addEventListener("DOMContentLoaded", function () { //This wrapper makes sure, the document is fully loaded before code is run
    document.getElementById("logo").addEventListener("click", toHome)
    document.getElementById("edit-me-link").addEventListener("click", toAboutMe);
    document.getElementById("edit-projects-link").addEventListener("click", toProjects);
    document.getElementById("edit-contact-link").addEventListener("click", toContact);
    document.getElementById("menu-button").addEventListener("click", toggleMenu);
  });
  
  function toHome() {
    window.location.assign("/");
  }
  
  function toAboutMe() {
    window.location.assign("/EditMe");
  }
  
  function toProjects() {
    window.location.assign("/EditProjects")
  }
  
  function toContact() {
    window.location.assign("/EditContact")
  }
  
  function toggleMenu() {
    var active = false
    var navlinks = document.querySelector(".navlinks");
    navlinks.classList.toggle("active");
    var active = navlinks.classList.contains("active");
    var menuButton = document.getElementById("button-text");
    active ? menuButton.innerText = "Close Menu" : menuButton.innerText = "Menu";
    active = !active
  }