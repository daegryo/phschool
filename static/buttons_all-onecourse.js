document.addEventListener("DOMContentLoaded", function() {
    var courseDivs = document.querySelectorAll(".all-onecourse");
    var courseDivs2 = document.querySelectorAll(".onecourse");
    courseDivs.forEach(function(courseDiv) {
        courseDiv.addEventListener("click", function() {
            var courseId = courseDiv.getAttribute("data-course-id");
            window.location.href = "/home/all-courses/" + courseId;
        });
    });
});