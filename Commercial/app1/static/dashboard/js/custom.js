$(document).ready(function() {
    $("#collapsebtn").click(function() {
        $("#collapseform").addClass("blockk");
        $("#collapsetable").addClass("nonee");
    });
});

$(document).ready(function() {
    $("#form_close #customer__submit_btn").click(function() {
        $("#collapseform").addClass("nonee");
        $("#collapsetable").addClass("blockk");
    });
});