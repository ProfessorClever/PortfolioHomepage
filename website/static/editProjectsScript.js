document.addEventListener("DOMContentLoaded", function () { 
    
    let deleteMenu = document.getElementById("deleteProject")
    let createMenu = document.getElementById("newProject")

    function changeMode(newMode) {
        switch (newMode) {
            case 1: { //createProjectMenu
                deleteMenu.style.display = "none"
                createMenu.style.display = "block"
                break;
            }
            case 2: { //deleteProjectMenu
                deleteMenu.style.display = "block"
                createMenu.style.display = "none"
                break;
            }
            default: { //NoMenu
                deleteMenu.style.display = "none"
                createMenu.style.display = "none"
                break;
            }
        }
    }

    document.getElementById("createAbort").addEventListener('click', function () {
        changeMode(0)
    })

    document.getElementById("deleteAbort").addEventListener('click', function () {
        changeMode(0)
    })

    document.getElementById("createNewProject").addEventListener('click', function () {
        changeMode(1)
    })
        
});