const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module. exports = { lintOnSave: false }

const webpack = require('webpack')
module.exports = defineConfig({
  transpileDependencies : true,
  "publicPath":"/",
  "assetsDir":"static",
  "indexPath":"templetes/index.html",
  configureWebpack:{
    plugins:[
      new webpack.IgnorePlugin({
        resourceRegExp:/^\.\/locales/,
        contextRegExp:/moments/
      }),
    ]
  },
  "filenameHashing":true,

  "devServer":{
    "proxy":{
      "^/api":{
        'target':"http://127.0.0.1:8000", 
        'ws':true,
        'changeOrigin':true,
        "bypass":(req) =>{
          if (req.headers && req.headers.referer){
            req.headers.referer = req.headers.referer.replace('http://localhost:8080', 'http://127.0.0.1:8000')
            req.headers.host = req.headers.host.replace('localhost:8080','127.0.0.1:8000')
          }
        }
      },
      "^/admin":{
        "target":"http://127.0.0.1:8000",
        "ws":true,
        "changeOrigin":true
      },

      "^/accounts":{
        "target":"http://127.0.0.1:8000",
        "ws":true,
        "changeOrigin":true
      },
      
      "^/media":{
        "target":"http://127.0.0.1:8000",
        "ws":true,
        "changeOrigin":true
      },
    }   
  },
})