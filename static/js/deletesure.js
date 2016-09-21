jQuery(document).ready(function($) {
      $( function() {
    $( "#dialog" ).dialog({
      resizable: false,
        autoOpen: false,
      height: "auto",
      width: 400,
      modal: true,
      buttons: {
        "Pašalinti": function() {
          $( this ).dialog( "close" );
        },
        "atgal": function() {
          $( this ).dialog( "close" );
        }
      }
    });
    });

    $("i.fa-trash").click( function () {
        $("#dialog").dialog('open');
    });

});

