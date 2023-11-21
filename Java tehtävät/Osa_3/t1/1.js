'use strict';

const div = document.querySelector("#target");
const list =
    `<li>First item</li>
    <li>Second item</li>
    <li>Third item</li>`;
div.innerHTML = list;

document.getElementById("target").classList.add("my-list")