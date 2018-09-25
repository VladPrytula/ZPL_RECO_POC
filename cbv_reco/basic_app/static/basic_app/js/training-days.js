{% load static %}
d3.csv('{ % static "basic_app/data/training-days.csv" % }').then(mileage => {
    
    var group = fc.group()
      .orient('horizontal')
      .key('week');
  
    var groupedMileage = group(mileage);
  
    var colourDomain = groupedMileage[0].map(d =>  d[0]);
    var color = d3.scaleOrdinal(d3.schemeCategory10)
      .domain(colourDomain);
  
    var point = fc.seriesSvgPoint()
        .size(20)
        .crossValue((_, i) =>  i + 1)
        .mainValue(d =>  d[1]);
  
    var line = fc.seriesSvgLine()
        .crossValue((_, i) =>  i + 1)
        .mainValue(d =>  d[1]);
  
    var pointLineSeries = fc.seriesSvgMulti()
      .series([point, line]);
  
    var multiLine = fc.seriesSvgRepeat()
        .series(pointLineSeries)
        .decorate(function(sel) {
          sel.attr('stroke', (_, i) => color(colourDomain[i]))
            .attr('fill', (_, i) => color(colourDomain[i]))
        });
  
    var gridline = fc.annotationSvgGridline()
        .yTicks(5);
    var multi = fc.seriesSvgMulti()
        .series([multiLine, gridline]);
  
    var yExtent = fc.extentLinear()
      .include([0])
      .pad([0, 0.1])
      .accessors([d => d.map(j => j[1])]);
  
    var legend = d3.legendColor()
      .shapeWidth(30)
      .orient('vertical')
      .scale(color);
    
    d3.select('#line-legend')
      .call(legend);
  
    var extent = yExtent(groupedMileage);
    var chart = fc.chartSvgCartesian(
                  d3.scaleLinear(),
                  d3.scaleLinear()
                )
        .xDomain([0.5, 17.5])
        .yDomain(yExtent(groupedMileage))
        .yOrient('left')
        .yTicks(5)
        .yLabel('Running days')
        .xLabel('Week')
        .yNice()
        .chartLabel('Weekly training days')
        .plotArea(multi);
  
    d3.select('#line-chart')
        .datum(groupedMileage)
        .call(chart);
  });