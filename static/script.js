// script.js
document.getElementById('messageForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const messageElement = document.getElementById('message');
    const chatBox = document.getElementById('chat-box');

    // Append user message
    const userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'user-message';
    userMessageDiv.textContent = messageElement.value;
    chatBox.appendChild(userMessageDiv);

    fetch('/process', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: messageElement.value }),
    })
        .then(response => response.json())
        .then(data => {
            // Append bot message
            const botMessageDiv = document.createElement('div');
            botMessageDiv.className = 'bot-message';
            botMessageDiv.textContent = data.message;
            chatBox.appendChild(botMessageDiv);

            // Scroll to the bottom of the chat box
            chatBox.scrollTop = chatBox.scrollHeight;

            // Clear the input field
            messageElement.value = '';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
});

