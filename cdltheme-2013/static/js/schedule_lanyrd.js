// Schedule js

function go_to_anchor() {
    
    var anchor = window.location.hash;

    if ($(anchor).length > 0)
        $('html, body').animate({
        scrollTop: $(anchor).offset().top
    }, 400);

}

function format_times(sessions) {

    for (var i = 0 ; i < sessions.sessions.length ; i++) {
        if (sessions.sessions[i].start_time_epoch) {
            var d = new Date(sessions.sessions[i].start_time_epoch * 1000);
            var m = moment([d.getFullYear(), d.getMonth() + 1, d.getDate(),
                            d.getHours(), d.getMinutes(), d.getSeconds()])
            sessions.sessions[i].start_time = m.format('HH[h]mm');
        }
        else {
            sessions.sessions[i].start_time = "??h??";
        }
        if (sessions.sessions[i].end_time_epoch) {
            var d = new Date(sessions.sessions[i].end_time_epoch * 1000);
            var m = moment([d.getFullYear(), d.getMonth() + 1, d.getDate(),
                            d.getHours(), d.getMinutes(), d.getSeconds()])
            sessions.sessions[i].end_time = m.format('HH[h]mm');
        }
        else {
            sessions.sessions[i].end_time = "??h??";
        }
    }
    return sessions;

}

function from_lanyrd_json(day, space) {

    var jqxhr = $.getJSON('/files/capitole-du-libre-schedule.json', function(data) {
    })
    .done(function(data) {
        
        var partials = { subscribe: "" },
            partial_summary = { subscribe: "" };
        
        if (day == "samedi") {
            sessions = data.sessions[0];
            
        }
        else if (day == "dimanche") {
            sessions = data.sessions[1];
            partials = { subscribe: "<a target='_blank' href='http://www.toulibre.org/capitoledulibre2013:ateliers:{{id}}' class='btn pull-right'>Je m'inscris !</a>" };
            partial_summary = { subscribe: " - <a target='_blank' href='http://www.toulibre.org/capitoledulibre2013:ateliers:{{id}}'>inscription</a>" };
        }

        format_times(sessions);

        if (space) {
            var results = $.grep(sessions.sessions, function(elem) {
                return elem.space == space;
            });
            sessions = {"sessions": results};
        }
        
        var template = $('#summary_tpl').html();
        var html = Mustache.to_html(template,sessions,partial_summary);
        $('#prog-summary').html(html);

        var template = $('#sessions_tpl').html();
        var html = Mustache.to_html(template,sessions,partials);
        $('#prog-details').html(html);
        
        go_to_anchor();
        
    }); 

}

function from_lanyrd_list() {

    var jqxhr = $.getJSON('/files/capitole-du-libre-schedule.json', function(data) {
    })
    .done(function(data) {
        if (day == "samedi") {
            sessions = data.sessions[0];
        }
        else if (day == "dimanche") {
            sessions = data.sessions[1];
        }
        var results = $.grep(sessions.sessions, function(elem) {
            return elem.space == space;
        });
        sessions = {"sessions": results};
            
        var template = $('#summary_tpl').html(),
            html = Mustache.to_html(template,sessions);
        $('#prog-summary').html(html);

        var template = $('#sessions_tpl').html(),
            html = Mustache.to_html(template,sessions);
        $('#prog-details').html(html);
    }); 
}
