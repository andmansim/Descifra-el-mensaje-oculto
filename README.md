# Descifra-el-mensaje-oculto
https://github.com/andmansim/Descifra-el-mensaje-oculto.git
Equipo: Ana López y Andrea Manuel

El cifrado Atbash se basa en reescribir el mensaje original utilizando las letras en espejo del abecedario. Es decir, en vez de la A, escribimos la Z y así. Por tanto, lo que hemos hecho es crear una función que busque en el abecedario original el índice de la letra y sustituirla por la letra del mismo índice del abecedario espejo. Así, devolvemos un mensaje cifrado. 


La fórmula sería: resultado += zxy[abc.index(letra)] --> donde buscamos las letras correspondientes y las acumulamos para generar la clave. 
clave  = sumatorio (27 - xi)
