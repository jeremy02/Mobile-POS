$(document).ready(function(){
    $("#device_register_button").click(function() {
        var device_serial_code,device_name;
        device_serial_code = $("#device_serial_code").val();
        device_name = $("#device_name").val();

        $.ajax({
            type: "POST",
            url: "/nauri/device_register/",
            data: $('#device_registration').serialize(),
            success: function (response)
                {
                    $('#modal_device').html(response);
                    $('#device_serial_code').val('');
                    $('#device_name').val('');
                },
            error:function(data) {
                    $('#modal_device').html(data);
                    $(document).find('.form-control').attr('id', 'has');
                }
            //dataType: 'html'
        });
        return false;
    });

    //$(function() {
        //$('#pos_messages').fadeIn(1500).delay(3500);//.fadeOut(1500);
        $('#nauri_messages').fadeIn('slow', 'swing', function(){
            //alert('fadeOut complete');
        }).delay(2000).fadeOut(1500, 'swing', function(){
            //alert('fadeOut complete');
        });
    //});

    //dealing with device user assignment//show the list of unassigned devices

});


