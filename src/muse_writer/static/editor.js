function editorLoad(event) {
    console.log(event)
}

$(function() {
    $('.document').each(function(idx, el) {
        var id = $(el).data('id');
        var $link = $('.name', el).first();
        $link.click(() => editorLoad(id));
    });
});