function editorLoad(docId) {
    console.log('editor', docId);
    $.ajax(project_url, {
        method: 'GET',
        data: {
            'action': 'doc-meta',
            'doc_id': docId
        }
    }).done((data) => {
        console.log('document', docId, data);
    });
}

function docOptions(docId) {
    console.log('options', docId);
}

function buildDocumentTree(nodes) {
    console.log('tree', nodes);
}

Vue.component('project-node', {
    props: node,
    template: '<div class="document" data-id="{{ node.document.id }}" data-path="{{ node.document.path }}" data-sort="{{ node.document.sort }}"> <div class="info doc-{{ node.document.type }}"> <span class="icon"><i class="fas fa-file"></i></span> <a class="name">{{ node.document.name }}</a> <a class="options"><i class="fas fa-cog"></i></a> </div> {% if node.children|length > 0 %} {{ make_nodes(node.children) }} {% endif %} </div>'
});

$(function() {
    $('.document').each(function(idx, el) {
        var id = $(el).data('id');

        var $link = $('.name', el).first();
        $link.click(() => editorLoad(id));

        var $opts = $('.options', el).first();
        $opts.click(() => docOptions(id));
    });

    $.ajax(project_url, {
        method: 'GET',
        dataType: 'json',
        data: {'action': 'doc-tree'}
    }).done((data) => {
        buildDocumentTree(data);
    });
});