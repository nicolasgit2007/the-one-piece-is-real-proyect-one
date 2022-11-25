def main_aorcado():
    import random 
    n = random.randint(0,20)
    x = ("conocer,random,proceso,hermosa,mejorar,interés,aspecto,momento,también,mostrar,valores,función,durante,cumplir,ofrecer,recibir,calidad,motivar,sistema,atender,aplicar,estudio,emoción,control,gracias,extraño,ilusión,caminar,influir,golpear,intensos,guardar,resumen,mensaje,otorgar,generar,empezar,montaña,inferir,cliente,obligar,señalar,afirmar,asistir,detalle,existir,plasmar,muestra,delgado,definir,armonía,exponer,término,obtener,icónico,difícil,honesto,urgente,indicar,ejercer,entidad,negocio,desafío,primero,incluir,castigo,posible,aquello,enfermo,escasez,avanzar,trabajo,esencia,enfoque").split(",")
    palabra = x[n]
    guess = ["_"]*len(palabra)
    w = 0
    tries = 5
    while True:
      t = input()
      flag = False
      for i,p in enumerate(x):
          if p== t:
            flag = True
            guess[i] = p 
      if not flag:
        w+=1
      if w==tries:
        print("ahorcado")
        break
      print("".join(guess))
      if"".join(guess) == x or t == x:
        print("ganador")
        break