// dashboard-script.js

document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the feedback button
    var feedbackButton = document.getElementById('feedbackButton');

    if (feedbackButton) {
        feedbackButton.addEventListener('click', function() {
            // Change button text to provide visual feedback
            this.textContent = 'Feedback Submitted!';
        });
    }
});
