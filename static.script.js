document.getElementById('text-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const inputBox = document.getElementById('message-input');
    const message = inputBox.value.trim();
    if (message) {
        addMessageToChat('You', message, 'user-message');
        fetch('/', {
            method: 'POST',
            body: new URLSearchParams(`question=${message}`),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        })
        .then(response => response.json())
        .then(data => {
            addMessageToChat('Bot', data.response, 'bot-message');
        })
        .catch(error => {
            addMessageToChat('Bot', 'Error getting response.', 'bot-message');
        });
        inputBox.value = '';
        inputBox.focus();
    }
});

function addMessageToChat(sender, message, type) {
    const chatBox = document.getElementById('chat-content');
    const messageWrapper = document.createElement('div');
    messageWrapper.classList.add('message');

    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    messageElement.classList.add(type); // Apply specific styles

    messageWrapper.appendChild(messageElement);
    chatBox.appendChild(messageWrapper);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

