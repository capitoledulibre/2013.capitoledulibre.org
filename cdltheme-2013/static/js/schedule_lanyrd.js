// Schedule js

function from_lanyrd_json(day, space) {

    var jqxhr = $.getJSON('/files/capitole-du-libre-schedule.json', function(data) {
    })
    .done(function(data) {
        var template = $('#summary_tpl').html();
        if (day == "samedi") {
            sessions = data.sessions[0];
        }
        else {
            sessions = data.sessions[1];
        }
        var results = $.grep(sessions.sessions, function(elem) {
            return elem.space == space;
        });
        sessions = {"sessions": results};
            
        var html = Mustache.to_html(template,sessions);
        $('#prog-summary').html(html);

        var template = $('#sessions_tpl').html();
        var html = Mustache.to_html(template,sessions);
        $('#prog-details').html(html);
    }); 

}

function from_lanyrd_list() {

    var jqxhr = $.getJSON('/files/capitole-du-libre-schedule.json', function(data) {
    })
    .done(function(data) {
        var template = $('#summary_tpl').html();
        if (day == "samedi") {
            sessions = data.sessions[0];
        }
        else {
            sessions = data.sessions[1];
        }
        var results = $.grep(sessions.sessions, function(elem) {
            return elem.space == space;
        });
        sessions = {"sessions": results};
            
        var html = Mustache.to_html(template,sessions);
        $('#prog-summary').html(html);

        var template = $('#sessions_tpl').html();
        var html = Mustache.to_html(template,sessions);
        $('#prog-details').html(html);
    }); 
}
