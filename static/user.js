document.addEventListener('DOMContentLoaded', function() {


let logoutTimer;

function resetLogoutTimer() {
    clearTimeout(logoutTimer);
    logoutTimer = setTimeout(logoutUser, 1.8e+6); // 10 minutes in milliseconds
}

function logoutUser() {
    // Perform logout actions
    window.location.href = '/logout';
}

// Attach event listeners to user activity events (e.g., mousemove, keypress)
document.addEventListener('mousemove', handleUserActivity);
document.addEventListener('keypress', handleUserActivity);

// Attach event listener for beforeunload (when the user is about to leave the page)
// window.addEventListener('beforeunload', handleBeforeUnload);

// Start the timer when the page loads
resetLogoutTimer();

// Function to handle user activity
function handleUserActivity() {
    resetLogoutTimer();
    console.log("hello")
}

// Function to handle beforeunload event
// function handleBeforeUnload(event) {
//     // You can perform additional checks or actions here if needed
//     // For example, ask the user if they really want to leave the page
//     // Uncomment the line below if you want to show a confirmation dialog
//     event.returnValue = 'Are you sure you want to leave?';
    
//     // Perform logout actions
//     logoutUser();
// }



});