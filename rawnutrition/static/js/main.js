document.addEventListener("DOMContentLoaded", function () {
  var dateContainer = document.getElementById("date-container");
  var today = new Date();

  var options = { weekday: "long", month: "short", day: "numeric" };
  var formattedDate = today.toLocaleDateString("en-US", options); // e.g., "Dec. 31, Sunday"

  dateContainer.textContent = formattedDate;
});