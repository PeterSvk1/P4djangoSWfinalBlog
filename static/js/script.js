document.addEventListener('DOMContentLoaded', function() {
    var messages = document.querySelectorAll('#alert-msg');
    
    Array.prototype.forEach.call(messages, function(message) {
        setTimeout(function() {
            message.style.display = 'none';
        }, 3000);
    });
});