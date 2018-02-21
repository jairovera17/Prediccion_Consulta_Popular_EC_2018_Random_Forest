function (doc) {
    if (doc.lang == 'es' && doc.place.country_code == 'EC'){  //Tweets solo en español y de Ecuador
      if (doc.user.location){
        var comparar = doc.user.location;
        var res_quito = comparar.match(/^(quito|uio)$/i)     //Verificar que la ubicación de usuario es Quito
        if (res_quito){
          emit(null,doc.text)
        }
      }
    }
  }