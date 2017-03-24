<!DOCTYPE HTML>
<html>
<meta charset="utf-8">
<head>
<title>Recherche</title>
</head>

<BODY>

<h1>Recherche</h1>
Veuillez remplir le formulaire ci-dessous pour nous contacter : <br/><br/>

<form action="http://localhost:9999/installation" methode="GET">

Type de sport : 

 <select name="sport">
  %for row in rows:
    <option value={{row[0]}}>{{row[1]}}</option>
  %end
</select>



Ville : <input required="required" type="text" name="ville" placeholder="ville"><br/><br/>



<INPUT TYPE="submit" NAME="nom" VALUE="Envoyer">

</FORM>

</body>
<html>