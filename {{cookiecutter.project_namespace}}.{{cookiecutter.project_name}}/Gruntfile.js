const sass = require("node-sass");

module.exports = function(grunt) {
  "use strict";
  grunt.initConfig({
    pkg: grunt.file.readJSON("package.json"),
    // we could just concatenate everything, really
    // but we like to have it the complex way.
    // also, in this way we do not have to worry
    // about putting files in the correct order
    // (the dependency tree is walked by r.js)
    sass: {
      options: {
        implementation: sass,
        sourceMap: true,
        outFile: "css/main.css.map",
        sourceMapRoot: "++theme++{{cookiecutter.project_namespace}}theme/css"
      },
      dist: {
        files: {
          "css/main.css": "scss/main.scss"
        }
      }
    },
    less: {
      plone: {
        options: {
          paths: ["node_modules/bootstrap/less"],
          strictMath: false,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapFileInline: false,
          sourceMapURL:
            "++theme++{{cookiecutter.project_namespace}}theme/css/theme-compiled.less.map",
          sourceMapFilename: "css/theme-compiled.less.map",
          modifyVars: {
            isPlone: "false"
          }
        },
        files: {
          "css/theme.css": "less/theme.local.less"
        }
      },
      theme: {
        options: {
          strictMath: false,
          sourceMap: true,
          outputSourceFiles: true,
          sourceMapFileInline: false,
          // sourceMapURL: "++theme++{{cookiecutter.project_namespace}}theme/css/main.css.map",
          sourceMapFilename: "css/main.css.map",
          modifyVars: {
            isPlone: "false"
          }
        },
        files: {
          "css/main.css": "less/main.less"
        }
      }
    },
    postcss: {
      options: {
        map: {
          prev: "css/",
          annotation: "css/",
          inline: false
        },
        processors: [
          require("postcss-preset-env")({
            browsers: "last 2 versions"
          })
        ]
      },
      dist: {
        src: "css/main.css"
      }
    },
    watch: {
      theme: {
        files: ["less/**/*.less", "barceloneta/less/*.less"],
        tasks: ["less", "postcss"]
      },
      main: {
        files: ["scss/*.scss"],
        tasks: ["sass", "postcss"]
      }
    },
    browserSync: {
      html: {
        bsFiles: {
          src: ["less/*.less", "barceloneta/less/*.less", "*.html"]
        },
        options: {
          watchTask: true,
          debugInfo: true,
          online: true,
          server: {
            baseDir: "."
          }
        }
      },
      plone: {
        bsFiles: {
          src: ["less/*.less", "barceloneta/less/*.less", "*.html", "*.xml"]
        },
        options: {
          watchTask: true,
          debugInfo: true,
          proxy: "localhost:8080",
          reloadDelay: 3000,
          // reloadDebounce: 2000,
          online: true
        }
      }
    }
  });

  // grunt.loadTasks('tasks');
  grunt.loadNpmTasks("grunt-browser-sync");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-contrib-less");
  grunt.loadNpmTasks("grunt-postcss");
  grunt.loadNpmTasks("grunt-sass");

  // CWD to theme folder
  grunt.file.setBase(
    "./src/{{cookiecutter.project_namespace}}.theme/src/{{cookiecutter.project_namespace}}/theme/theme"
  );

  grunt.registerTask("compile", ["less", "postcss"]);
  grunt.registerTask("default", ["compile"]);
  grunt.registerTask("bsync", ["browserSync:html", "watch"]);
  grunt.registerTask("plone-bsync", ["browserSync:plone", "watch"]);
};
