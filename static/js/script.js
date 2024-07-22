document.addEventListener('DOMContentLoaded', () => {
    // Select all message elements
    const messages = document.querySelectorAll('#alert-msg');
    
    // Loop through each message element
    messages.forEach((message) => {
        // Set a timeout to hide the message after 3 seconds (3000 milliseconds)
        setTimeout(() => {
            message.style.display = 'none';
        }, 3000); // Change this value to adjust the display duration
    });
});