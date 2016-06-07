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
    $.ajax({
      type: 'GET',
      url: '/portfolio/projects/',
      dataType: 'json',
      success: function(response){
        Project.loadAll(response);
        pageView.initPage();
      }
    })
  };

  Project.fetchAll(pageView.initPage);

  module.Project = Project;
})(window);
