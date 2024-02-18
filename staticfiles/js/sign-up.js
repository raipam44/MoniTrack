
    // Function to display errors dynamically
    function displayErrors(errors) {
      var errorContainer = document.getElementById('error-container');
      errorContainer.innerHTML = '<div class="alert alert-danger"><strong>Error(s):</strong><ul>';

      for (var i = 0; i < errors.length; i++) {
        errorContainer.innerHTML += '<li>' + errors[i] + '</li>';
      }

      errorContainer.innerHTML += '</ul></div>';

      // Add fade-out effect
      setTimeout(function () {
        errorContainer.innerHTML = '';
      }, 2000); // Adjust the duration (in milliseconds) as needed
    }

    // Attach an event listener to the form submission
    document.getElementById('register-form').addEventListener('submit', function (event) {
      // Check for form validity using HTML5 built-in checkValidity() method
      if (!event.target.checkValidity()) {
        // Prevent form submission
        event.preventDefault();

        // Extract and display detailed error messages
        var formElements = event.target.elements;
        var errors = [];

        for (var i = 0; i < formElements.length; i++) {
          if (!formElements[i].checkValidity()) {
            // Add the error message to the list
            errors.push(formElements[i].validationMessage);
          }
        }

        // Display errors dynamically
        displayErrors(errors);
      }
    });
