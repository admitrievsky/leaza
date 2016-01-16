show_authorization_screen = ->
    $('a#login').click()

$ ->

    $('a#login').click ->
        $(@).colorbox {closeButton: false, href: $(@).attr('href') + '?xhr=xhr'}

    $('div.article div.vote a, div.comment .vote a').on 'click', ->
        $.ajax
            url: "/a/vote/"
            data : JSON.stringify({
                id: $(@).parents('.article, .comment').attr('data-id'),
                mark: if $(@).hasClass('up') then 1 else -1
            }),
            contentType : 'application/json',
            type : 'POST',
            beforeSend: (xhr, settings) ->
                xhr.setRequestHeader("X-CSRFToken", get_csrf_token())
            error: (jqXHR, textStatus, errorThrown) ->
                show_authorization_screen() if jqXHR.status == 403
            success: (data, textStatus, jqXHR) =>
                $(@).parents('.vote').find('.value').text data.now

    $('a.answer-this').on 'click', ->
        parent = $(@).parents('.comment').first()
        $('#id_parent').val(parent.attr('data-id'))
        $('#id_content').val('')
        $('div.wysiwyg-editor').html('')

        $('a.answer-this').show()
        $('a.cancel-answer').hide()
        $('#add-comment-heading').hide()
        $(@).hide()

        $(parent).find('a.cancel-answer').first().show()

        $(parent).find('div.comment-form-placeholder').first().append($('#comment-form'))

    $('a.cancel-answer').on 'click', ->
        $('#id_parent').val('')
        $('#id_content').val('')
        $('div.wysiwyg-editor').html('')

        $('a.answer-this').show()
        $('#add-comment-heading').show()
        $('a.cancel-answer').hide()

        $('#comment-form-wrapper').append($('#comment-form'))