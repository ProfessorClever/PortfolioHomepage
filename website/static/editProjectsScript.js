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

    document.getElementById("createAbort").addEventListener('click', function (event) {
        event.preventDefault();
        changeMode(0)
    })

    document.getElementById("deleteAbort").addEventListener('click', function () {
        changeMode(0)
    })

    document.getElementById("createNewProject").addEventListener('click', function () {
        changeMode(1)
    })

    document.getElementById("newProjectForm").addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        
        fetch('/Api/createProject', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(message => {
            document.getElementById('newProjectResponseMessage').innerText = message;
        })
        .catch(error => {
            document.getElementById('newProjectResponseMessage').innerText = 'An error occurred while sending the message.';
            console.error('Error:', error);
        });
    })
    
    document.querySelectorAll('.openProjectButton').forEach(button => {
        button.addEventListener('click', function () {
            const projectId = this.getAttribute('projectId');
            openProject(projectId);
        });
    });

    document.querySelectorAll('.editProjectButton').forEach(button => {
        button.addEventListener('click', function () {
            const projectId = this.getAttribute('projectId');
            editProject(projectId);
        });
    });

    document.querySelectorAll('.deleteProjectButton').forEach(button => {
        button.addEventListener('click', function () {
            const projectId = this.getAttribute('projectId');
            deleteProject(projectId);
        });
    });
});

function openProject(projectId) {
    console.log("Opening project with ID:", projectId);
    window.location.assign = `/Projects/${projectId}`; 
}

function editProject(projectId) {
    console.log("Editing project with ID:", projectId);
    window.location.assign = `/Admin/EditProject/${projectId}`;
}

function deleteProject(projectId) {
    console.log("Deleting project with ID:", projectId);
    if (confirm("Are you sure you want to delete this project?")) {
        fetch(`/Api/deleteProject/${projectId}`, {
            method: 'POST'
        })
        .then(response => response.text())
        .then(data => {
            console.log(data);
            location.reload();
        })
        .catch(error => console.error('Error:', error));
    }
}