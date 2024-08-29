document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("newTagForm").addEventListener("submit", function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        
        fetch('/Api/createTag', {
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
});