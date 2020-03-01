function scrollSmoothTo(elementId) {
    var element = document.getElementById(elementId);
    element.scrollIntoView({
        block: 'start',
        behavior: 'smooth'
    });
}

// JavaScript source code
var $input;

function onInputFocus(event) {
    var $target = $(event.target);
    var $parent = $target.parent();
    $parent.addClass('input--filled');
};

function onInputBlur(event) {
    var $target = $(event.target);
    var $parent = $target.parent();

    if (event.target.value.trim() === '') {
        $parent.removeClass('input--filled');
    }
};

$(document).ready(function () {
    $input = $('.input__field');

    // in case there is any value already
    $input.each(function () {
        if ($input.val().trim() !== '') {
            var $parent = $input.parent();
            $parent.addClass('input--filled');
        }
    });

    $input.on('focus', onInputFocus);
    $input.on('blur', onInputBlur);
});

jQuery(document).ready(function ($) {

    $('ul.filter li').click(function () {

        $("ul.filter li").removeClass("active");
        $(this).addClass("active");

        var selector = $(this).attr('data-filter');
        $(".gallery__projects").isotope({
            filter: selector,
            animationOptions: {
                duration: 750,
                easing: 'linear',
                queue: false,
            }
        });
        return false;
    });

    // init Isotope
    var $grid = $('.isotope__grid').isotope({
        itemSelector: '.gallery__item',
        percentPosition: true,
        layoutMode: 'fitRows',
        fitRows: {
            gutter: 20
        }
    });
    // layout Isotope after each image loads
    $grid.imagesLoaded().progress(function () {
        $grid.isotope('layout');
    });
});