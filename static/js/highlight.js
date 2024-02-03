document.addEventListener('DOMContentLoaded', function () {
    window.addEventListener('scroll', function () {
        var position = window.scrollY;
        var sections = document.querySelectorAll('.section');
        var navLinks = document.querySelectorAll('.navbar__link');

        sections.forEach(function (section) {
            var target = section.offsetTop;
            var id = section.getAttribute('id');

            if (position + window.innerHeight / 2 >= target) {
                navLinks.forEach(function (navLink) {
                    navLink.classList.remove('navbar__link--highlighted');
                });

                document.querySelector('.navbar__link[href="#' + id + '"]').classList.add('navbar__link--highlighted');
            }
        });
    });
});
