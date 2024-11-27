$(document).ready(function() {
    // if (window.location.href === window.location.origin + '/') {
    //     $("#primary_header").hide();
    // }
    $('#prompt-form').submit(function() {
        $('#spinner-overlay').css('display', 'flex');
    });

    $('#searchCandidateBtn').click(function(){
        window.location.href = "/";
    });

    const $promptResultBox = $('.prompt-result-box');
    const $mainWrapper = $('#main_wrapper');
    if ($promptResultBox.length && $.trim($promptResultBox.text()) !== "") {
        $mainWrapper.addClass('auto-height');
    }
    const $hamburger = $('#hamburger');
const $closeIcon = $('#close-icon');
const $sidebar = $('#main_sidebar');
const $body = $('body');

// Create overlay
const $overlay = $('<div>', {
    class: 'sidebar-overlay'
});
$body.append($overlay);

function toggleSidebar() {
    if (window.innerWidth <= 768) {
        if ($sidebar.hasClass('active')) {
            closeSidebar();
        } else {
            openSidebar();
        }
    }
}

function openSidebar() {
    $sidebar.css('display', 'block');
    $body.addClass('sidebar-active');
    $overlay.addClass('active');
    setTimeout(() => {
        $sidebar.addClass('active');
    }, 10);
    $hamburger.hide();
    $closeIcon.show();
}

function closeSidebar() {
    $sidebar.removeClass('active');
    $body.removeClass('sidebar-active');
    $overlay.removeClass('active');
    setTimeout(() => {
        $sidebar.css('display', 'none');
    }, 300);
    $closeIcon.hide();
    $hamburger.show();
}

$hamburger.on('click', toggleSidebar);
$closeIcon.on('click', toggleSidebar);
$overlay.on('click', closeSidebar);

$(window).on('resize', function() {
    if (window.innerWidth > 768) {
        $sidebar.css('display', 'block').removeClass('active');
        $body.removeClass('sidebar-active');
        $overlay.removeClass('active');
        $hamburger.hide();
        $closeIcon.hide();
    } else {
        $sidebar.css('display', 'none').removeClass('active');
        $body.removeClass('sidebar-active');
        $overlay.removeClass('active');
        $hamburger.show();
        $closeIcon.hide();
    }
});

// Initial state setup
if (window.innerWidth > 768) {
    $sidebar.css('display', 'block').removeClass('active');
    $hamburger.hide();
    $closeIcon.hide();
} else {
    $sidebar.css('display', 'none').removeClass('active');
    $hamburger.show();
    $closeIcon.hide();
}

});
