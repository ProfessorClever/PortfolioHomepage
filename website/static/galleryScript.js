document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('uploadImageForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData(this);
        
        fetch('/Api/uploadImage', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(message => {
            document.getElementById('responseMessage').innerText = message;
        })
        .catch(error => {
            document.getElementById('responseMessage').innerText = 'An error occurred while sending the message.';
            console.error('Error:', error);
        });
    });
});