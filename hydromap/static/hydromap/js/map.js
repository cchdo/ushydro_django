var width = 960,
    height = 650;

  var projection = d3.geo.miller()
  .scale(153)
  .translate([width / 2, height / 2])
.rotate([160,0])
  .precision(.1);

var path = d3.geo.path()
  .projection(projection);

  var graticule = d3.geo.graticule();

  var svg = d3.select(".hydromap_container").append("svg")
  .attr("width", "100%")
  .attr("preserveAspectRatio", "xMinYMin meet")
  .attr("viewBox", "0 0 " + width + " " + height );

  svg.append("path")
.datum(graticule)
  .attr("class", "graticule")
  .attr("d", path);

  d3.json("/static/hydromap/data/world-110m.json", function(error, world) {
    svg.insert("path", ".graticule")
    .datum(topojson.feature(world, world.objects.land))
    .attr("class", "land")
    .attr("d", path);

  svg.insert("path", ".graticule")
    .datum(topojson.mesh(world, world.objects.countries, function(a, b) { return a !== b; }))
    .attr("class", "boundary")
    .attr("d", path);
  });
d3.json("/static/hydromap/data/ushydro.json", function(collection) {
  var years = [];
  tracks = svg.selectAll()
  .data(collection.features).enter().append("g")
  .append("svg:a")
  .attr("xlink:href", function(d){return "http://cchdo.ucsd.edu/search?query=" + d.properties.title})
  .attr("target", "_blank");
tracks.append("svg:path")
  .attr("class", "hydro")
  .attr("d", path);
tracks.append("svg:rect")
  .attr("class", "info")
  .attr("x", function(d){ return projection(d.properties.box)[0]-40})
  .attr("y", function(d){ return projection(d.properties.box)[1]-20})
  .attr("width", "75px")
  .attr("height", "40px");
tracks.append("svg:text")
  .attr("x", function(d){ return projection(d.properties.box)[0]})
  .attr("y", function(d){ return projection(d.properties.box)[1]-8})
  .attr("text-anchor", "middle")
  .attr("font-size", "13px")
  .text(function(d){return d.properties.title});
tracks.append("svg:text")
  .attr("x", function(d){ return projection(d.properties.box)[0]})
  .attr("y", function(d){ return projection(d.properties.box)[1]+4})
  .attr("text-anchor", "middle")
  .attr("font-size", "12px")
  .attr("class", "completed")
  .text(function(d){return d.properties.completed});
tracks.append("svg:text")
  .attr("x", function(d){ return projection(d.properties.box)[0]})
  .attr("y", function(d){ return projection(d.properties.box)[1]+16})
  .attr("text-anchor", "middle")
  .attr("font-size", "12px")
  .attr("class", "pending")
  .text(function(d){return d.properties.pending});
for (var c in collection.features){
  years = years.concat(collection.features[c].properties.completed);
  years = years.concat(collection.features[c].properties.pending);
}
$("#hydromap_year_end").text(d3.max(years));
$("#hydromap_year_start").text(d3.min(years));
});

d3.select(self.frameElement).style("height", height + "px");
function hc_size(){
  var hc = $(".hydromap_container");
  hc.height(10 + hc.width() * (height/width));
}

$(window).resize(hc_size);
hc_size();
