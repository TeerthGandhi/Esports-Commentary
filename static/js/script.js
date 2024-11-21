$(document).ready(function () {
    $('.tooltipped').tooltip();
 });
 
 $(document).ready(function () {
    $('select').formSelect();
 });
 
 $(document).ready(function () {
    $('#submitForm').click(function (event) {
       event.preventDefault(); // Prevent the default form submission
 
       // Show success toast
       M.toast({
          html: 'Pocessing...',
          classes: 'rounded grey'
       });
 
       // Show the preloader and hide the form
       $('#preloader').show(); // Show preloader
 
       var formData = new FormData($('#ajaxForm')[0]); // Create FormData object from the form
 
       $.ajax({
          url: '{% url "upload" %}', // Replace with the URL to your Django view
          type: 'POST',
          data: formData,
          processData: false,
          contentType: false,
          success: function (response) {
             console.log('Form submitted successfully: ', response);
 
             // Show success toast
             //  M.toast({html: 'Form submitted successfully!', classes: 'rounded green'});
 
 
             // Hide the preloader
             $('#preloader').hide();
 
             // Check if the response is successful and contains the video URL
             if (response.status === 'success') {
 
                M.toast({
                   html: 'Successfully processed video',
                   classes: 'rounded green'
                });
 
                // Display the success button when the submission is successful
                $('#redoButton').fadeIn();
 
                // Hide the form and show the video card
                $('#form-container').hide();
                $('#video-card').show(); // Show the video card
                $('#video-iframe').attr('src', response.video_url).show(); // Set the video URL and show the iframe
             } else {
 
                // Show error toast with the response message
                M.toast({
                   html: 'Error: ' + response.message,
                   classes: 'rounded red'
                });
 
                // Show the form again on failure
                $('#form-container').show();
             }
          },
          error: function (xhr, status, error) {
             console.error('Form submission failed: ', error);
 
             // Show error toast
             M.toast({
                   html: 'Form submission failed! Please try again.',
                   classes: 'rounded red'
                });
 
             // Hide the preloader and show the form again on failure
             $('#preloader').hide();
             $('#form-container').show();
          }
       });
    });
 });
 