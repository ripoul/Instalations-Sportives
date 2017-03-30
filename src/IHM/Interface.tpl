<!DOCTYPE HTML>
<html>
<meta charset="utf-8">
<head>
<title>Recherche</title>
</head>

<BODY>

<h1>Recherche</h1>
Veuillez remplir le formulaire ci-dessous pour nous contacter : <br/><br/>

<form action="http://localhost:9999/recherche" methode="GET">

Type de sport :

 <select name="sport">
 	<option value="all">all</option>
  %for row in rows[0]:
    <option value={{row[0]}}>{{row[1]}}</option>
  %end
</select>



Ville :

<select name="ville">
	<option value="all">all</option>
  %for row in rows[1]:
    <option value={{row[0]}}>{{row[0]}}</option>
  %end
</select>


<INPUT TYPE="submit" NAME="nom" VALUE="Envoyer">

</FORM>

</body>
</html>
