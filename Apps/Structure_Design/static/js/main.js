(function($) {
	"use strict"

	// Mobile Nav toggle
	$('.menu-toggle > a').on('click', function (e) {
		e.preventDefault();
		$('#responsive-nav').toggleClass('active');
	})

	// Fix cart dropdown from closing
	$('.cart-dropdown').on('click', function (e) {
		e.stopPropagation();
	});

	/////////////////////////////////////////

	// project Slick
	$('.project-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			slidesToShow: 4,
			slidesToScroll: 1,
			autoplay: true,
			infinite: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
			responsive: [{
	        breakpoint: 991,
	        settings: {
	          slidesToShow: 2,
	          slidesToScroll: 1,
	        }
	      },
	      {
	        breakpoint: 480,
	        settings: {
	          slidesToShow: 1,
	          slidesToScroll: 1,
	        }
	      },
	    ]
		});
	});

	// project Widget Slick
	$('.project-widget-slick').each(function() {
		var $this = $(this),
				$nav = $this.attr('data-nav');

		$this.slick({
			infinite: true,
			autoplay: true,
			speed: 300,
			dots: false,
			arrows: true,
			appendArrows: $nav ? $nav : false,
		});
	});

	/////////////////////////////////////////

	// project Main img Slick
	$('#project-main-img').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    infinite: true,
    speed: 300,
    dots: false,
    arrows: true,
    fade: true,
    asNavFor: '#project-imgs',
  });

	// project imgs Slick
  $('#project-imgs').slick({
    slidesToShow: 2,
    slidesToScroll: 1,
    arrows: true,
    centerMode: true,
    focusOnSelect: true,
		centerPadding: 0,
		vertical: true,
    asNavFor: '#project-main-img',
		responsive: [{
        breakpoint: 991,
        settings: {
					vertical: false,
					arrows: false,
					dots: true,
        }
      },
    ]
  });


	// project img zoom
	var zoomMainproject = document.getElementById('project-main-img');
	if (zoomMainproject) {
		$('#project-main-img .project-preview').zoom();
	}

	/////////////////////////////////////////

	// Input number
	$('.input-number').each(function() {
		var $this = $(this),
		$input = $this.find('input[type="number"]'),
		up = $this.find('.qty-up'),
		down = $this.find('.qty-down');

		down.on('click', function () {
			var value = parseInt($input.val()) - 1;
			value = value < 1 ? 1 : value;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})

		up.on('click', function () {
			var value = parseInt($input.val()) + 1;
			$input.val(value);
			$input.change();
			updatePriceSlider($this , value)
		})
	});

	var priceInputMax = document.getElementById('price-max'),
			priceInputMin = document.getElementById('price-min');

	priceInputMax.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	priceInputMin.addEventListener('change', function(){
		updatePriceSlider($(this).parent() , this.value)
	});

	function updatePriceSlider(elem , value) {
		if ( elem.hasClass('price-min') ) {
			console.log('min')
			priceSlider.noUiSlider.set([value, null]);
		} else if ( elem.hasClass('price-max')) {
			console.log('max')
			priceSlider.noUiSlider.set([null, value]);
		}
	}

	// Price Slider
document.addEventListener('DOMContentLoaded', function () {
    var priceSlider = document.getElementById('price-slider');
    noUiSlider.create(priceSlider, {
        start: [1, 40000], // Initial values for the slider
        connect: true,     // Connect the two handles with a bar
        range: {
            min: 1000,        // Minimum value
            max: 40000     // Maximum value
        },
        step: 1,           // Increment step
        format: {
            to: function (value) {
                return Math.round(value); // Round off decimal values
            },
            from: function (value) {
                return value;
            }
        }
    });

    // Link slider to input fields
    var inputMin = document.getElementById('price-min');
    var inputMax = document.getElementById('price-max');

    priceSlider.noUiSlider.on('update', function (values, handle) {
        if (handle === 0) {
            inputMin.value = values[0]; // Set the minimum input value
        } else {
            inputMax.value = values[1]; // Set the maximum input value
        }
    });

    // Sync input fields with slider
    inputMin.addEventListener('change', function () {
        priceSlider.noUiSlider.set([this.value, null]);
    });

    inputMax.addEventListener('change', function () {
        priceSlider.noUiSlider.set([null, this.value]);
    });
});



document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('filter-form');
    const checkboxes = document.querySelectorAll('#filter-form .form-check-input');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            form.submit();
        });
    });
});











})
(jQuery);
