const osm = "https://www.openstreetmap.org/copyright";
const copy = `© <a href='${osm}'>OpenStreetMap</a>`;
const url = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });
//map.fitWorld();
map
  .locate()
  .on("locationfound", (e) =>
    map.setView(e.latlng, 8)
  )
  .on("locationerror", () =>
    map.setView([0, 0], 5)
  );
const layerGroup = L.layerGroup().addTo(map);

// …

async function load_accidents() {
  const accidents_url = `/api/accidents/?in_bbox=${map
    .getBounds()
    .toBBoxString()}`;
  const response = await fetch(
    accidents_url
  );
  const geojson = await response.json();
  return geojson;
}

async function render_accidents() {
  const accidents = await load_accidents();
  layerGroup.clearLayers();
  L.geoJSON(accidents)
    .bindPopup(
      (layer) =>
        layer.feature.properties.name
    )
    .addTo(layerGroup);
}

map.on("moveend", render_accidents);