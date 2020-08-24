$('document').ready(function(){

    var form = $('#add_to_korz');

    form.on('submit', function(e){
        e.preventDefault();
        var nmb = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");

        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#add_to_korz [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");

        //console.log(data)

         $.ajax({
             url: url,
             type: 'POST',
             data: data,
             cache: true,
             success: function (data) {
                 console.log("OK");
                 console.log(data.products_total_nmb);
                 if (data.products_total_nmb || data.products_total_nmb == 0){
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                     $('.basket-items ul').html("");
                     $.each(data.products, function(k, v){
                        $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + 'шт. ' + 'по ' + v.price_per_item + 'грн  ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                            '</li>');
                     });
                 }

             },
             error: function(){
                 console.log("error")
             }
         })

        $('.korz_item ul').append('<li>'+name+', ' + nmb + 'шт. ' + 'по ' + price + 'грн  ' +
            '<a class="delete-item" href="">x</a>'+
            '</li>');
    });

     $('.nav_korz').mouseover(function(){
         $('.korz_item').removeClass('hidden');
     });
     $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         $(this).closest('li').remove();
     })
});