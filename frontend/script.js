// Configuration
const API_BASE_URL = 'http://localhost:5000/api';

// DOM Elements
const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const clearButton = document.getElementById('clearButton');
const charCount = document.getElementById('charCount');
const statusIndicator = document.getElementById('statusIndicator');
const statusText = document.getElementById('statusText');

// State
let isProcessing = false;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    checkServerHealth();
    setupEventListeners();
});

// Event Listeners
function setupEventListeners() {
    // Send button click
    sendButton.addEventListener('click', sendMessage);

    // Enter key to send (Shift+Enter for new line)
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });

    // Auto-resize textarea
    userInput.addEventListener('input', () => {
        autoResizeTextarea();
        updateCharCount();
    });

    // Clear history button
    clearButton.addEventListener('click', clearHistory);
}

// Auto-resize textarea based on content
function autoResizeTextarea() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 120) + 'px';
}

// Update character count
function updateCharCount() {
    const count = userInput.value.length;
    charCount.textContent = count;

    if (count > 450) {
        charCount.style.color = '#ef4444';
    } else {
        charCount.style.color = '#94a3b8';
    }
}

// Check server health
async function checkServerHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();

        if (data.status === 'healthy') {
            updateStatus('online', `Online • ${data.stats.total_documents} docs loaded`);
        } else {
            updateStatus('error', 'Server Error');
        }
    } catch (error) {
        console.error('Health check failed:', error);
        updateStatus('error', 'Offline');
    }
}

// Update status indicator
function updateStatus(status, text) {
    statusText.textContent = text;

    if (status === 'online') {
        statusIndicator.classList.remove('error');
    } else if (status === 'error') {
        statusIndicator.classList.add('error');
    }
}

// Send message
async function sendMessage() {
    const message = userInput.value.trim();

    if (!message || isProcessing) return;

    // Clear input
    userInput.value = '';
    autoResizeTextarea();
    updateCharCount();

    // Remove welcome message if it exists
    const welcomeMsg = document.querySelector('.welcome-message');
    if (welcomeMsg) {
        welcomeMsg.remove();
    }

    // Add user message to chat
    addMessage(message, 'user');

    // Show typing indicator
    const typingId = showTypingIndicator();

    // Disable send button
    isProcessing = true;
    sendButton.disabled = true;

    try {
        // Send to API
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message })
        });

        if (!response.ok) {
            throw new Error('Failed to get response');
        }

        const data = await response.json();

        // Remove typing indicator
        removeTypingIndicator(typingId);

        // Add assistant response
        addMessage(data.response, 'assistant');

    } catch (error) {
        console.error('Error sending message:', error);
        removeTypingIndicator(typingId);
        addMessage('Sorry, I encountered an error. Please make sure the backend server is running.', 'assistant');
    } finally {
        // Re-enable send button
        isProcessing = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}

// Add message to chat
function addMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;

    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = text;

    messageDiv.appendChild(contentDiv);
    chatContainer.appendChild(messageDiv);

    // Scroll to bottom
    scrollToBottom();
}

// Show typing indicator
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    const id = 'typing-' + Date.now();
    typingDiv.id = id;
    typingDiv.className = 'message assistant';

    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = `
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    `;

    typingDiv.appendChild(indicator);
    chatContainer.appendChild(typingDiv);
    scrollToBottom();

    return id;
}

// Remove typing indicator
function removeTypingIndicator(id) {
    const element = document.getElementById(id);
    if (element) {
        element.remove();
    }
}

// Scroll to bottom of chat
function scrollToBottom() {
    chatContainer.scrollTo({
        top: chatContainer.scrollHeight,
        behavior: 'smooth'
    });
}

// Clear conversation history
async function clearHistory() {
    if (!confirm('Are you sure you want to clear the conversation history?')) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/clear-history`, {
            method: 'POST'
        });

        if (response.ok) {
            // Clear chat UI
            chatContainer.innerHTML = `
                <div class="welcome-message">
                    <h2>👋 Hello, I'm Jarvis</h2>
                    <p>Your intelligent AI assistant powered by advanced language models and semantic search.</p>
                    <p>I can help you with information about products, services, and answer your questions using my knowledge base.</p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error clearing history:', error);
        alert('Failed to clear history');
    }
}
