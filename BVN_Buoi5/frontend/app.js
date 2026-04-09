let offset = 0;
let page = 1;
let cursor = null;

function render(data) {
  const table = document.getElementById("table");

  table.innerHTML = "";

  data.forEach((r) => {
    const row = document.createElement("tr");

    row.innerHTML = `<td>${r.id}</td>
         <td>${r.name}</td>
         <td>${r.email}</td>`;

    table.appendChild(row);
  });
}

async function loadOffset() {
  const res = await fetch(
    `http://localhost:5000/offset?limit=20&offset=${offset}`,
  );
  const json = await res.json();

  document.getElementById("time").innerText = "Query time: " + json.time + "s";

  render(json.data);

  offset += 600000;
}

async function loadPage() {
  const res = await fetch(`http://localhost:5000/page?page=${page}&size=20`);
  const json = await res.json();

  document.getElementById("time").innerText = "Query time: " + json.time + "s";

  render(json.data);

  page += 45000;
}

async function loadCursor() {
  let url = "http://localhost:5000/cursor?limit=20";

  if (cursor) url += "&cursor=" + cursor;

  const res = await fetch(url);

  const json = await res.json();

  document.getElementById("time").innerText = "Query time: " + json.time + "s";

  render(json.data);

  cursor = json.next_cursor + 600000;
}
