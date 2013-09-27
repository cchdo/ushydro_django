/* Build the S04P progress map.

Construct a map of the region in which S04P (320620110219) takes place and
fill in the cruise positions and correspondence.
*/
google.setOnLoadCallback(function () {
  // prototype.js uses $, so let jQuery be nice.
  jQuery.noConflict();

  // set up a jQuery wrapper to make sure that jQuery is loaded before trying
  // any AJAX requests to populate the map. If jQuery fails to load, the map
  // doesn't get initialized. (FIXME this may be undesirable.)
  jQuery(function () {
    var gm = google.maps;
    var map = new gm.Map2(document.getElementById('map'));
    var track;
    var bounds;

    var icon_letter = new gm.Icon(G_DEFAULT_ICON, '../images/s4p/NBP_blog_letter.png');
    icon_letter.shadow = '';
    icon_letter.transparent = '../images/s4p/NBP_blog_letter_transparency.png';
    icon_letter.iconSize = new gm.Size(50, 31);
    icon_letter.iconAnchor = new gm.Point(25, 31); // move icons upward to show the track better
    icon_letter.imageMap = [1,16,9,6,17,2,21,0,31,6,34,10,60,15,58,39,21,35,16,34,4,35,2,30,1,16];
    var icon_report = new gm.Icon(icon_letter, '../images/s4p/NBP_blog_report.png');
    icon_report.transparent = '../images/s4p/NBP_blog_report_transparency.png';
    icon_report.imageMap = [0,14,17,14,18,4,35,2,28,2,42,2,43,8,47,7,51,20,49,30,1,30,0,17];

    // Set the map to Terrain type. Use setUIToDefault() to obtain Terrain
    // type, which isn't normally in the default map types.
    map.setUIToDefault();
    map.setMapType(G_PHYSICAL_MAP);

    // Request the cruise positions and construct the track that shows the
    // ship's progress.
    jQuery.ajax({
        type: 'GET',
        url: '/progress/positions',
        datatype: 'json',
        success: function (data) {
          // Extract the coordinates from each position object and construct
          // gm.LatLng objects for them for giving to the gm.Polyline
          // constructor.
          var trackpts = data.map(function (pos) {
            return new gm.LatLng(pos.position.latitude, pos.position.longitude);
          });

          // Build the gm.Polyline for the track.
          track = new gm.Polyline(trackpts, '#ADD8E6', 3, 1);

          // Store the view boundaries of the track. We'll be adding things
          // to the map that we still want to be visible, so we need to store
          // this for later.
          bounds = track.getBounds();

          // Add the track to the map and set its initial viewport.
          map.addOverlay(track);
          map.setCenter(bounds.getCenter(), map.getBoundsZoomLevel(bounds));

          // Request correspondence and plot it on the map.
          jQuery.ajax({
              type: 'GET',
              url: '/progress/posts',
              datatype: 'json',
              success: function (data) {
                // Construct a gm.Marker for each email.
                data.map(function (postContainer) {
                  var post = postContainer.post;
                  var pos = new gm.LatLng(post.latitude, post.longitude);
              	  var icon;
              		
                  // Different marker colors for different correspondence types.
                  // No blue, boo-hoo.
                  // http://chart.apis.google.com/chart?
                  //     chst=d_map_pin_letter&chld=%E2%80%A2|9999FF|000000

/*
              		if(post.post_type === 'letter') { icon = G_DEFAULT_ICON; }
                  else { icon = new gm.Icon(G_DEFAULT_ICON,
                      'http://www.google.com/mapfiles/marker_green.png'
                      //'../images/marker_blue.png'
); }      
*/

                  if (post.post_type === 'letter') {
                    icon = icon_letter;
                  } else {
                    icon = icon_report;
                  }

                  // Build the gm.Marker with the colored icon. Tooltip is the
                  // date of the correspondence, %Y-%m-%d.
                  var placemark = new gm.Marker(pos, {icon: icon, title: post.post_date});

                  // Give the marker its excerpt description, which will be
                  // displayed in the info window when the user clicks on the
                  // placemark.
                  placemark.desc = '<div style="font-weight:bold">' + post.post_date + ' ' +
                      (post.post_type === 'letter' ? 'letter from Jim Swift' : 'cruise report') +
                      '<br>' + post.latitude + ', ' + post.longitude + '</div>' +
                      post.excerpt + '<span class="newer"><a href="/blog/' +
                      post.post_type + '/' +
                      post.post_date + '">Read more</a></span>';

                  // Add a listener that opens an info window with a placemark's
                  // description (set above) when it is clicked.
                  gm.Event.addListener(placemark, 'click', function () {
                    this.openInfoWindowHtml(this.desc, {maxWidth: 400});
                  });

                  // Add the placemark to the map.
                  map.addOverlay(placemark);

                  // Make sure the placemark is visible by extending the original
                  // viewing bounds to include it.
                  bounds.extend(pos);
                });

                // Refresh the viewport so that everything is visible.
                map.setCenter(bounds.getCenter(), map.getBoundsZoomLevel(bounds));
              }
          });
        }
    });

    // Make the track change color to dark green (more visible) when the
    // user changes to a map type with a lighter background.
    gm.Event.addListener(map, 'maptypechanged', function () {
      if(map.getCurrentMapType() === G_SATELLITE_MAP ||
          map.getCurrentMapType() === G_HYBRID_MAP) {
        // FIXME This probably doesn't capture all the dark-ocean
        // map types. (Case in point: I had to add the hybrid map type
        // 2011-03-28 17:59.)
        track.setStrokeStyle({color: '#add8e6', weight: 3, opacity: 1});
      } else {
        // G_PHYSICAL_MAP (terrain)
        // G_NORMAL_MAP (streets)
        // FIXME This probably doesn't list all the light-ocean
        // map types either.
        track.setStrokeStyle({color: '#339933', weight: 3, opacity: 1});
      }
    });

    // A debug pointer. Lets us get at the gm.Map2 object that we used.
    window.$gmapobj = map;
  });
});
