$(document).ready(function () {
   // Initialize modal triggers on the page load for the first set
   $('.modal').modal();

   // Functionality for the second set of cards and modals
   $('#create-div-btn-2').on('click', function () {
      // Generate unique IDs for the second card and modal
      var cardId2 = 'card-2-' + ($('.card-panel').length + 1);
      var modalId2 = 'modal-2-' + ($('.modal').length + 1);

      // Create the second card HTML
      var cardHtml2 = `
               <div class="col s12 m5">
                   <div id="${cardId2}" class="card-panel teal modal-trigger" data-target="${modalId2}">
                       <span class="white-text">
                           Other Company: 6 months
                           <br>Position: Developer
                           <br>Date: Jan 2023 – June 2023
                       </span>
                   </div>
               </div>
           `;

      // Create the second modal HTML with a unique ID and the form inside
      var modalHtml2 = `
           <div id="${modalId2}" class="modal modal-fixed-footer">
               <div class="modal-content">
                   <div id="newFormContainer${modalId2}">
                     <div class="row">
                        <form class="col s11 bordered-form">
                           <div class="col s12">
                              <p class="left">
                                 <a class="waves-effect waves-light" style="font-size:12px">
                                 <i class="material-icons left tiny">delete</i>Delete</a>
                                   
                                 <a class="waves-effect waves-light" style="font-size:12px">
                                 <i class="material-icons left tiny">open_with</i>Move</a>
                              </p>
                              <p class="right">
                                       <a class="waves-effect waves-light btn-small btn-custom blue" style="color:white;"><i class="material-icons left">save</i>Save</a>
                              </p>
                           </div>
                           <div class="">
                              <div class="input-field col s12">
                                 <i class="material-icons prefix">short_text</i>
                                 <div class="chips chip-heading-${modalId2}" id="chip_heading_${modalId2}" style="border-bottom: none;"></div>
                              </div>
                           </div>
                           <div class="">
                              <div class="input-field col s12">
                                 <i class="material-icons prefix">more_vert</i>
                                 <div class="chips chip-content-${modalId2}" id="chips_${modalId2}" style="border-bottom: none;"></div>
                              </div>
                           </div>
                        </form> 
                     </div>
                   </div>
               </div>
           </div>`;

      // Append the second card and modal to the second card container and the body respectively
      $('#card-container-2').append(cardHtml2);
      $('body').append(modalHtml2);

      // Reinitialize modal triggers for dynamically added modals
      $('.modal').modal();

      // Attach event to open the modal when the second card is clicked
      $('#' + cardId2).on('click', function () {
         var modalInstance = M.Modal.getInstance($('#' + modalId2));
         if (modalInstance) {
            modalInstance.open();
         }
      });

      // Initialize chips for the dynamically created chips containers in the new form
      initializeChipsForForm(modalId2);
   });

   // Function to initialize chips for a dynamically created form inside a modal
   function initializeChipsForForm(modalId) {
      var isChipAdded = false;

      // Initialize the main "heading" chip
      var chipInstanceHeading = $(`#chip_heading_${modalId}`).chips({
         data: [{
            tag: 'Heading'
         }],
         placeholder: 'Heading',
         secondaryPlaceholder: ' ',
         onChipAdd: function (chip) {
            if (!isChipAdded) {
               isChipAdded = true;
               $(`#chip_heading_${modalId}`).addClass('disabled'); // Adds disabled class to div
               $(`#chip_heading_${modalId}`).find('*').prop('disabled', true); // Disables all child elements

               $(`#chip_heading_${modalId}`).css('border-bottom', 'none');
               $(`#chip_heading_${modalId}`).find('*').css('border-bottom', 'none');
            } else {
               // Remove the newly added chip if another chip exists
               $(chip.tag).remove();
               alert('Only one chip allowed.');
            }
            console.log('Chip added:', chip);
            $(`#chip_heading_${modalId} .chip`).removeClass('chip').addClass('chip red white-text');
         },
         onChipDelete: function (chip) {
            isChipAdded = false;
            console.log('Chip deleted:', chip);
            $(`#chip_heading_${modalId}`).removeClass('disabled'); // Remove 'disabled' class
            $(`#chip_heading_${modalId}`).find('*').prop('disabled', false); // Re-enable all child elements
         }
      });

      // Initialize the "skills" chips
      var chipInstanceSkills = $(`#chips_${modalId}`).chips({
         data: [{
            tag: 'Skill 1'
         }, {
            tag: 'Skill 2'
         }],
         placeholder: 'Enter a skill',
         secondaryPlaceholder: '+Skill',
         onChipAdd: function (chip) {
            $(`#chips_${modalId} .chip`).removeClass('chip').addClass('chip blue white-text');
            console.log('Chip added:', chip);
         },
         onChipDelete: function (chip) {
            console.log('Chip deleted:', chip);
         }
      });

      // Ensure initial chips have the correct styles
      $(`#chip_heading_${modalId} .chip`).removeClass('chip').addClass('chip red white-text');
      $(`#chips_${modalId} .chip`).removeClass('chip').addClass('chip blue white-text');
   }
});


$(document).ready(function () {
   // Initialize modal triggers on the page load
   $('.modal').modal();

   // On button click, create and append the card and its modal
   $('#create-div-btn').on('click', function () {
      // Generate unique IDs for the card and modal
      var cardId = 'card' + ($('.card-panel').length + 1);
      var modalId = 'modal' + ($('.modal').length + 1);

      // Create the card HTML
      var cardHtml = `
               <div class="col s12 m5">
                   <div id="${cardId}" class="card-panel blue modal-trigger" data-target="${modalId}">
                       <span class="white-text">
                           Synapse: 3 months
                           <br>Position: Software Engineer
                           <br>Date: Jul 2023 – Sept 2023
                       </span>
                   </div>
               </div>
           `;

      // Create the modal HTML with a unique ID and the form inside
      var modalHtml = `
           <div id="${modalId}" class="modal modal-fixed-footer">
               <div class="modal-content">
                   <div id="newFormContainer${modalId}">
                     <div class="row">
                        <form class="col s12 experience-form-full">
                           <div class="col s12">
                              <p class="left">
                                 <a class="waves-effect waves-light btn-delete" style="font-size:12px">
                                       <i class="material-icons left tiny">delete</i>Delete
                                 </a>
                                 <!--   
                                 <a class="waves-effect waves-light btn-move" style="font-size:12px">
                                       <i class="material-icons left tiny">open_with</i>Move
                                 </a> -->
                              </p>
                              <p class="right">
                                 <!-- <a class="waves-effect waves-light btn-small btn-custom" style="width:200px"><i class="material-icons left">link</i>Import from linkedIn</a> -->
                                 <!-- <a class="waves-effect waves-light btn-small btn-custom red" style="color:white;width:140px"><i class="material-icons left">delete</i>Delete section</a> -->
                                 <a class="waves-effect waves-light btn-small btn-custom blue" style="color:white;"><i class="material-icons left">save</i>Save</a>
                              </p>
                           </div>
                           <div class="col s12">
                              <div class="input-field col s6">
                                 <i class="material-icons prefix">business</i>
                                 <input id="company" type="text" class="validate">
                                 <label for="company">Company</label>
                              </div>
                              <div class="input-field col s6">
                                 <i class="material-icons prefix">work</i>
                                 <input id="designation" type="text" class="validate">
                                 <label for="designation">Designation</label>
                              </div>
                              <div class="input-field col s6">
                                 <i class="material-icons prefix">date_range</i>
                                 <input id="from_date" type="text" class="validate">
                                 <label for="from_date">From Date</label>
                           </div>
                              <div class="input-field col s6">
                                 <i class="material-icons prefix">date_range</i>
                                 <input id="to_date" type="text" class="validate">
                                 <label for="to_date">To Date</label>
                              </div>
                           </div>
                           <div class="col s12">
                              <div class="input-field col s12">
                                 <i class="material-icons prefix">short_text</i>
                                 <textarea id="details" class="materialize-textarea"></textarea>
                                 <label for="details">Details</label>
                              </div>
                           </div>
                        </form>
                     </div>
                   </div>
               </div>
           </div>
           `;

      // Append the card and modal to the card container and the body respectively
      $('#card-container').append(cardHtml);
      $('body').append(modalHtml);

      // Reinitialize modal triggers for dynamically added modals
      $('.modal').modal();

      // Attach event to open the modal when the card is clicked (optional as it's triggered by data-target)
      $('#' + cardId).on('click', function () {
         var modalInstance = M.Modal.getInstance($('#' + modalId));
         if (modalInstance) {
            modalInstance.open();
         }
      });
   });
});


$(document).ready(function () {
   // the "href" attribute of the modal trigger must specify the modal ID that wants to be triggered
   $('.modal').modal();
});


$(document).ready(function () {

   // Add event listener for when the element with id 'exp' is clicked
   $('#exp').on('click', function () {

      $('#exp_tabs').tabs()

      console.log("here...");
      // $('#exp_tabs').tabs()
      console.log($('#exp_tabs').tabs());


   });


});


$(document).ready(function () {

   // Example: Click on active tab
   var $active = $('#table .tab a.active');

   console.log($active);
   console.log('.....');
   console.log($(this).parent());


   if ($active.length > 0) {
      var id = $(this).parent().attr('id');
      console.log(id);
      $('a[href="#' + id + '"]').trigger('click');
   }


});


$(document).ready(function () {

   // Initialize tabs if not already initialized
   var instance = M.Tabs.init($('#exp_tabs'));

   // Function to activate a specific tab by its ID
   function activateTab(tabId) {
      // Remove 'active' class from all tabs
      $('#exp_tabs .tab a').removeClass('active');

      // Add 'active' class to the specified tab
      $('#' + tabId).addClass('active');

      //   // Use MaterializeCSS's method to select the tab and display its content
      //   instance.select('#' + tabId);

      // Programmatically click the tab to activate it
      $('a[href="#' + tabId + '"]').trigger('click');

   }

   // Example: Activate the "Test 2" tab
   activateTab('test1');


});

$(document).ready(function () {
   // Initialize main tabs
   $('#main_tabs').tabs();

   // Initialize sub tabs
   $('#exp_tabs').tabs();

   $('#add-tab').on('click', function (e) {
      e.preventDefault();

      // Generate new tab id and content
      var newTabId = 'test' + ($('#exp_tabs li.tab').length + 1);
      var newTabContent = 'Content for ' + newTabId;

      // Create new tab
      var newTab = $('<li class="tab col s3"><a href="#' + newTabId + '">' + newTabId + '</a></li>');
      $('#add-tab-container').before(newTab);

      // Create new tab content
      var newTabDiv = $('<div id="' + newTabId + '" class="col s12">' + newTabContent + '</div>');
      $('#exp_div').append(newTabDiv);


   });


});


$(document).ready(function () {
   $("#draggable").draggable();

});


$(document).ready(function () {
   $('#addFormBtn').click(function () {
      var formCount = $('#newFormContainer').children('form').length + 1;

      var newForm = $('<form>').addClass('col s11 experience-form-full');

      newForm.html(`
                   <!-- Your existing form content -->
                   
                   <div class="col s12">
                       <p class="left">
                           <a class="waves-effect waves-light btn-delete" style="font-size:12px">
                               <i class="material-icons left tiny">delete</i>Delete
                           </a>
                             
                           <a class="waves-effect waves-light btn-move" style="font-size:12px">
                               <i class="material-icons left tiny">open_with</i>Move
                           </a>
                       </p>
                   </div>
                   <div>
                       <div class="input-field col s6">
                           <i class="material-icons prefix">business</i>
                           <input id="company${formCount}" type="text" class="validate">
                           <label for="company${formCount}">Company</label>
                       </div>
                       <div class="input-field col s6">
                           <i class="material-icons prefix">work</i>
                           <input id="designation${formCount}" type="text" class="validate">
                           <label for="designation${formCount}">Designation</label>
                       </div>
                   </div>
                   <div>
                       <div class="input-field col s12">
                           <i class="material-icons prefix">date_range</i>
                           <input id="date${formCount}" type="text" class="validate">
                           <label for="date${formCount}">Date</label>
                       </div>
                   </div>
                   <div>
                       <div class="input-field col s12">
                           <i class="material-icons prefix">short_text</i>
                           <textarea id="details${formCount}" class="materialize-textarea"></textarea>
                           <label for="details${formCount}">Details</label>
                       </div>
                   </div>
               `);

      $('#newFormContainer').append(newForm);
   });
});


$(document).ready(function () {
   $('.collapsible').collapsible();

   $('.collapsible-header').on('click', function () {
      var targetId = $(this).data('target');
      $('.card-container').each(function () {
         if ($(this).attr('id') === targetId) {
            $(this).show();
         } else {
            $(this).hide();
         }
      });
   });
});


$(document).ready(function () {
   // Initialize the sidenav
   $('.sidenav').sidenav();

   // Add click event to the logo
   $('#logo').click(function (e) {
      e.preventDefault(); // Prevent the default action
      $('.sidenav').sidenav('open'); // Open the sidenav
   });
});


$(document).ready(function () {
   $('.parallax').parallax();
});


$(document).ready(function () {
   var chipInstance = $('#chips').chips({
      data: [{
            tag: 'Skill 1'
         },
         {
            tag: 'Skill 2'
         },
      ],
      placeholder: 'Enter a skill',
      secondaryPlaceholder: '+Skill',
      onChipAdd: function (chip) {

         $('#chips .chip').removeClass('chip').addClass('chip blue white-text');
         console.log('Chip added:', chip);
      },
      onChipDelete: function (chip) {
         console.log('Chip deleted:', chip);
      }
   });

   $('#chips .chip').removeClass('chip').addClass('chip blue white-text');

});


$(document).ready(function () {
   var isChipAdded = false;

   var chipInstance = $('#chip_heading').chips({

      data: [{
         tag: 'Heading'
      }, ],
      placeholder: 'Heading',
      secondaryPlaceholder: ' ',
      onChipAdd: function (chip) {
         if (!isChipAdded) {
            isChipAdded = true;
            $('#chip_heading').addClass('disabled'); // Adds disabled class to div
            $('#chip_heading').find('*').prop('disabled', true); // Disables all child elements

            $('#chip_heading').css('border-bottom', 'none');
            $('#chip_heading').find('*').css('border-bottom', 'none');


         } else {
            // Remove the newly added chip if another chip exists
            $(chip.tag).remove();
            alert('Only one chip allowed.');
         }
         console.log('Chip added:', chip);
         $('#chip_heading .chip').removeClass('chip').addClass('chip red white-text');

      },
      onChipDelete: function (chip) {
         isChipAdded = false;
         console.log('Chip deleted:', chip);
         $('#chip_heading').removeClass('disabled'); // Remove 'disabled' class from #chip_heading
         $('#chip_heading').find('*').prop('disabled', false); // Disables all child elements


      }
   });

   $('#chip_heading .chip').removeClass('chip').addClass('chip red white-text');


});


document.addEventListener('DOMContentLoaded', function () {
   const elem = document.querySelector('.image-row');
   const instance = M.Carousel.init(elem, {
      fullWidth: true,
      indicators: true
   });

   document.getElementById('prevBtn').addEventListener('click', function () {
      const instance = M.Carousel.getInstance(elem);
      instance.prev();
   });

   document.getElementById('nextBtn').addEventListener('click', function () {
      const instance = M.Carousel.getInstance(elem);
      instance.next();
   });
});



// new ones

// document.getElementById('submitButton').addEventListener('click', function() {
//    alert("here...");
//    document.getElementById('summary_form').submit();
// });


// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        // Serialize the form data
//        var formData = $('#summary_form').serialize();
//       console.log("here...1");
//        $.ajax({
//            type: 'POST',
//            url: "{% url 'summary' %}",  // Ensure this URL matches your Django URL pattern
//            data: formData,
//            success: function(response) {
//                // Handle a successful response (e.g., redirect or display a message)
//       console.log("here...2");

//                window.location.href = "success_url";  // Replace with your success URL
//            },
//            error: function(xhr, status, error) {
//                // Handle error response (optional)
//                alert('An error occurred: ' + xhr.responseText);
//            }
//        });
//    });
// });


// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        var formData = $('#summary_form').serialize();
//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': '{{ csrf_token }}'  // Include CSRF token
//            }
//        });

//        $.ajax({
//            type: 'POST',
//            url: "{% url 'summary' %}",  // Ensure this is the correct URL
//            data: formData,
//            success: function(response) {
//                if (response.success) {
//                    window.location.href = "success_url";  // Replace with your success URL
//                } else {
//                    // Handle validation errors
//                    alert('Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred: ' + xhr.responseText);
//            }
//        });
//    });
// });


// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        var formData = $('#summary_form').serialize();

//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': '{{ csrf_token }}'  // If using CSRF token, pass it in your HTML or handle it in the setup
//            }
//        });

//        $.ajax({
//            type: 'POST',
//            url: summaryFormUrl,  // Use the rendered URL variable
//            data: formData,
//            success: function(response) {
//                if (response.success) {
//                   alert("here..1");

//                   //  window.location.href = "success_url";  // Replace with your success URL
//                } else {
//                    // Handle validation errors
//                    alert('Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred: ' + xhr.responseText);
//            }
//        });
//    });
// });



// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        var formData = $('#profile_form').serialize();

//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': csrfToken  // Use the passed CSRF token
//            }
//        });

//        $.ajax({
//            type: 'POST',
//            url: profileFormUrl,  // Use the rendered URL variable
//            data: formData,
//            success: function(response) {
//                if (response.success) {
//                   alert("here..2");
//                   //  window.location.href = "success_url";  // Replace with your success URL
//                } else {
//                    // Handle validation errors
//                    alert('Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred: ' + xhr.responseText);
//            }
//        });
//    });
// });



// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        // Serialize both forms
//        var summaryFormData = $('#summary_form').serialize();
//        var profileFormData = $('#profile_form').serialize();

//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': csrfToken  // Use the passed CSRF token
//            }
//        });

//        // Send AJAX request for SummaryForm
//        $.ajax({
//            type: 'POST',
//            url: summaryFormUrl,  // Use the rendered URL variable for summary form
//            data: summaryFormData,  // Send combined data
//            success: function(response) {
//                if (response.success) {
//                    alert("Summary Form Submitted!");
//                } else {
//                    // Handle validation errors for SummaryForm
//                    alert('Summary Form Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred: ' + xhr.responseText);
//            }
//        });

//        // Send AJAX request for ProfileForm
//        $.ajax({
//            type: 'POST',
//            url: profileFormUrl,  // Use the rendered URL variable for profile form
//            data: profileFormData,  // Send combined data
//            success: function(response) {
//                if (response.success) {
//                    alert("Profile Form Submitted!");
//                } else {
//                    // Handle validation errors for ProfileForm
//                    alert('Profile Form Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred: ' + xhr.responseText);
//            }
//        });
//    });
// });



// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        // Serialize both forms
//        var profileFormData = $('#profile_form').serialize();
//        var summaryFormData = $('#summary_form').serialize();
//        var fileUploadData = new FormData($('#fileUploadForm')[0]);

//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': csrfToken  // Use the passed CSRF token
//            }
//        });


//        // Send AJAX request for ProfileForm
//        $.ajax({
//          type: 'POST',
//          url: profileFormUrl,  // Use the rendered URL variable for profile form
//          data: profileFormData,  // Send profile form data
//          success: function(response) {
//              if (response.success) {
//                  alert("Profile Form Submitted!");
//              } else {
//                  alert('Profile Form Errors: ' + JSON.stringify(response.errors));
//              }
//          },
//          error: function(xhr, status, error) {
//              alert('An error occurred with the Profile Form: ' + xhr.responseText);
//          }
//      });



//        // Send AJAX request for SummaryForm
//        $.ajax({
//            type: 'POST',
//            url: summaryFormUrl,  // Use the rendered URL variable for summary form
//            data: summaryFormData,  // Send summary form data
//            success: function(response) {
//                if (response.success) {
//                    alert("Summary Form Submitted!");
//                } else {
//                    alert('Summary Form Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred with the Summary Form: ' + xhr.responseText);
//            }
//        });

//        // Send AJAX request for File Upload
//        $.ajax({
//            type: 'POST',
//            url: fileUploadUrl,  // Use the rendered URL variable for file upload
//            data: fileUploadData,  // Send file upload data
//            processData: false,  // Important for file uploads
//            contentType: false,  // Important for file uploads
//            success: function(response) {
//                if (response.success) {
//                    alert("File Uploaded Successfully!");
//                } else {
//                    alert('File Upload Errors: ' + JSON.stringify(response.errors));
//                }
//            },
//            error: function(xhr, status, error) {
//                alert('An error occurred with the File Upload: ' + xhr.responseText);
//            }
//        });
//    });

   
// });


// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        // Serialize both forms
//        var profileFormData = $('#profile_form').serialize();
//        var summaryFormData = $('#summary_form').serialize();
//        var fileUploadData = new FormData($('#fileUploadForm')[0]);

//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': csrfToken  // Use the passed CSRF token
//            }
//        });

//        // Send AJAX request for ProfileForm
//        $.ajax({
//          type: 'POST',
//          url: profileFormUrl,  // Use the rendered URL variable for profile form
//          data: profileFormData,  // Send profile form data
//          success: function(response) {
//              if (response.success) {
//                  var $toastContent = $('<span>Profile Form Submitted Successfully!</span>');
//                  M.toast({html: $toastContent, displayLength: 5000});
//              } else {
//                  var $toastContent = $('<span>Profile Form Errors: ' + JSON.stringify(response.errors) + '</span>');
//                  M.toast({html: $toastContent, displayLength: 5000});
//              }
//          },
//          error: function(xhr, status, error) {
//              var $toastContent = $('<span>An error occurred with the Profile Form: ' + xhr.responseText + '</span>');
//              M.toast({html: $toastContent, displayLength: 5000});
//          }
//        });

//        // Send AJAX request for SummaryForm
//        $.ajax({
//            type: 'POST',
//            url: summaryFormUrl,  // Use the rendered URL variable for summary form
//            data: summaryFormData,  // Send summary form data
//            success: function(response) {
//                if (response.success) {
//                    var $toastContent = $('<span>Summary Form Submitted Successfully!</span>');
//                    M.toast({html: $toastContent, displayLength: 5000});
//                } else {
//                    var $toastContent = $('<span>Summary Form Errors: ' + JSON.stringify(response.errors) + '</span>');
//                    M.toast({html: $toastContent, displayLength: 5000});
//                }
//            },
//            error: function(xhr, status, error) {
//                var $toastContent = $('<span>An error occurred with the Summary Form: ' + xhr.responseText + '</span>');
//                M.toast({html: $toastContent, displayLength: 5000});
//            }
//        });

//        // Send AJAX request for File Upload
//        $.ajax({
//            type: 'POST',
//            url: fileUploadUrl,  // Use the rendered URL variable for file upload
//            data: fileUploadData,  // Send file upload data
//            processData: false,  // Important for file uploads
//            contentType: false,  // Important for file uploads
//            success: function(response) {
//                if (response.success) {
//                    var $toastContent = $('<span>File Uploaded Successfully!</span>');
//                    M.toast({html: $toastContent, displayLength: 5000});
//                } else {
//                    var $toastContent = $('<span>File Upload Errors: ' + JSON.stringify(response.errors) + '</span>');
//                    M.toast({html: $toastContent, displayLength: 5000});
//                }
//            },
//            error: function(xhr, status, error) {
//                var $toastContent = $('<span>An error occurred with the File Upload: ' + xhr.responseText + '</span>');
//                M.toast({html: $toastContent, displayLength: 5000});
//            }
//        });
//    });
// });


// $(document).ready(function() {
//    $('#submitButton').on('click', function() {
//        // Serialize both forms
//        var profileFormData = $('#profile_form').serialize();
//        var summaryFormData = $('#summary_form').serialize();
//        var fileUploadData = new FormData($('#fileUploadForm')[0]);

//        $.ajaxSetup({
//            headers: {
//                'X-CSRFToken': csrfToken  // Use the passed CSRF token
//            }
//        });

//        // Function to show toast with success or failure and text color
//        function showToast(message, isSuccess) {
//            var colorClass = isSuccess ? 'green-text' : 'red-text';  // Green for success text, red for failure text
//            var $toastContent = $('<span>' + '<span class="' + colorClass + '">' + message + '</span>' + '</span>');
//            M.toast({html: $toastContent, displayLength: 5000});
//        }

//        // Send AJAX request for ProfileForm
//        $.ajax({
//          type: 'POST',
//          url: profileFormUrl,  // Use the rendered URL variable for profile form
//          data: profileFormData,  // Send profile form data
//          success: function(response) {
//              if (response.success) {
//                  showToast("Profile Form Submitted Successfully!", true);
//              } else {
//                  showToast('Profile Form Errors: ' + JSON.stringify(response.errors), false);
//              }
//          },
//          error: function(xhr, status, error) {
//              showToast('An error occurred with the Profile Form: ' + xhr.responseText, false);
//          }
//        });

//        // Send AJAX request for SummaryForm
//        $.ajax({
//            type: 'POST',
//            url: summaryFormUrl,  // Use the rendered URL variable for summary form
//            data: summaryFormData,  // Send summary form data
//            success: function(response) {
//                if (response.success) {
//                    showToast("Summary Form Submitted Successfully!", true);
//                } else {
//                    showToast('Summary Form Errors: ' + JSON.stringify(response.errors), false);
//                }
//            },
//            error: function(xhr, status, error) {
//                showToast('An error occurred with the Summary Form: ' + xhr.responseText, false);
//            }
//        });

//        // Send AJAX request for File Upload
//        $.ajax({
//            type: 'POST',
//            url: fileUploadUrl,  // Use the rendered URL variable for file upload
//            data: fileUploadData,  // Send file upload data
//            processData: false,  // Important for file uploads
//            contentType: false,  // Important for file uploads
//            success: function(response) {
//                if (response.success) {
//                    showToast("File Uploaded Successfully!", true);
//                } else {
//                    showToast('File Upload Errors: ' + JSON.stringify(response.errors), false);
//                }
//            },
//            error: function(xhr, status, error) {
//                showToast('An error occurred with the File Upload: ' + xhr.responseText, false);
//            }
//        });
//    });
// });


$(document).ready(function() {
   $('#submitButton').on('click', function() {
       // Serialize both forms
       var profileFormData = $('#profile_form').serialize();
       var summaryFormData = $('#summary_form').serialize();
       var fileUploadData = new FormData($('#fileUploadForm')[0]);

       $.ajaxSetup({
           headers: {
               'X-CSRFToken': csrfToken  // Use the passed CSRF token
           }
       });

       // Function to show toast with colored "Success" or "Failure" and a white message
       function showToast(isSuccess, message) {
           var statusText = isSuccess ? 'Success' : 'Failure';
           var colorClass = isSuccess ? 'yellow-text' : 'orange-text';  // Green for success text, red for failure text
           var $toastContent = $('<span><span class="' + colorClass + '">' + statusText + '</span>: ' + message + '</span>');
         //   M.toast({html: $toastContent, displayLength: 5000});
           M.toast({html: $toastContent, displayLength: 5000, classes: 'rounded'});
       }

       // Send AJAX request for ProfileForm
       $.ajax({
         type: 'POST',
         url: profileFormUrl,  // Use the rendered URL variable for profile form
         data: profileFormData,  // Send profile form data
         success: function(response) {
             if (response.success) {
                 showToast(true, "Profile Form Submitted Successfully!");
             } else {
                 showToast(false, 'Profile Form Errors: ' + JSON.stringify(response.errors));
             }
         },
         error: function(xhr, status, error) {
             showToast(false, 'An error occurred with the Profile Form: ' + xhr.responseText);
         }
       });

       // Send AJAX request for SummaryForm
       $.ajax({
           type: 'POST',
           url: summaryFormUrl,  // Use the rendered URL variable for summary form
           data: summaryFormData,  // Send summary form data
           success: function(response) {
               if (response.success) {
                   showToast(true, "Summary Form Submitted Successfully!");
               } else {
                   showToast(false, 'Summary Form Errors: ' + JSON.stringify(response.errors));
               }
           },
           error: function(xhr, status, error) {
               showToast(false, 'An error occurred with the Summary Form: ' + xhr.responseText);
           }
       });

       // Send AJAX request for File Upload
       $.ajax({
           type: 'POST',
           url: fileUploadUrl,  // Use the rendered URL variable for file upload
           data: fileUploadData,  // Send file upload data
           processData: false,  // Important for file uploads
           contentType: false,  // Important for file uploads
           success: function(response) {
               if (response.success) {
                   showToast(true, "File Uploaded Successfully!");
               } else {
                   showToast(false, 'File Upload Errors: ' + JSON.stringify(response.errors));
               }
           },
           error: function(xhr, status, error) {
               showToast(false, 'An error occurred with the File Upload: ' + xhr.responseText);
           }
       });
   });
});


$(document).ready(function(){
   $('.materialboxed').materialbox();
 });
     