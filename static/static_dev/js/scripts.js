$(document).ready(function(){
    var form = $('#form_buying_product');

    function basketUpdating(product_id, num, is_delete){
        var data = {};
        data.product_id = product_id;
        data.num = num;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }

        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                if (data.products_total_num || data.products_total_num ==0 ){
                    $('#basket_total_num').text("("+data.products_total_num+")");
                    $('.basket-items ul').html("");
                    $.each(data.products, function(k, v){
                        $('.basket-items ul').append('<li>'+ v.name+' * ' + v.num + ' = ' + v.total_price + ' Руб' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">X</a>'+
                            '</li>');
                     });
                }
            },
            error: function(){
                console.log("error")
            }
        });
    };

    form.on('submit', function(e){
        e.preventDefault();
        var num = $('#number').val();
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");

        basketUpdating(product_id, num, is_delete=false);
    });

    $('.basket-container').on('click', function(e){
        e.preventDefault();
        $('.basket-items').removeClass('d-none');
    });

    $('.basket-container').mouseover(function(){
        $('.basket-items').removeClass('d-none');
    });

    //$('.basket-container').mouseout(function(){
    //    $('.basket-items').addClass('d-none');
    //});

    $(document).on('click', '.delete-item', function(e){
        e.preventDefault();
        product_id = $(this).data("product_id");
        num = 0;
        basketUpdating(product_id, num, is_delete=true);
    });


    function calculatingBasketAmount(){
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function(){
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        $('#total_order_amount').text(total_order_amount);
    };


    $(document).on('change', '.product-in-basket-num', function(){
        var current_num = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = parseFloat(current_num * current_price).toFixed(2);
        current_tr.find('.total-product-in-basket-amount').text(total_amount + " руб");
        calculatingBasketAmount();
    });

    calculatingBasketAmount();

});