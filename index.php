<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width,user-scalable=no">
    <meta charset="utf-8">
    <meta property="og:title" content="apres-work.co: Комьюнити будничных райдеров" />
    <meta property="og:description" content="" />
    <meta property="og:url" content="https://apres-work.co" />
    <meta property="og:image" content="http://apres-work.co/images/fuckthejob.png" />

    <meta name="title" content="apres-work.co: Комьюнити будничных райдеров" />
    <meta name="description" content="" />
    <link rel="image_src" href="http://apres-work.co/images/fuckthejob.png" />
    <title>apres-work.co</title>
    <link href='http://fonts.googleapis.com/css?family=Lato:400,700|Kaushan+Script|Montserrat' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Roboto&subset=latin,cyrillic' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <script type="text/javascript" src="js/modernizr.min.js"></script>
</head>
<body>
    <noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5VS7S9" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript><script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start': new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0], j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src= '//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f); })(window,document,'script','dataLayer','GTM-5VS7S9');</script>
    <header>
        <div id="bg_video"></div>
        <i id="i_scroll_down" class="icon-arrow-down animated infinite pulse"></i>
        <div class="titles">
            <h1>apres-work.co</h1>
            <h3>Катаем по будням после работы или учебы</h3>
        </div>
        <div class="social">
            <a class="vk" href="http://vk.com/apresworkco"><i class="icon-vk"></i></a>
            <a class="instagram" href="http://instagram.com/apresworkco"><i class="icon-instagram"></i></a>
        </div>
    </header>
    <section class="instagram-wrap">
        <div class="container">
            <div class="row">
                <div class="col-xs-12">
                    <div class="instagram-content">
                        <h3>Последние фото</h3>
                        <div class="row photos-wrap">
                            <!-- Instafeed target div -->
                            <div id="instafeed"></div>
                            <!-- The following HTML will be our template inside instafeed -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <footer>
        <div class="container site-description">
            <div class="row">
                <div class="col-xs-12">
                    <h4>apres-work это</h4>
                    <p class="about-text">
                        почти что калька с французского apres-ski, только это не алкопати после катания,
                        а катание по будням, после работы или учебы.<br> 
                        <strong>Основная идея - скидка за катание группой</strong>.<br>Работает просто - набирается группа от 8-10 чел и каждый получает скидку на катание или спец.бонус от спота.
<br><br>
Как все происходит: за 3 дня открываем голосование во вконтакте куда едем, за день голосование закрывается и становится доступна страница для записи. <br>Если едешь - оставляй на странице имя и номер телефона, как только наберется группа, ты сразу получишь смс с кодом. Этот код называешь при оплате в парке или на кассе и получаешь скидку.<br><br>
Вот так вот просто: нажал на кнопку - получил скидку.</p>
                    <div class="row contact-form">
                        <form action="iwannago.php" method="POST" id="form_contact">
                            <input class="input-lg" name="name" type="text" id="inp_name" placeholder="Имя">
                            <input class="input-lg" name="phone" type="tel" id="inp_phone" placeholder="Телефон">
                            <button class="contact-now-btn" type="submit" id="btn_wannago">Хочу поехать!</button>
                        </form>
                        <div class="hidden alert alert-success" role="alert">Супер, жди смс! Как только наберется 8 человек мы отправим тебе смс с промо-кодом</div>
                        <div class="hidden alert alert-warning" role="alert">Что-то пошло не так. Попробуй еще раз</div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    <script type="text/javascript" src="js/jquery.min.js"></script>
    <script type="text/javascript" src="js/bootstrap.js"></script>
    <script type="text/javascript" src="js/instafeed.min.js"></script>
    <script type="text/javascript" src="js/tubular.js"></script>
    <script type="text/javascript" src="js/jquery.scrollto.min.js"></script>
    <script type="text/javascript" src="js/app.js?v=2"></script>
    <script>
        $('#btn_wannago').removeAttr('disabled');
        $('#bg_video').tubular({videoId: 'ajPPMBtqY1k'});
        $('#form_contact').on('submit', function(e){
            e.preventDefault();
            $('.contact-form .alert').addClass('hidden');
            $.post($(this).attr('action'),
                $(this).serialize(),
                function(rp){
                    var rpo = JSON.parse(rp);
                    if(rpo.result==0){
                        $('#form_contact').addClass('hidden');
                        $('.contact-form .alert-success').removeClass('hidden');
                    } else {
                        $('.contact-form .alert-warning').removeClass('hidden');
                    }
                }).fail(function(){
                    $('.contact-form .alert-warning').removeClass('hidden');
                }).always(function(){
                    $('#btn_wannago').removeAttr('disabled');
                })
        })
    </script>
</body>
</html>
