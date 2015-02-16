module.exports = function(grunt) {

    // 1. Вся настройка находится здесь
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            // 2. Настройка для объединения файлов находится тут
            dist_js: {
                src: [
        		    'app/static/js/lib/jquery.min.js',
        		    'app/static/js/lib/bootstrap.js',
        		    'app/static/js/lib/instafeed.min.js',
        		    'app/static/js/lib/tubular.js'
                ],
                dest: 'app/static/js/libs.js',
            },
            dist_css: {
                src: [
                    'app/static/css/lib/bootstrap.css',
                    'app/static/css/lib/font-awesome.css',
                    'app/static/css/lib/weather-icons.css',
                    'app/static/css/lib/animate.css',
                    'app/static/css/base.css',
                    'app/static/css/instafeed.css',
                    'app/static/css/webcameras.css'
                ],
                dest: 'app/static/css/style.css'
            }
        },
        uglify: {
            build_js: {
                src  : 'app/static/js/libs.js',
                dest : 'app/static/js/libs.min.js'
            }
        },
        cssmin: {
          options: {
            //shorthandCompacting: false,
            //roundingPrecision: -1,
            keepSpecialComments: 0
          },
          target: {
            files: {
              'app/static/css/style.min.css': ['app/static/css/style.css']
            }
          }
        }

    });

    // 3. Тут мы указываем Grunt, что хотим использовать этот плагин
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin')

    // 4. Указываем, какие задачи выполняются, когда мы вводим «grunt» в терминале
    grunt.registerTask('default', ['concat', 'uglify', 'cssmin']);

};
