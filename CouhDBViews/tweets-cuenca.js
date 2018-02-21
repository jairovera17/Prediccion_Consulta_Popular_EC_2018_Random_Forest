function (doc) {
    if (doc.lang == 'es' && doc.place.country_code == 'EC'){   //Tweets solo en español y de Ecuador
      if (doc.user.location){
        var comparar = doc.user.location  
        var res_guayaquil = comparar.match(/^(cuenca|cue)$/i)  //Verificar que la ubicación de usuario es Cuenca
        if(res_guayaquil){
          emit(null,doc.text)
        }
      }
    }
  }