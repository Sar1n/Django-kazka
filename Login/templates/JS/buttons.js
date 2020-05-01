
    
  alert("This alert box was called with the onload event");
    
    
    $('#btn-add').click
    (
        function()
        {
            $.ajax
            (
                {
                    url: "ajax/testadd/",
                    type: "POST",
                    success: function()
                    {
                        alert("good");
                    }
                }
            )
        .fail(function() {
         alert("fail");
        });
        }
    );