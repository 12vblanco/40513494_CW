// OPENING HOURS
const opening = document.querySelector(".openingjs");

const openingjs = [
  "Mon  13:00 - Midnight ",
  "Tue  13:00 - Midnight ",
  "Wed  13:00 - Midnight ",
  "Thu  13:00 - Midnight ",
  "Fri  13:00 - Midnight ",
  "Sat  13:00 - Midnight ",
  "Sun  13:00 - Midnight ",
];

let html = ``;

openingjs.forEach((openingHours) => {
  html += `<li style="list-style: none; text-align: left;"> ${openingHours} </li>`;
});
opening.innerHTML = html;
// in this case is just to show the use of JavaScript in a flask application
// but if the opening hours appeared in more than one place it would make sense to render them from one place only
