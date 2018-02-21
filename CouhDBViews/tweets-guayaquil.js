function (doc) {
    if (doc.lang == 'es' && doc.place.country_code == 'EC'){   //Tweets solo en español y de Ecuador
      if (doc.user.location){
        var comparar = doc.user.location  
        var res_guayaquil = comparar.match(/^(guayaquil|gye)$/i)  //Verificar que la ubicación de usuario es Guayaquil
        if(res_guayaquil){
          emit(null,doc.text)
        }
      }
    }
  }