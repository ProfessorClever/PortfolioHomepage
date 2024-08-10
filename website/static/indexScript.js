document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("knowMeButton").addEventListener("click", toAboutMe);
    document.getElementById("showProjectsButton").addEventListener("click", toProjects);
    document.getElementById("latest").addEventListener("click", () => {
        const latest_id = document.getElementById("latest_id").innerText
        window.location.assign('/Projects/'+latest_id)
    });
    document.getElementById("popular").addEventListener("click", () => {
        const popular_id = document.getElementById("popular_id").innerText
        window.location.assign('/Projects/'+popular_id)
    });
});