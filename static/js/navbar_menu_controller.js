function handleResizeAndClick() {
    var checkbox = document.getElementById('navbar__toggler');
    var lista = document.getElementById('navbar__menu');

    // callback function added to addEventListener of the list
    function OnClick(e) {
        if (e.target.tagName === "A") {
            checkbox.checked = false;
        }
    }

    if (window.innerWidth < 500) {
        lista.addEventListener("click", OnClick);
    } else {
        checkbox.checked = false;
        lista.removeEventListener("click", OnClick);
    }
}

handleResizeAndClick();

window.addEventListener('resize', handleResizeAndClick, true);
