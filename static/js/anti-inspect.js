// Disable right click
document.addEventListener("contextmenu", function (e) {
    e.preventDefault();
});

// Block common DevTools shortcuts
document.addEventListener("keydown", function (e) {

    if (
        e.key === "F12" ||
        (e.ctrlKey && e.shiftKey && e.key === "I") ||
        (e.ctrlKey && e.shiftKey && e.key === "J") ||
        (e.ctrlKey && e.shiftKey && e.key === "C") ||
        (e.ctrlKey && e.key === "U") ||
        (e.ctrlKey && e.key === "S")
    ) {
        e.preventDefault();
        return false;
    }

});

// Detect DevTools open
setInterval(function () {

    if (
        window.outerWidth - window.innerWidth > 160 ||
        window.outerHeight - window.innerHeight > 160
    ) {

        document.body.innerHTML = "<h1>Developer tools are not allowed</h1>";
        window.location.href = "about:blank";

    }

}, 1000);

// Disable drag
document.addEventListener("dragstart", function (e) {
    e.preventDefault();
});