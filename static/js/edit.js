(function($){
$(function(){
    $('#id_content').wysiwyg({
        toolbar: 'top-selection',
        buttons: {
              smilies: {
                    title: 'Smilies',
                    image: '\uf118',
                    popup: function( $popup, $button ) {
                            var list_smilies = [
                                    '<img src="/static/smiley/afraid.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/amorous.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/angel.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/angry.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/bored.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/cold.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/confused.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/cross.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/crying.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/devil.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/disappointed.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/dont-know.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/drool.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/embarrassed.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/excited.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/excruciating.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/eyeroll.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/happy.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/hot.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/hug-left.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/hug-right.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/hungry.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/invincible.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/kiss.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/lying.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/meeting.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/nerdy.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/neutral.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/party.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/pirate.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/pissed-off.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/question.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/sad.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/shame.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/shocked.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/shut-mouth.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/sick.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/silent.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/sleeping.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/sleepy.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/stressed.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/thinking.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/tongue.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/uhm-yeah.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/wink.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/working.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/bathing.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/beer.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/boy.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/camera.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/chilli.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/cigarette.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/cinema.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/coffee.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/girl.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/console.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/grumpy.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/in_love.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/internet.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/lamp.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/mobile.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/mrgreen.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/musical-note.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/music.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/phone.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/plate.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/restroom.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/rose.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/search.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/shopping.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/star.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/studying.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/suit.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/surfing.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/thunder.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/tv.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/typing.png" width="16" height="16" alt="" />',
                                    '<img src="/static/smiley/writing.png" width="16" height="16" alt="" />'
                            ];
                            var $smilies = $('<div/>').addClass('wysiwyg-plugin-smilies')
                                                      .attr('unselectable','on');
                            $.each( list_smilies, function(index,smiley) {
                                if( index != 0 )
                                    $smilies.append(' ');
                                var $image = $(smiley).attr('unselectable','on');
                                // Append smiley
                                var imagehtml = ' '+$('<div/>').append($image.clone()).html()+' ';
                                $image
                                    .css({ cursor: 'pointer' })
                                    .click(function(event) {
                                        $('#id_content').wysiwyg('shell').insertHTML(imagehtml); // .closePopup(); - do not close the popup
                                    })
                                    .appendTo( $smilies );
                            });
                            var $container = $('#id_content').wysiwyg('container');
                            $smilies.css({ maxWidth: parseInt($container.width()*0.95)+'px' });
                            $popup.append( $smilies );
                            // Smilies do not close on click, so force the popup-position to cover the toolbar
                            var $toolbar = $button.parents( '.wysiwyg-toolbar' );
                            if( ! $toolbar.length ) // selection toolbar?
                                return ;
                            return { // this prevents applying default position
                                left: parseInt( ($toolbar.outerWidth() - $popup.outerWidth()) / 2 ),
                                top: $toolbar.hasClass('wysiwyg-toolbar-bottom') ? ($container.outerHeight() - parseInt($button.outerHeight()/4)) : (parseInt($button.outerHeight()/4) - $popup.height())
                            };
                           },
                    showselection: false
                },
                insertimage: {
                    title: 'Insert image',
                    image: '\uf030',
                    showselection: false
                },
                insertvideo: {
                    title: 'Insert video',
                    image: '\uf03d',
                    showselection: false
                },
                insertlink: {
                    title: 'Insert link',
                    image: '\uf08e',
                    showselection: false
                },
                bold: {
                    title: 'Bold (Ctrl+B)',
                    image: '\uf032',
                    hotkey: 'b'
                },
                italic: {
                    title: 'Italic (Ctrl+I)',
                    image: '\uf033',
                    hotkey: 'i'
                },
                underline: {
                    title: 'Underline (Ctrl+U)',
                    image: '\uf0cd',
                    hotkey: 'u'
                },
                strikethrough: {
                    title: 'Strikethrough (Ctrl+S)',
                    image: '\uf0cc',
                    hotkey: 's'
                }
        },
        submit: {
            title: 'Submit',
            image: '\uf00c'
        },
        placeholderUrl: 'example.com',
        selectImage: 'Click or drop image',
        maxImageSize: [600, 10000],
        videoFromUrl: function( url ) {
                // youtube - http://stackoverflow.com/questions/3392993/php-regex-to-get-youtube-video-id
                var youtube_match = url.match( /^(?:http(?:s)?:\/\/)?(?:[a-z0-9.]+\.)?(?:youtu\.be|youtube\.com)\/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|(?:embed|v|vi|user)\/)([^\?&\"'>]+)/ );
                if( youtube_match && youtube_match[1].length == 11 )
                    return '<iframe src="//www.youtube.com/embed/' + youtube_match[1] + '" width="600" height="338" frameborder="0" allowfullscreen></iframe>';

                // vimeo - http://embedresponsively.com/
                var vimeo_match = url.match( /^(?:http(?:s)?:\/\/)?(?:[a-z0-9.]+\.)?vimeo\.com\/([0-9]+)$/ );
                if( vimeo_match )
                    return '<iframe src="//player.vimeo.com/video/' + vimeo_match[1] + '" width="600" height="338" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>';

                // dailymotion - http://embedresponsively.com/
                var dailymotion_match = url.match( /^(?:http(?:s)?:\/\/)?(?:[a-z0-9.]+\.)?dailymotion\.com\/video\/([0-9a-z]+)$/ );
                if( dailymotion_match )
                    return '<iframe src="//www.dailymotion.com/embed/video/' + dailymotion_match[1] + '" width="600" height="338" frameborder="0" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>';

                return ' ';
            }
    });


})
})(jQuery);