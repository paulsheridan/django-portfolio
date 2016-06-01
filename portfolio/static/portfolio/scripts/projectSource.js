(function(module) {
  function Project (details) {
    Object.keys(details).forEach(function(e, index, keys) {
      this[e] = details[e];
    },this);
  }

  Project.all = [];

  Project.prototype.postProj = function(){
    var source = $('#project-template').html();
    var template = Handlebars.compile(source);
    return template(this);
  };

  Project.loadAll = function(rawData) {
    rawData.forEach(function(ele) {
      Project.all.push(new Project(ele));
    });
  };

  Project.fetchAll = function() {
    if (localStorage.rawData) {
      $.ajax({
        type: 'HEAD',
        url: 'data/projects.json',
        success: function(data, message, xhr){
          var neweTag = xhr.getResponseHeader('ETag');
          if(neweTag === localStorage.savedeTag) {
            Project.loadAll(JSON.parse(localStorage.rawData));
            console.log('no change');
            pageView.initPage();
          } else {
            $.getJSON('data/projects.json', function(rawData){
              Project.loadAll(rawData);
              localStorage.rawData = JSON.stringify(rawData);
              localStorage.savedeTag = neweTag;
              pageView.initPage();
            });
          }
        },
      });
    } else {
      $.getJSON('data/projects.json', function(data, message, xhr){
        Project.loadAll(data);
        localStorage.rawData = JSON.stringify(data);
        localStorage.savedeTag = xhr.getResponseHeader('ETag');
        pageView.initPage();
      });
    }
  };

  Project.fetchAll(pageView.initPage);

  module.Project = Project;
})(window);
