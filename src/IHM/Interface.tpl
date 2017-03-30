<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8">
		<title>Recherche</title>
	</head>

	<body>
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

			<input TYPE="submit" NAME="nom" VALUE="Envoyer">
		</form>
	</body>
</html>
